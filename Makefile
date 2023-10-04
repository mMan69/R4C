SERVICE=robot-factory

build:
	docker build --rm --force-rm -t $(SERVICE) .
up:
	docker run --name $(SERVICE) -p 8000:8000 --rm -v ${PWD}:/app -it $(SERVICE) ./start.sh
bash:
	docker exec -it $(SERVICE) /bin/bash
test:
	docker exec -it $(SERVICE) pytest $T

# Запустить отдельный тест
# T=tests/test_robots.py::TestCreateRobot::test_post_create_robot make test


