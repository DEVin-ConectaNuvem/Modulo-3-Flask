from src.app.models.technology import Technology, technologies_share_schema

def get_technologies():
  try:
    technologies_query = Technology.query.order_by(Technology.name).all()
    technologies = technologies_share_schema.dump(technologies_query)

    return { "records": technologies, "status_code": 200 }

  except Exception as e:
    return { "error": str(e), "status_code": 500 }
