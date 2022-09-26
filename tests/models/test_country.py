from src.app.models.country import Country

def test_new_country():
  country = Country.seed(
      'Canada',
      "English"
  )

  assert country.language == "English"
  assert country.name == 'Canada'
  

