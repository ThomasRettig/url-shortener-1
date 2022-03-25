import pytest
from urlshort import create_app
#call the app for testing
@pytest.fixture
def app():
    app = create_app()
    yield app
@pytest.fixture
def client(app):
    return app.test_client()
