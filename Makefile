SERVICE=robot-factory

build:
	docker build --rm --force-rm --tag $(SERVICE) .
up:
	docker run --name $(SERVICE) -p 8000:8000 --rm -v ${PWD}:/app -it $(SERVICE) ./start.sh
bash:
	docker run -v ${PWD}:/app -it $(SERVICE) /bin/bash
