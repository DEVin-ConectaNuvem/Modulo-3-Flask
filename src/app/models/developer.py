from src.app import DB, MA
from src.app.models.user import User, user_share_schema
from src.app.models.technology import TechnologySchema

developer_technologies = DB.Table('developer_technologies',
                    DB.Column('developer_id', DB.Integer, DB.ForeignKey('developers.id')),
                    DB.Column('technology_id', DB.Integer, DB.ForeignKey('technologies.id'))
                    )

class Developer(DB.Model):
  __tablename__ = "developers"
  id = DB.Column(DB.Integer, autoincrement=True, primary_key=True)
  minimum_experience_time = DB.Column(DB.Integer, nullable=False)
  maximum_experience_time = DB.Column(DB.Integer, nullable=False)
  accepted_remote_work = DB.Column(DB.Boolean, nullable = False, default = True)
  user_id = DB.Column(DB.Integer, DB.ForeignKey(User.id), nullable = False)
  technologies = DB.relationship('Technology', secondary=developer_technologies, backref='developers')
  user = DB.relationship("User", foreign_keys=[user_id])

  def __init__(self, minimum_experience_time, maximum_experience_time, accepted_remote_work, user_id, technologies):
    self.minimum_experience_time = minimum_experience_time
    self.maximum_experience_time = maximum_experience_time
    self.accepted_remote_work = accepted_remote_work
    self.user_id = user_id
    self.technologies = technologies

  @classmethod
  def seed(cls, minimum_experience_time, maximum_experience_time, accepted_remote_work, user_id, technologies):
    developer = Developer(
      minimum_experience_time = minimum_experience_time,
      maximum_experience_time = maximum_experience_time,
      accepted_remote_work = accepted_remote_work,
      user_id = user_id,
      technologies = technologies
    )
    developer.save()
    return developer
    
  def save(self):
    DB.session.add(self)
    DB.session.commit()

class DeveloperSchema(MA.Schema):
  technologies = MA.Nested(TechnologySchema, many=True)
  user = MA.Nested(user_share_schema)
  class Meta:
    fields = ('id', 'minimum_experience_time', 'maximum_experience_time', 'accepted_remote_work', 'user_id', 'technologies', 'user')

developer_share_schema = DeveloperSchema()
developers_share_schema = DeveloperSchema(many = True)

