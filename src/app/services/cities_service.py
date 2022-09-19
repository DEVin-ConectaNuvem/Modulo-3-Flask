from src.app.models.city import City, cities_share_schema

def get_cities_by_state(state_id):
  try:
    cities_query = City.query.filter(City.state_id == state_id).order_by(City.name).all()
    cities_info = cities_share_schema.dump(cities_query)

    return { "records": cities_info, "status_code": 200 }

  except Exception as e:
    return { "error": str(e), "status_code": 500 }