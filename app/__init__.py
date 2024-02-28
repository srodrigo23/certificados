from flask import Flask
from app.extensions import db
from config import config
# from app.extensions import migrate
import os

def create_app():
    
    app = Flask(__name__)
    # print(env_values['CONFIG_MODE'])
    # app.config.from_object(config[os.getenv("CONFIG_MODE")])
    # app.config['SQLALCHEMY_DATABASE_URI'] = env_values['DEVELOPMENT_DATABASE_URL']
    app.config.from_object(config[os.environ.get("CONFIG_MODE")])
    
    # Initialize Flask extensions here
    db.init_app(app)
    # migrate.init_app(app, db)

    #Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    # from app.posts import bp as posts_bp
    # app.register_blueprint(posts_bp, url_prefix='/posts')

    # from app.questions import bp as questions_bp
    # app.register_blueprint(questions_bp, url_prefix='/questions')

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app


