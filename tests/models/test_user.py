from src.app.models.user import User
from src.app.models.role import Role

def test_new_user():
  user = User.seed(
      1,
      'Luis Lopes',
      22,
      "luislopes2@gmail.com",
      "123Mudar!",
      Role.query.filter_by(description = "OWNER").all()
  )

  assert user.city_id == 1
  assert user.name == 'Luis Lopes'
  assert user.age == 22
  assert user.email == "luislopes2@gmail.com"
  assert user.password != "123Mudar!"
  assert user.roles[0].description == "OWNER"

