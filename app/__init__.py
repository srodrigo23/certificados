from flask import Flask, url_for, send_from_directory
from app.extensions import db
from config import config
from app.extensions import migrate

import os

from app.models import user

def create_app():
    
    app = Flask(__name__)
    app.config.from_object(config[os.environ.get("CONFIG_MODE")])
    
    # Initialize Flask extensions here

    with app.app_context():
        db.init_app(app)
        db.create_all()

        migrate.init_app(app, db)
        
        #Register blueprints here
        from app.main import bp as main_bp
        app.register_blueprint(blueprint=main_bp)

        from app.certificates import bp as certificates_bp
        app.register_blueprint(blueprint=certificates_bp, url_prefix="/certificates")
        
        from app.users import bp as users_bp
        app.register_blueprint(blueprint=users_bp, url_prefix="/users")

        @app.route('/favicon.ico')
        def favicon():
            return send_from_directory(
                directory=os.path.join(app.root_path, 'static'),
                path='static/favicon.ico', 
                mimetype='image/vnd.microsoft.icon'
            )

        @app.route('/test/')
        def test_page():
            return '<h1>Testing the Flask Application Factory Pattern</h1>'
        return app
