from http.server import HTTPServer, CGIHTTPRequestHandler
from flask import Flask, render_template,url_for

app = Flask(__name__)


@app.route('/')
def training():
    return render_template('base.html', imag='/static/img/mars.png')
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')




