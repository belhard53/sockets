from flask import Flask


app = Flask(__name__)


@app.route('/', )
def index():
    return ('Hello PYthon')

@app.route('/cats/', methods = ['POST', 'GET'])
def cats():    
    return ('Hello from cats ls;kd;sldk')

@app.route('/cat/<int:id>')
def cat(id):
    return (f'Hello from cat with number {id}')



@app.route('/cat/<id>')
def cat_err(id):
    return (f'BAD ID')


@app.errorhandler(404)
def page_not_found(error):
    return "Нет такой странички"


app.run(debug =True)






    
