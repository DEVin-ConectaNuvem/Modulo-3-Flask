from src.app.models.role import Role
from src.app.models.permission import Permission
from sqlalchemy.sql.expression import func

def test_new_role():
  role = Role.seed(
      'OPERATOR',
       Permission.query.order_by(func.random()).limit(3).all()
  )

  assert role.description == 'OPERATOR'
  assert len(role.permissions) >= 1


