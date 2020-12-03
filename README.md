Trabalho Prático de Sistemas Distribuídos

Grupo: Alex Lopes, Gabriel Duarte, Guilherme Rocha e Luiz Araújo.

Para executar a API e a interface, é necessário ter o Docker e o Docker-compose instalados. O processo abaixo é para sua instalação:

Métodos de instalação do Docker: 


Windows 10 PRO:

Faça o download do instalador a partir do link: https://www.docker.com/get-started

Faça a instalação seguindo as opções padrão

Abra a aplicação pelo ícone na area de trabalho e abra a interface clicando no submenu, próximo ao relógio, e clicando com o botão direto abra a dashboard.



Linux:

Atualize seu sistema executando os dois comandos abaixo:

sudo apt update
sudo apt upgrade

Assim que atualizar o sistema, você deve instalar alguns dos pacotes necessários antes de instalar o Docker no Ubuntu. Para isso, execute o seguinte comando:

sudo apt-get install curl apt-transport-https ca-certificates software-properties-common

Adicione os repositórios do Docker:

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

Depois disso, apenas atualize a informação do repositório:

sudo apt update

Finalmente, instale o Docker com o comando abaixo:

sudo apt install docker-ce

Para verificar o status da instalação, execute:

sudo systemctl status docker


Com o Docker instalado corretamente, vamos executar a API:

Execute o comando: docker-compose up

Acesse localhost:8001

É possível fazer consultas pela URL, utilize o padrão: http://localhost:8000/consulta_objetos?&format=json&catalogo=&entrada=&titulo=&idioma=&descricao=&palavras_chaves=&cobertura=&estrutura=&nivel_agregacao=&formato=&data=&tamanho=

Exemplos: 
Para buscar um objeto de aprendizagem com o título "Sistemas de Informação", use a URL a seguir. http://localhost:8000/consulta_objetos?&format=json&catalogo=&entrada=&titulo=Sistemas%20de%20Informa%C3%A7%C3%A3o&idioma=&descricao=&palavras_chaves=&cobertura=&estrutura=&nivel_agregacao=&formato=&data=&tamanho=

Para buscar por um objeto de aprendizagem com a data de contribuição "11/9/2020", use a URL a seguir. http://localhost:8000/consulta_objetos?&format=json&catalogo=&entrada=&titulo=&idioma=&descricao=&palavras_chaves=&cobertura=&estrutura=&nivel_agregacao=&formato=&data=2020-11-09&tamanho=

O projeto também está disponível no GitHub por meio do endereço: https://github.com/Alexlr10/TPSD.
