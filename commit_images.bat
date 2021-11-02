set MIS_DOCKER_NAME=python3.6_flask_001
set MIS_DOCKER_IMAGE="python3.6_flask:flask_001"
set MIS_DOCKER_HOSTNAME=PYTHON_3.6_FLASK_001
set MIS_ROOT=%~dp0
set datestr=%date%

for /f %%i in ('docker ps -aqf "name=%MIS_DOCKER_NAME%"') do If not "%%i" == "" (
	docker commit %%i %MIS_DOCKER_IMAGE%
  ) else (
    echo "No Container running"
)


