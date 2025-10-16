import pdfplumber
import pandas as pd
import re

pdf = pdfplumber.open("demonstrativo.pdf")
pages = pdf.pages
num_operacao = pages[0].extract_table()[3][2]
dados = []

def extract_value(text):
     padrao = r"(?:R\$\s*)?\d{1,3}(?:[\.\s]?\d{3})*(?:[.,]\d{2})?"
     valor = re.findall(padrao, text)[0]
     return valor

def extract_table(page):
    tables = page.extract_table()
    for table in tables:
        if "200 - PAGTO" in table[0] or "707 - BX" in table[0]:
            table_clear = table[0].replace("DESC FOLHA", "").replace("REFIN", "").replace("REFI", "").replace("SDO","")
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
    dados_tabela = { 
        "Data": datas,
          "Valor bruto": valor_bruto,
            "Retenção/Valor Pago": "",
              "Historico": parcelas,
                }
    
df = pd.DataFrame(dados_tabela)
nome_arquivo = 'relatorio_simples.xlsx'
df.to_excel( nome_arquivo, sheet_name='Dados', index=False)
print(f"Planilha '{nome_arquivo}' criada com sucesso!")