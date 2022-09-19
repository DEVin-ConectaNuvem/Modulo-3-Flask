from sqlalchemy.sql.expression import func
import requests

from src.app.models.city import City, cities_share_schema
from src.app.models.developer import Developer
from src.app.models.state import State, states_share_schema
from src.app.models.country import Country, country_share_schema
from src.app.models.user import User, users_share_schema
from src.app.models.technology import Technology
from src.app.models.role import Role
from src.app.models.permission import Permission
from src.app.utils import is_table_empty

def populate_db_country():
  if is_table_empty(Country.query.first(), 'countries'):
      Country.seed('Brazil' , 'Português')
      print('Countries populated')

def populate_db_state():
  if is_table_empty(State.query.first(), 'states'):
      country = Country.query.first()
      country_dict = country_share_schema.dump(country)
      states_data = requests.get("https://servicodados.ibge.gov.br/api/v1/localidades/estados")
      for stateObject in states_data.json():
          State.seed(
          country_dict['id'],
          stateObject['nome'],
          stateObject['sigla']
          )
      print('States populated')

def populate_db_city():
  if is_table_empty(City.query.first(), 'cities'):
      cities_data = requests.get("https://servicodados.ibge.gov.br/api/v1/localidades/municipios")
      state = State.query.order_by(State.name.asc()).all()
      state_dict = states_share_schema.dump(state)

      for city_object in cities_data.json():
          state_id = 0
          for state_object in state_dict:
              if state_object['initials'] == city_object['microrregiao']['mesorregiao']['UF']['sigla']:
                  state_id = state_object['id']
          City.seed(
          state_id,
          city_object['nome']
          )
      print('Cities populated')

def populate_db_permissions_and_roles():
  permissions = ['DELETE', 'READ', 'WRITE', 'UPDATE']
  roles = ['OWNER', 'HELPER']

  if is_table_empty(Permission.query.first(), 'permissions'):
    for permission in permissions:
      Permission.seed(
        permission
      )
    
    permissions_helper = Permission.query.filter(
      Permission.description.in_([
        'READ', 'WRITE'
      ])
    ).all()

    permissions_owner = Permission.query.all()
    print("Permissions populated")

    if is_table_empty(Role.query.first(), 'roles'):
      for index, role in enumerate(roles):
        if index == 0:
          Role.seed(
            role,
            permissions_owner
          )
        else:
          Role.seed(
            role,
            permissions_helper
          )
      print("Roles populated")

def populate_db_technologies():
  if is_table_empty(Technology.query.first(), 'technologies'):
    techs = requests.get('https://lit-citadel-12163.herokuapp.com/technologies/get_all_technologies')
    for tech_object in techs.json():
      Technology.seed(
        tech_object['name']
      )
    print("Technologies populated")

def populate_db_users():
  if is_table_empty(User.query.first(), 'users'):
    users = requests.get('https://randomuser.me/api?nat=br&results=10')
    roles_query = Role.query.filter_by(description = "HELPER").all()
    cities = City.query.order_by(City.name.asc()).all()
    cities_dict = cities_share_schema.dump(cities)
    for user in users.json()['results']:
      city_id = 2
      for city_object in cities_dict:
        if user['location']['city'] == city_object['name']:
          city_id = city_object['id']
      User.seed(
        city_id,
        user['name']['first'] + ' ' + user['name']['last'],
        user['registered']['age'],
        user['email'],
        "123Mudar!",
        roles_query
      )
    User.seed(
      1,
      'Luis Lopes',
      22,
      "luislopes@gmail.com",
      "123Mudar!",
      Role.query.filter_by(description = "OWNER").all()
    )
    print("Users populated")

def populate_db_developers():
  if is_table_empty(Developer.query.first(), 'developers'):

    users = User.query.order_by(User.name.asc()).all()
    users_dict = users_share_schema.dump(users)

    for index, user_object in enumerate(users_dict):
      if index % 2 == 0: # if para verificar se o index é par
        techs = Technology.query.order_by(func.random()).limit(10).all() # query que retorna aleatóriamente 10 tecnologias
        Developer.seed(
          1,
          3,
          index % 2 == 0,
          user_object['id'],
          techs
        )
    print("Developers populated")

def populate_db():
  populate_db_country()
  populate_db_state()
  populate_db_city()
  populate_db_permissions_and_roles()
  populate_db_technologies()
  populate_db_users()
  populate_db_developers()