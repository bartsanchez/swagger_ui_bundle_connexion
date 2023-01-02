import pytest
from app import app as flask_app
import re


@pytest.fixture()
def client():
    with flask_app.app.test_client() as c:
        yield c


def test_200_OK(client):
    response = client.get('/foo')
    assert response.status_code == 200


def test_version(client):
    response = client.get('/ui/swagger-ui-bundle.js')

    assert response.status_code == 200

    content = response.text
    version = re.findall(r'PACKAGE_VERSION:\"(\d+.\d+.\d+)"', content)

    assert version == ['4.14.0']
