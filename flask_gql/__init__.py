from flask import Flask
from flask_graphql import GraphQLView

app = Flask()

from . import models, views, schema

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True  # for having the GraphiQL interface
    )
)



@app.teardown_appcontext
def shutdown_session(exception=None):
    models.db.remove()



if __name__ == '__main__':
    app.run(debug=True)
