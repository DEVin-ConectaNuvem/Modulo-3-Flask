from src.app.models.permission import Permission

def test_new_permission():
  permission = Permission.seed(
      'ADMIN'
  )

  assert permission.description == 'ADMIN'
  

