<p align="center">
  <a href="#title">Projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp; 
  <a href="#requirements">Pré-requisitos</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#rodando">Rodando a aplicação</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#technologies">Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp; 
</p>

<h1 id="title">💻 Projeto extrator de tabelas pdf</h1>

<p>&nbsp; Essa aplição foi feita para extrair tabelas de um pdf de demonstrativo de pagamentos</p>

<h2 id="requirements">:hammer: Pré-requisitos</h1>

<p>&nbsp;Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas: <a href="https://git-scm.com">Git</a>, <a href="https://www.python.org/">Python</a>, <a href="https://nodejs.org/pt-br/">NodeJS</a>, um bom editor de texto para trabalhar com o código como o <a href="https://code.visualstudio.com/">VSCode</a>.</p>

<h2 id="rodando">:game_die: Rodando a aplicação</h2>

```bash
# Clone este repositório
$ git clone https://github.com/LuisFelipe777/Extrator-de-PDF


#API
# Acesse a pasta da API no terminal/cmd
$ cd server

# Instale as dependências Python usando o arquivo requirements.txt
$ pip install -r requirements.txt

# Rode a API com Uvicorn
$ uvicorn main:app --reload

# A API irá rodar, por padrão, em `http://127.0.0.1:8000`.

#FRONT
# Acesse a pasta do front-end no terminal/cmd
$ cd client

# Acesse api.js e coloque o link da api que faz o precesso da extração
$ const response = await fetch("http://coloque_o_link_aqui/processar_pdf",

# Feito isso, instale as dependencias do projeto
$ npm install

# Agora você pode executar a aplicação usando npm run dev
$ npm run dev

```

<h2 id="technologies">✨ Tecnologias</h2>

As seguintes ferramentas foram usadas na construção do projeto:

- [Python](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/)
- [FastApi](https://www.python.org/)
- [pdfplumber](https://pypi.org/project/pdfplumber/)
- [openpyxl](https://pypi.org/project/openpyxl/)
- [Node.js](https://nodejs.org/en/)
- [Vite(react)](https://vite.dev/)
