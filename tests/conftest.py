import pytest
from src.app import create_app, DB
from src.app.routes import routes
from flask import json
from sqlalchemy import event
from src.app.models.user import User

mimetype = 'application/json'
headers = {
    'Content-Type': mimetype,
    'Accept': mimetype
}

@pytest.fixture(scope="session")
def app():
  app_on = create_app('testing')
  routes(app_on)
  return app_on

@pytest.fixture
def logged_in_client(client):
  data = {
      "email": "luislopes@gmail.com",
      "password": "123Mudar!"
  }

  response = client.post("user/login", data=json.dumps(data), headers=headers)
  return response.json["token"]

@pytest.fixture
def logged_in_client_with_user_deleted(client):
  data = {
      "email": "loivaci.lopes1@example.com",
      "password": "123Mudar!"
  }

  response = client.post("user/login", data=json.dumps(data), headers=headers)
  user = User.query.filter(User.id == 33).first()
  user.roles = []
  DB.session.commit()
  User.query.filter(User.id == 33).delete()
  
  return response.json["token"]

@pytest.fixture(scope="function", autouse=True)
def session(app):
    with app.app_context():
        connection = DB.engine.connect()
        transaction = connection.begin()
        options = dict(bind=connection, binds={})
        sess = DB.create_scoped_session(options=options)
        sess.begin_nested()

        @event.listens_for(sess(), 'after_transaction_end')
        def restart_savepoint(sess2, trans):
            if trans.nested and not trans._parent.nested:
                sess2.expire_all()
                sess2.begin_nested()

        DB.session = sess
        #O yield faz parte do protocolo de iteradores do python, ele evita você ter que criar o elemento iterável efetivamente, tornando seu código mais escalável
        yield sess 
        sess.remove()
        transaction.rollback()
        connection.close()
