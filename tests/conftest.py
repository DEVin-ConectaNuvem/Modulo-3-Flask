import pytest
from src.app import create_app
from src.app.routes import routes

@pytest.fixture(scope="session")
def app():
  app_on = create_app('testing')
  routes(app_on)
  return app_on