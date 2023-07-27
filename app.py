import os
from flask import Flask
from flask import jsonify
from application.config import LocalDevelopmentConfig, ProductionConfig
from models.model import Todos, User, Role
from application.database import db, db_con_string
from flask_security import Security, SQLAlchemyUserDatastore
from flask_migrate import Migrate
from resetdb import resetdb_command

app = None

def create_app():
    app = Flask(__name__, template_folder='templates')
    if os.getenv('ENV', "development") == "production":
        print("++///---------Staring Production Development----------///++".upper())
        app.config.from_object(ProductionConfig)
    else:
        print("++///---------Staring Local Development----------///++".upper())
        app.config.from_object(LocalDevelopmentConfig)
    db.init_app(app)
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    app.security = Security(app, user_datastore)
    migrate = Migrate(app, db)
    app.app_context().push()
    return app


app = create_app()

@app.route("/test")
def test():
    return jsonify({"Hello": "World!"})


from controllers.main import *

if __name__ == "__main__":
    if os.getenv("ENV") == 'production':
        db_status = resetdb_command()
        if db_status:
            print("**************PostgreSQL DB connected successfully.**************")
            app.run()
        else:
            raise Exception("DB ERROR!!!!!!!!!!")
    else:
        app.run(debug=True)