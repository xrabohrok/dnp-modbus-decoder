@echo off
start python manage.py runserver
timeout /t 3 /nobreak
start http://localhost:8000/Power/DNP3/DNP3/