from src.app import DB, MA
from src.app.models.user import user_share_schema

class Technology(DB.Model):
  __tablename__ = 'technologies'
  id = DB.Column(DB.Integer, autoincrement=True, primary_key=True)
  name = DB.Column(DB.String(84), nullable=False)

  def __init__(self, name):
    self.name = name

  @classmethod
  def seed(cls, name):
    tech = Technology(
      name = name
    )
    tech.save()
    return tech
    
  def save(self):
    DB.session.add(self)
    DB.session.commit()

class DeveloperSchema(MA.Schema):
  user = MA.Nested(user_share_schema)
  class Meta:
    fields = ('id', 'months_experience', 'accepted_remote_work', 'user_id', 'user')

developer_share_schema = DeveloperSchema()
developers_share_schema = DeveloperSchema(many = True)

class TechnologySchema(MA.Schema):
  developers = MA.Nested(developers_share_schema)
  class Meta:
    fields = ('id', 'name', 'developers')
    
technology_share_schema = TechnologySchema()
technologies_share_schema = TechnologySchema(many=True)