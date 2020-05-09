from http.server import HTTPServer, CGIHTTPRequestHandler
from flask import Flask, render_template,url_for

app = Flask(__name__)


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def training(nickname,level,rating):
    return render_template('base.html', nickname=nickname,level=level,rating=rating)
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')




