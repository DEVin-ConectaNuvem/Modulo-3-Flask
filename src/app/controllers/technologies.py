from flask import Blueprint, json
from flask.wrappers import Response
from src.app.services.technologies_service import get_technologies
from src.app.middlewares.auth import requires_access_level
technology = Blueprint('technology', __name__, url_prefix="/technologies")

@technology.route('/get_all_technologies', methods=['GET'])
@requires_access_level("READ")
def get_all_technologies():
  response = get_technologies()

  return Response(
    response=json.dumps(response),
    status=200,
    mimetype='application/json'
  )