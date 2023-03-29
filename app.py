from flask import Flask
from config import DefCon
from models import *


app = None

def create_app():
    app = Flask(__name__)
    app.config.from_object(DefCon)
    db.init_app(app)
    app.app_context().push()
    return app

app = create_app()

from controllers import *

if __name__ == '__main__':
  # Run the Flask app
  app.run(host='0.0.0.0',debug=True)
