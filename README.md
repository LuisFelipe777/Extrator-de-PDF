<p align="center">
  <a href="#title">Projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp; 
  <a href="#requirements">Pré-requisitos</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#rodando">Rodando a API</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#technologies">Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp; 
</p>

<h1 id="title">💻 Projeto extrator de tabelas pdf API</h1>

<p>&nbsp; Essa API foi feita para extrair tabelas de um pdf de demonstrativo de pagamentos</p>

<h2 id="requirements">:hammer: Pré-requisitos</h1>

<p>&nbsp;Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas: <a href="https://git-scm.com">Git</a>, <a href="https://www.python.org/">Python</a>, um bom editor de texto para trabalhar com o código como o <a href="https://code.visualstudio.com/">VSCode</a>.</p>

<h2 id="rodando">:game_die: Rodando a API</h2>

```bash
# Clone este repositório
$ git clone https://github.com/ErikPervious/BlogApp-Insider

# Acesse a pasta do projeto no terminal/cmd
$ cd EXTRAÇÂO-PDF

# Instale as dependências Python usando o arquivo requirements.txt
$ pip install -r requirements.txt

# Rode a API com Uvicorn
$ uvicorn main:app --reload

# A API irá rodar, por padrão, em `http://127.0.0.1:8000`.
```

<h2 id="technologies">✨ Tecnologias</h2>

As seguintes ferramentas foram usadas na construção do projeto:

- [Python](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/)
- [FastApi](https://www.python.org/)
- [pdfplumber](https://pypi.org/project/pdfplumber/)
- [openpyxl](https://pypi.org/project/openpyxl/)
