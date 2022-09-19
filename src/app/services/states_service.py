from src.app.models.state import State, states_share_schema

def get_states_by_country(country_id):
  try:
    states_query = State.query.filter(State.country_id == country_id).order_by(State.name).all()
    states_info = states_share_schema.dump(states_query)

    return { "records": states_info, "status_code": 200 }

  except Exception as e:
    return { "error": str(e), "status_code": 500 }
