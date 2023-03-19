from typing import Union

from flask import Flask, Blueprint
from view.api import app2
from config import Config
 
app = Flask(__name__)
app.register_blueprint(app2, url_prefix='/pages')
#http://127.0.0.1:5000/pages/app2
app.config.from_object(Config)

@app.route('/')
def index():
        return "Hello index"
 


if __name__ == '__main__':
    
    app.run(debug=True, host='0.0.0.0',port=8080)

