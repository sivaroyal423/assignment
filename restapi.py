import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {'id': 0,
      'chemicals': ['Amazon', 'Microsoft', 'Google'],
      'symbols': ['I', 'Am', 'cro', 'Na', 'le', 'abc']} ,

      {'id':1,
       
      'result': ['Amazon', 'Microsoft'  ,'Google'],
            }]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>assignment</h1>
<p>A prototype API .</p>'''


@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)


@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():

   
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    results = []

    for book in books:
        if book['id'] == id:
            results.append(book)
    return jsonify(results)
        

app.run()