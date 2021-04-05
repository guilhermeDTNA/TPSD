<h3>Trabalho Prático de Sistemas Distribuídos</h3>

<h4>Grupo: Alex Lopes, Gabriel Duarte, Guilherme Rocha e Luiz Araújo.</h4>

Para executar a API e a interface, é necessário ter o Docker e o Docker-compose instalados. O processo abaixo é para sua instalação:

Métodos de instalação do Docker: 

<b>Windows 10 PRO:</b>

Faça o download do instalador a partir do link: <a href="https://www.docker.com/get-started">https://www.docker.com/get-started</a>

Faça a instalação seguindo as opções padrão

Abra a aplicação pelo ícone na area de trabalho e abra a interface clicando no submenu, próximo ao relógio, e clicando com o botão direto abra a dashboard.

<b>Linux:</b>

Atualize seu sistema executando os dois comandos abaixo:

```console

sudo apt update
sudo apt upgrade

```

Assim que atualizar o sistema, você deve instalar alguns dos pacotes necessários antes de instalar o Docker no Ubuntu. Para isso, execute o seguinte comando:

```console
sudo apt-get install curl apt-transport-https ca-certificates software-properties-common

```

Adicione os repositórios do Docker:

```console

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

```

Depois disso, apenas atualize a informação do repositório:

```console

sudo apt update

```

Finalmente, instale o Docker com o comando abaixo:

```console

sudo apt install docker-ce

```

Para verificar o status da instalação, execute:

```console

sudo systemctl status docker

```

Com o Docker instalado corretamente, vamos executar a API:

Execute o comando: 

```console

COMPOSE_HTTP_TIMEOUT=200 docker-compose up

```

Acesse <a href="localhost:8001">localhost:8001</a>

É possível fazer consultas pela URL, utilize o padrão: <a href="http://localhost:8000/consulta_objetos?&format=json&catalogo=&entrada=&titulo=&idioma=&descricao=&palavras_chaves=&cobertura=&estrutura=&nivel_agregacao=&formato=&data=&tamanho=">http://localhost:8000/consulta_objetos?&format=json&catalogo=&entrada=&titulo=&idioma=&descricao=&palavras_chaves=&cobertura=&estrutura=&nivel_agregacao=&formato=&data=&tamanho=</a>

<b>Exemplos:</b>
 
Para buscar um objeto de aprendizagem com o título "Sistemas de Informação", use a URL a seguir. <a href="http://localhost:8000/consulta_objetos?&format=json&catalogo=&entrada=&titulo=Sistemas%20de%20Informa%C3%A7%C3%A3o&idioma=&descricao=&palavras_chaves=&cobertura=&estrutura=&nivel_agregacao=&formato=&data=&tamanho=">http://localhost:8000/consulta_objetos?&format=json&catalogo=&entrada=&titulo=Sistemas%20de%20Informa%C3%A7%C3%A3o&idioma=&descricao=&palavras_chaves=&cobertura=&estrutura=&nivel_agregacao=&formato=&data=&tamanho=</a>

Para buscar por um objeto de aprendizagem com a data de contribuição "11/9/2020", use a URL a seguir. <a href="http://localhost:8000/consulta_objetos?&format=json&catalogo=&entrada=&titulo=&idioma=&descricao=&palavras_chaves=&cobertura=&estrutura=&nivel_agregacao=&formato=&data=2020-11-09&tamanho=">http://localhost:8000/consulta_objetos?&format=json&catalogo=&entrada=&titulo=&idioma=&descricao=&palavras_chaves=&cobertura=&estrutura=&nivel_agregacao=&formato=&data=2020-11-09&tamanho=</a>

O projeto também está disponível no GitHub por meio do endereço: <a href="https://github.com/Alexlr10/TPSD">https://github.com/Alexlr10/TPSD</a>.
