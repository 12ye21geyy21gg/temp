from http.server import HTTPServer, CGIHTTPRequestHandler
from flask import Flask, render_template,url_for

app = Flask(__name__)


@app.route('/')
def training():
    l = ['/static/img/1.jpg',
         '/static/img/2.jpg',
         '/static/img/3.jpg',
         '/static/img/4.jpg',
         '/static/img/5.jpg',
         '/static/img/6.jpg',]
    return render_template('base.html', l=l)
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')




