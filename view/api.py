
from flask import Blueprint
 
app2 = Blueprint('app2', __name__, static_folder='static',template_folder='templates')
#根據不同的功能切分

@app2.route('/app2')
def show():
        return "Hello Blueprint app2"