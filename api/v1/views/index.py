#!/usr/bin/python3
'''Contains a Flask web application API.
'''
import os
from flask import Flask, jsonify
from flask_cors import CORS

from models import storage
from api.v1.views import app_views


app = Flask(__name__)
'''The Flask web application instance.'''
app_host = os.getenv('HBNB_API_HOST', '0.0.0.0')
app_port = int(os.getenv('HBNB_API_PORT', '5000'))
app.url_map.strict_slashes = False
app.register_blueprint(app_views)
CORS(app, resources={'/*': {'origins': app_host}})
root@7853b1fe5fcb:/AirBnB_clone_v3/api/v1# ls
__init__.py  app.py  views
root@7853b1fe5fcb:/AirBnB_clone_v3/api/v1# cd views
root@7853b1fe5fcb:/AirBnB_clone_v3/api/v1/views# ls
__init__.py  index.py
root@7853b1fe5fcb:/AirBnB_clone_v3/api/v1/views# vi index.py
root@7853b1fe5fcb:/AirBnB_clone_v3/api/v1/views# vi __init__.py
root@7853b1fe5fcb:/AirBnB_clone_v3/api/v1/views# cat index.py
#!/usr/bin/python3
'''Contains the index view for the API.'''
from flask import jsonify

from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route('/status')
def get_status():
    '''Gets the status of the API.
    '''
    return jsonify(status='OK')


@app_views.route('/stats')
def get_stats():
    '''Gets the number of objects for each type.
    '''
    objects = {
        'amenities': Amenity,
        'cities': City,
        'places': Place,
        'reviews': Review,
        'states': State,
        'users': User
    }
    for key, value in objects.items():
        objects[key] = storage.count(value)
    return jsonify(objects)

