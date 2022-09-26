import json
from flask import Blueprint
from flask.wrappers import Response

from src.app.services.cities_service import get_cities_by_state
from src.app.middlewares.auth import requires_access_level

cities = Blueprint('cities', __name__, url_prefix="/cities")

@cities.route('/get_all_cities/<int:state_id>', methods = ["GET"])
@requires_access_level("READ")
def list_all_cities(state_id):

  response = get_cities_by_state(state_id)

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