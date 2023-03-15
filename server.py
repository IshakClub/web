from flask import Flask, render_template, redirect, jsonify
from flask_login import LoginManager, UserMixin, login_user
from flask_restful import reqparse, abort, Api, Resource

from data import db_session, news_api, jobs_api

from flask import make_response
from data import users_resource

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


# для списка объектов
api.add_resource(users_resource.UsersListResource, '/api/v2/users')

# для одного объекта
api.add_resource(users_resource.UsersResource, '/api/v2/users/<int:users_id>')


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(400)
def bad_request(_):
    return make_response(jsonify({'error': 'Bad Request'}), 400)


def main():
    db_session.global_init("db/blogs.db")
    app.register_blueprint(news_api.blueprint)
    app.register_blueprint(jobs_api.blueprint)
    app.run()


if __name__ == '__main__':
    main()
