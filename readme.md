Esse projeto é um sistema de blog, desenvolvido utilizando: Framework Django (Python), HTML, CSS, Javascript e Bootstrap.

Como executar o projeto?
1 - Clonar repositório no git através do comando -> git clone https://github.com/Jonathas-Vidal/DjangoBlog
2 - Criar um ambiente virtual (venv) -> (Certifique de estar na raiz, por exemplo C:Users\DjangoBlog) - python -m venv .venv
3 - Ativar o ambiente virtual -> .\.venv\Scripts\activate (Caso dê erro de powershell, execute -> Set-ExecutionPolicy Bypass CurrentUser
4 - Instalar as dependências e bibliotecas: pip install -r requirements.txt
5 - Popular o banco de dados -> python manage.py makemigrations , e em seguida: python manage.py migrate
6 - Executar o projeto -> python manage.py runserver.
7 - Ir até http://127.0.0.1:8000/ no navegador de sua preferência.
