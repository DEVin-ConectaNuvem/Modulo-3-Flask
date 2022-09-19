import os
import click

from flask.cli import with_appcontext

from src.app import create_app, DB
from src.app.routes import routes
from src.app.db import populate_db

app = create_app(os.getenv('FLASK_ENV'))
routes(app)

@click.command(name='populate_db')
@with_appcontext 
def call_command():
  populate_db()

@click.command(name='delete_tables') 
@with_appcontext 
def delete_tables():
  DB.drop_all()

app.cli.add_command(call_command)
app.cli.add_command(delete_tables)

if __name__ == "__main__":
  app.run(port=int(os.environ.get("PORT", 5000)), host='0.0.0.0',debug=False)