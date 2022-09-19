import json
from flask import Blueprint
from flask.wrappers import Response

from src.app.models.country import Country, countries_share_schema
from src.app.middlewares.auth import requires_access_level
countries = Blueprint('countries', __name__, url_prefix="/countries")

@countries.route('/get_all_countries', methods = ["GET"])
@requires_access_level("READ")
def get_all_countries():

  countries_query = Country.query.order_by(Country.name).all()
  countries_info = countries_share_schema.dump(countries_query)

  return Response(
      response=json.dumps(countries_info),
      status=200,
      mimetype='application/json'
  )