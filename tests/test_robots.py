import json
import http

import pytest


# T=tests/test_robots.py::TestCreateRobot make test
class TestCreateRobot:

    # T=tests/test_robots.py::TestCreateRobot::test_post_create_robot make test
    @pytest.mark.django_db(transaction=True)
    def test_post_create_robot(self, client):
        json_robot = {
            'model': 'll',
            'version': 'll',
            'created': '2022-12-31 23:59:59'
        }
        response = client.post(
            '/robots/create',
            json.dumps(json_robot),
            content_type="application/json"
        )

        assert response.status_code == http.HTTPStatus.CREATED
        assert response.json()['message'] == 'Robot created successfully'

    # T=tests/test_robots.py::TestCreateRobot::test_get_create_robot make test
    def test_get_create_robot(self, client):
        response_get = client.get('/robots/create')

        assert response_get.status_code == http.HTTPStatus.METHOD_NOT_ALLOWED
        assert response_get.json()['message'] == 'Invalid request method'

    # T=tests/test_robots.py::TestCreateRobot::test_error_form_create_robot make test
    def test_error_form_create_robot(self, client):
        json_robot = {
            'model': 'lll',
            'version': 'll',
            'created': '2022-12-31 23:59:59'
        }
        response = client.post(
            '/robots/create',
            json.dumps(json_robot),
            content_type="application/json"
        )

        assert response.status_code == http.HTTPStatus.BAD_REQUEST
        assert 'errors' in response.json()

    # T=tests/test_robots.py::TestCreateRobot::test_invalid_json_create_robot make test
    def test_invalid_json_create_robot(self, client):
        invalid_json = '{"test":123,}'
        response = client.post(
            '/robots/create',
            invalid_json,
            content_type="application/json"
        )

        assert response.status_code == http.HTTPStatus.BAD_REQUEST
        assert response.json()['message'] == 'Invalid json'
