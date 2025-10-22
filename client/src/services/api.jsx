async function api(formData, name) {
  const response = await fetch("http://127.0.0.1:8000/processar_pdf", {
    method: "POST",
    body: formData,
  });
  if (!response.ok) {
    throw new Error("Erro ao baixar o arquivo");
  }
  const blob = await response.blob();
  const url = window.URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = `${name}.xlsx`.replace(".pdf", "");
  document.body.appendChild(a);
  a.click();
  a.remove();
  window.URL.revokeObjectURL(url);
}

export default api;
