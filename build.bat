@echo off
set MIS_DOCKER_NAME=python3.8_d3ext
set MIS_DOCKER_IMAGE="python3.8_flask:d3ext"
set MIS_DOCKER_HOSTNAME=PYTHON_3.8_D3EXT
set MIS_ROOT="%~dp0app"
set MIS_PORT_WEB=9091



echo [*] Building docker image '%MIS_DOCKER_IMAGE%'
docker build -t %MIS_DOCKER_IMAGE%  .
if errorlevel 1 (
    goto ERRDOCKERBUILD
)
echo [*] Building docker image '%MIS_DOCKER_IMAGE%' finished
goto END

:ERRDOCKERBUILD
echo [!] Could not build docker image '%MIS_DOCKER_IMAGE%'

:END
rem Удалить исходный образ с которого собирался
rem docker rmi python:3.6




