set MIS_DOCKER_NAME=python3.8_d3ext
set MIS_DOCKER_IMAGE="python3.8_flask:d3ext"
set MIS_DOCKER_HOSTNAME=PYTHON_3.8_D3EXT
set MIS_ROOT=%~dp0
set datestr=%date%
for /f %%i in ('docker ps -aqf "name=%MIS_DOCKER_NAME%"') do If not "%%i" == "" (
	docker commit %%i %MIS_DOCKER_IMAGE%
  ) else (
    echo "No Container running"
)


