from flask import Flask, jsonify, redirect, url_for, abort
from datetime import datetime
from uuid import uuid4

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

content = {}

@app.route("/")
def index():
  try:
    content[str(datetime.now())] = str(uuid4())
    response = dict(reversed(list(content.items())))
    return jsonify(response)
  except:
    return abort(422, 'cannot process request')


@app.errorhandler(404)
def catch_all(e):
    print(e)
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run()