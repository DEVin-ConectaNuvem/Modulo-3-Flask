from src.app.models.developer import Developer
from src.app.models.technology import Technology
from sqlalchemy.sql.expression import func

def test_new_developer():
  developer = Developer.seed(
      1,
      3,
      True,
      2,
      Technology.query.order_by(func.random()).limit(10).all()
  )

  assert developer.user_id == 2
  assert developer.minimum_experience_time == 1
  assert developer.maximum_experience_time == 3
  assert developer.accepted_remote_work == True
  assert len(developer.technologies) >= 1


