from src.app.models.technology import Technology

def test_new_technology():
  technology = Technology.seed(
      'Mobx'
  )

  assert technology.name == 'Mobx'
  

