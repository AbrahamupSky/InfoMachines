Para abrir el programa:

## Docker
1. Clonar el repo
2. En terminal poner:
  - docker build -t infomachines .
  - docker run -p 8000:8000 infomachines
    
3. Listo

## No Docker
1. Clonar el repo
2. En terminal poner:
  - python3 -m venv venv
  - pip3 install -r requirements.txt
  - python3 manage.py runserver
3. Con eso deberia estar corriendo ya en nuestra PC en el 'https://localhost:8000/'
