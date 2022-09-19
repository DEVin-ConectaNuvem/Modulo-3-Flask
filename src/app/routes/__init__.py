from flask import Flask
from src.app.controllers.technologies import technology
from src.app.controllers.developers import developers
from src.app.controllers.cities import cities
from src.app.controllers.states import states
from src.app.controllers.coutries import countries
from src.app.controllers.users import user

def routes(app: Flask):
  app.register_blueprint(technology)
  app.register_blueprint(developers)
  app.register_blueprint(cities)
  app.register_blueprint(states)
  app.register_blueprint(countries)
  app.register_blueprint(user)