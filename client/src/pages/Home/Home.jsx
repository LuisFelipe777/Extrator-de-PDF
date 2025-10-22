import "./Home.css";
import btnDownload from "../../assets/download.png";
import btnUpload from "../../assets/upload.png";
import { useState } from "react";
import api from "../../services/api";

function Home() {
  const [pdfFile, setPdfFile] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [nameFile, setNameFile] = useState("");

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    if (file && file.type !== "application/pdf") {
      alert("Por favor, selecione um arquivo no formato PDF.");
      setPdfFile(null);
    } else {
      setPdfFile(file);
      setNameFile(file.name);
    }
  };

  const handleSubmit = async () => {
    if (!pdfFile) {
      alert("Nenhum arquivo selecionado.");
      return;
    }
    try {
      setIsLoading(true);
      const formDataParaEnvio = new FormData();
      formDataParaEnvio.append("file", pdfFile);
      await api(formDataParaEnvio, nameFile);
    } catch (error) {
      throw new Error(error);
    } finally {
      setIsLoading(false);
    }
  };
  return (
    <div className="Home">
      <div className="buttons">
        <div className="btn-upload">
          <input type="file" name="" id="" onChange={handleFileChange} />
          <img src={btnUpload} alt="" height={"40px"} />
          Importar PDF
        </div>
        <div className="btn-dowload" onClick={handleSubmit}>
          <input type="button" />
          <img src={btnDownload} alt="" height={"40px"} />
          Baixar Excel
        </div>
        <div className="file">
          <p>{nameFile}</p>
        </div>
        {isLoading ? (
          <div>
            <p>Processando arquivo...</p>
          </div>
        ) : null}
      </div>
    </div>
  );
}

export default Home;
