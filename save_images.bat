rem docker run --rm -d -p 8008:80 -p 2222:22 --name misxcontainer --hostname MED-DEV-DARMAEV-DOCKER -v "C:/bars/www:/var/www/html" centos7/mis
set MIS_DOCKER_NAME=python3.8_d3ext
set MIS_DOCKER_IMAGE="python3.8_flask:d3ext"
set MIS_DOCKER_HOSTNAME=PYTHON_3.8_D3EXT
set MIS_ROOT_IMG=%~dp0
set datestr=%date%

docker save -o %MIS_ROOT_IMG%Flask_001(%datestr%).tar %MIS_DOCKER_IMAGE% 

