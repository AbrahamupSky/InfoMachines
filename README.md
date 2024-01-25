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
  - Una vez con eso, tenemos que activar el entorno virtual:
    - # Windows:
      - .\venv\Scripts\activate
    - # MacOS / Linux:
      - source venv/bin/activate
     
    - Con eso, en nuestra terminal deberiamos ver 'venv' al principio, ya con eso tenemos el entorno virtual de python activado.
  
  - pip3 install -r requirements.txt
  - python3 manage.py runserver
3. Con eso deberia estar corriendo ya en nuestra PC en el 'https://localhost:8000/'
