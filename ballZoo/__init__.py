# config                    
from flask import Flask
from flask_migrate import Migrate

# factory
def create_app():
    app = Flask(__name__)
    
    # database config
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:2J1bzy9489@localhost:5432/ballpy'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False     

    # index route
    @app.route('/')
    def index(): 
        return 'Hello, this is Ballpy'        
    
    # Do i need this ---------------------------?
    from . import models 
    models.db.init_app(app) 
    migrate = Migrate(app, models.db)
    
    # register pet blueprint 
    from . import reptile 
    app.register_blueprint(reptile.bp)

    # register fact blueprint 
    from . import fact
    app.register_blueprint(fact.bp)

    # return the app 
    return app