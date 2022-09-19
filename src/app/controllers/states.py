import json
from flask import Blueprint
from flask.wrappers import Response

from src.app.services.states_service import get_states_by_country
from src.app.middlewares.auth import requires_access_level
states = Blueprint('states', __name__, url_prefix="/states")

@states.route('/get_all_states/<country_id>', methods = ["GET"])
@requires_access_level("READ")
def get_all_states(country_id):
  response = get_states_by_country(country_id)

  if "error" in response:
    return Response(
      response=json.dumps({"error": response['error']}),
      status=response['status_code'],
      mimetype='application/json'
    )

  return Response(
      response=json.dumps({"records": response["records"]}),
      status=response["status_code"],
      mimetype='application/json'
  )