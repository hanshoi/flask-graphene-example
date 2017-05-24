from flask import Flask
from flask_graphql import GraphQLView

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = "super-secret"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.sqlite3"

from . import models, schema

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema.schema,
        graphiql=True  # for having the GraphiQL interface
    )
)
