from functools import wraps
from jwt import decode
from flask import current_app, request, json
from flask.wrappers import Response

from src.app.models.user import User

def requires_access_level(permission):
  def jwt_required(function_current):
    @wraps(function_current)
    def wrapper(*args, **kwargs):

      token = None

      if "Authorization" in request.headers:
        token = request.headers["Authorization"]

      if not token:
        return Response(
          response=json.dumps({"error": "Você não tem permissão"}),
          status=403,
          mimetype='application/json'
        )

      if not "Bearer" in token:
        return Response(
          response=json.dumps({"error": "Você não tem permissão"}),
          status=401,
          mimetype='application/json'
        )

      try:
        token_pure = token.replace("Bearer ", "")
        decoded = decode(token_pure, current_app.config["SECRET_KEY"], "HS256")
        current_user = User.query.filter(User.id == decoded["user_id"]).first_or_404()

      except:
        return Response(
          response=json.dumps({"error": "O Token é inválido"}),
          status=403,
          mimetype='application/json'
        )

      found_permission = 0

      for role in current_user.roles:
        for permission_in_roles in role.permissions: 
          if permission_in_roles.description == permission:
            found_permission = found_permission + 1

      if found_permission == 0:
        return Response(
          response=json.dumps({"error": "Você não tem permissão para essa funcionalidade"}),
          status=403,
          mimetype='application/json'
        )

      return function_current(*args, **kwargs)
    return wrapper
  return jwt_required
