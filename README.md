Trabalho Prático de Sistemas Distribuídos

Grupo: Alex Lopes, Gabriel Duarte, Guilherme Rocha e Luiz Araújo.

Como executar a API:

* Instale alguma versão do Python (3.5, 3.6, 3.7, 3.8, 3.9)
* Para a instalação dos pacotes recomendamos a utilização do comando "sudo", para que o usuário tenha as permissões necessárias para tal
* Navegue até a pasta back_end
    * Instale o ambiente virtual env
        * apt-get install python3.6-venv
    * Ative-o
        * Ativando em ambiente Unix: source env/bin/activate
    * Instale os pacotes:
        * pip install django
        * pip install djangorestframework
        * pip install markdown       # Markdown support for the browsable API.
        * pip install django-filter  # Filtering support
        * pip install django-cors-headers
    * Execute o comando:
        * python manage.py migrate
    * Inicie o servidor
        * python manage.py runserver
    * Acesse localhost:8000/objetos
        * Para visualizar os objetos de aprendizagem em formato JSON selecione a opção "json" através do botão "GET"


Como executar a interface para consulta:

* Instale o npm
* Navegue até a pasta front_end
    * Instale as bibliotecas necessárias da seguinte maneira:
        * npm install react-router-dom
        * npm install react-icons
        * npm install axios
        * npm install react-bootstrap
        
    Excute o comando:
        * npm start
    
    Acesse localhost:8001
        

O projeto também está disponível no GitHub por meio do endereço: https://github.com/Alexlr10/TPSD.
