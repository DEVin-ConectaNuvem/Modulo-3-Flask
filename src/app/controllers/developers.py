import json
from flask import Blueprint, request
from flask.wrappers import Response

from src.app.services.developers_service import list_all_developers_service, search_developers_service
from src.app.middlewares.auth import requires_access_level

developers = Blueprint('developers', __name__, url_prefix="/developers")

@developers.route('/', methods = ["GET"])
@requires_access_level("READ")
def list_all_developers():

  response = list_all_developers_service()
  return Response(
    response=json.dumps(response),
    status=response['status_code'],
    mimetype='application/json'
  )

@developers.route('/search_developers', methods = ["GET"])
@requires_access_level("READ")
def search_developers():
  options = request.args.to_dict()
  response = search_developers_service(options)

  if "error" in response:
    return Response(
      response=json.dumps(response),
      status=response['status_code'],
      mimetype='application/json'
    )

  return Response(
    response=json.dumps(response),
    status=response['status_code'],
    mimetype='application/json'
  )
