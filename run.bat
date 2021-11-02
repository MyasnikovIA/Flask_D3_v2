rem docker run --rm -d -p 8008:80 -p 2222:22 --name misxcontainer --hostname MED-DEV-DARMAEV-DOCKER -v "C:/bars/www:/var/www/html" centos7/mis

set MIS_DOCKER_NAME=python3.6_d3ext
set MIS_DOCKER_IMAGE="python3.6_flask:d3ext"
set MIS_DOCKER_HOSTNAME=PYTHON_3.6_D3EXT
set MIS_ROOT="%~dp0app"
set MIS_PORT_WEB=9091
set MIS_PORT_SERVICE=5000


docker run --rm -d -p %MIS_PORT_WEB%:5000  -p %MIS_PORT_SERVICE%:8080   --name %MIS_DOCKER_NAME% --hostname %MIS_DOCKER_HOSTNAME% -v %MIS_ROOT%:/app  %MIS_DOCKER_IMAGE%
timeout 10
start "" "http://127.0.0.1:%MIS_PORT_WEB%/" 

