# app.py
from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
@app.route('/<path:path>', methods=['GET', 'POST'])
def all_routes(path):
    return jsonify({
        'json': request.get_json(silent=True),
        'data': request.form,
        'query': request.args,
        'path': '/%s' % path,
        'method': request.method,
        'headers': dict(request.headers)
    })


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
