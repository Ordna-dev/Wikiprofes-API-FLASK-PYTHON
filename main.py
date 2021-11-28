from flask import Flask

app = Flask(__name__)

exec(open('C:/Users/Administrator/Desktop/WikiProfes/Wikiprofes-2.0-master/Flask.py').read())

app.run(debug = True)