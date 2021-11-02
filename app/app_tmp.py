from flask import Flask, render_template, request
import os

app = Flask(__name__)
rootDir = os.path.dirname(__file__)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', **locals()), 404


def getParam(name, defoultValue=''):
    return request.args.get(name, defoultValue)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<path:the_path>', methods=['GET', 'POST'])
def all_other_routes(the_path):
    return "htmlContent", 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
