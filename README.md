# sistemaulasparticular

Orientações para execução do projeto em uma máquina local.

1 - Clone esse repositório.

2 - Crie um virtualenv com Python 3.

3 - Ative o virtualenv.

4 - Instale as dependências.

5 - Rode as migrações.

6 - Rode o projeto

Windows:

git clone https://github.com/cleocardoso/WorkBook.git

python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

Linux:

git clone https://github.com/cleocardoso/WorkBook.git

sudo apt install python3-venv

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py runserver
