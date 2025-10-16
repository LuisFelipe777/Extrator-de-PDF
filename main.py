from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
import pdfplumber
import pandas as pd
import re
from io import BytesIO

app = FastAPI()

def extract_value(text):
    padrao = r"(?:R\$\s*)?\d{1,3}(?:[\.\s]?\d{3})*(?:[.,]\d{2})?"
    valor = re.findall(padrao, text)[0]
    return valor

def process_pdf(file_bytes):
    pdf = pdfplumber.open(BytesIO(file_bytes))
    pages = pdf.pages
    num_operacao = pages[0].extract_table()[3][2]
    dados = []

    def extract_table(page):
        tables = page.extract_table()
        for table in tables:
            if "200 - PAGTO" in table[0] or "707 - BX" in table[0]:
                table_clear = table[0].replace("DESC FOLHA", "").replace("REFIN", "").replace("REFI", "").replace("SDO", "")
                for linha in table_clear.split("\n"):
                    if ("200 - PAGTO") in linha or ("707 - BX") in linha:
                        dados.append([linha.split(" ")[10], linha.split(" ")[1], extract_value(linha.split(" ")[11])])
    for page in pages:
        extract_table(page)

    datas = []
    valor_bruto = []
    parcelas = []

    for dado in dados:
        datas.append(dado[0])
        parcelas.append(num_operacao + " - " + dado[1])
        valor_bruto.append(dado[2])

    df = pd.DataFrame({
        "Data": datas,
        "Valor bruto": valor_bruto,
        "Retenção/Valor Pago": "",
        "Historico": parcelas,
    })

    output = BytesIO()
    df.to_excel(output, index=False, sheet_name="Dados")
    output.seek(0)
    return output

@app.post("/processar_pdf")
async def processar_pdf(file: UploadFile = File(...)):
    file_bytes = await file.read()
    excel_file = process_pdf(file_bytes)
    return StreamingResponse(
        excel_file,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={"Content-Disposition": "attachment; filename=relatorio.xlsx",
                 }
    )
