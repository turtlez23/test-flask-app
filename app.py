from flask import Flask

app = Flask(__name__)


app.secret_key = 'adadasdsad'


@app.route("/")
def index():
  return 'Test flask app'

if '__main__' == '__main__':
  app.run(debug=True, port=5000)