from src.app.models.developer import Developer, developers_share_schema, DeveloperSchema
from src.app.models.user import User

def list_all_developers_service():

  list_developers = Developer.query.all()
  list_developers_dict = developers_share_schema.dump(list_developers)

  return {"records": list_developers_dict, "status_code": 200}

def search_developers_service(options): 

  try:
    list_developers = Developer.query
    
    if len(options) == 0:
        list_developers = list_developers.all()
        list_developers_dict = developers_share_schema.dump(list_developers)

        return { "records": list_developers_dict, "status_code": 200 }

    if "city_id" in options:
      if not options['city_id'].isdigit():
        return { "error": "City_id não é um número", "status_code": 422 }

      list_developers = list_developers.filter(Developer.user_id == User.id)
      list_developers = list_developers.filter(User.city_id == options['city_id'])

    if "min_exp" and "max_exp" in options:
      if not options['min_exp'].isdigit() or not options['max_exp'].isdigit():
        return { "error": "Algum dos valores enviados não é um número", "status_code": 422 }
      
      list_developers = list_developers.filter(Developer.minimum_experience_time >= options['min_exp'])
      list_developers = list_developers.filter(Developer.maximum_experience_time <= options['max_exp'])
    
    if "accepted_remote_work" in options:
      if not options["accepted_remote_work"].isdigit():
        return { "error": "accepted_remote_work não é um booleano", "status_code": 422 }
      if int(options["accepted_remote_work"]) < 0 or int(options["accepted_remote_work"]) > 1:
        return { "error": "accepted_remote_work não é um booleano", "status_code": 422 }

      list_developers = list_developers.filter_by(accepted_remote_work = options['accepted_remote_work'])

    list_developers = list_developers
    list_developers_schema = DeveloperSchema(many = True, only=(
      "id",
      "user.name",
      "accepted_remote_work", 
      "minimum_experience_time",
      "maximum_experience_time", 
      "technologies.name"
      )
    )
    list_developers_dict = list_developers_schema.dump(list_developers)
    return { "records": list_developers_dict, "status_code": 200 }
  
  except Exception as error:
    return { "error": str(error), "status_code": 500 }

