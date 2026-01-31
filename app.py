# app.py
import os

from flask import Flask, request, jsonify

app = Flask(__name__)

APP_NAME = os.environ.get("APP_NAME", "echo-flask")


@app.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
@app.route('/<path:path>', methods=['GET', 'POST'])
def all_routes(path):
    return jsonify({
        'app_name': APP_NAME,
        'host': request.host,
        'json': request.get_json(silent=True),
        'data': request.form,
        'query': request.args,
        'path': '/%s' % path,
        'method': request.method,
        'headers': dict(request.headers)
    })


if __name__ == '__main__':
    app.run(threaded=True, port=5000)
