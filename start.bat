@echo off
set CONTAINER_NAME=python
set APP_URL=http://localhost:8501

echo Verificando se o container "%CONTAINER_NAME%" existe...

docker ps -a --format "{{.Names}}" | findstr /i /c:"%CONTAINER_NAME%" > nul
if %errorlevel% neq 0 (
    echo Container nao encontrado. Iniciando build.
    docker-compose build
) else (
    echo Container "%CONTAINER_NAME%" ja existe
)

echo Iniciando aplicação
docker-compose up -d

echo Aguardando o container iniciar...

:wait_for_streamlit
docker logs %CONTAINER_NAME% 2>&1 | findstr /C:"You can now view your Streamlit app in your browser" > nul
if %errorlevel% neq 0 (
    timeout /t 1 > nul
    goto wait_for_streamlit
)

echo Streamlit pronto no container %CONTAINER_NAME%!

echo Container em execucao!

timeout /t 3 > nul

echo Abrindo %APP_URL% no navegador...
start %APP_URL%
