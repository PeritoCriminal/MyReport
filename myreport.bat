@echo off
REM Ativar o ambiente virtual
cd C:\Users\capri\Desktop\MyReport
CALL venv\Scripts\activate.bat

REM Iniciar o servidor Django em segundo plano
start /B python manage.py runserver

REM Abrir o navegador na página inicial
start "" http://localhost:8000/

REM Esperar até que o navegador seja fechado
echo Aguardando o fechamento do navegador...
tasklist /FI "IMAGENAME eq chrome.exe" /FO CSV > NUL 2>&1

:loop
tasklist /FI "IMAGENAME eq chrome.exe" /FO CSV > NUL 2>&1
IF ERRORLEVEL 1 (
    echo Navegador fechado. Parando o servidor...
    taskkill /F /IM python.exe > NUL 2>&1
    exit
) ELSE (
    timeout /T 1 > NUL
    goto loop
)
