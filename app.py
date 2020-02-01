from flask import Flask
from flask_mongoengine import MongoEngine
from flask_mongorest import MongoRest
from flask_mongorest.views import ResourceView
from flask_mongorest.resources import Resource
from flask_mongorest import operators as ops
from flask_mongorest import methods
import settings

app = Flask(__name__)

app.config.update(
    MONGODB_HOST = settings.MONGODB_HOST,
    MONGODB_PORT = settings.MONGODB_PORT,
    MONGODB_DB = settings.MONGODB_DB,
    TESTING = settings.TESTING,
    SECRET_KEY=settings.SECRET_KEY
)

db = MongoEngine(app)
api = MongoRest(app)

class Content(db.EmbeddedDocument):
    text = db.StringField()

class ContentResource(Resource):
    document = Content

class Logs(db.Document):
    source = db.StringField(max_length=120, required=True)
    logs = db.StringField(required=True)

class PostResource(Resource):
    document = Logs
    related_resources = {
        'content': ContentResource,
    }
    filters = {
        'source': [ops.Exact, ops.Startswith],
        'logs': [ops.Exact, ops.Contains, ops.Startswith],
    }


@api.register(name='addlog', url='/addlog/')
class PostView(ResourceView):
    '''
        add log accepts POST method content type application/json
        required field in request body: source and log 
        limitations: source max_length limited to 120 chars
    '''
    resource = PostResource
    methods = [methods.Create, ]

@api.register(name='logs', url='/logs/')
class GetView(ResourceView):
    '''
        add log accepts POST method content type application/json
        optional path parameter for accessing object in url: id
    '''
    resource = PostResource
    methods = [ methods.Fetch, methods.List]

@api.register(name='deletelog', url='/deletelog/')
class DelteteView(ResourceView):
    '''
        delete log accepts POST method content type application/json
        optional path parameter for accessing object in url: id
    '''
    resource = PostResource
    methods = [ methods.Delete] 


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)