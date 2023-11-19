# Canvassistant
```shell
cd backend

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```
Running Backend
```shell
cd app

uvicorn main:app --reload
```
Running File Upload
```shell
cd frontend

streamlit run submission.py  
```

Freezing pip packages
```shell
pip freeze > requirements.txt
```
