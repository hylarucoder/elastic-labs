from flask import Flask
from elasticapm.contrib.flask import ElasticAPM

app = Flask(__name__)

app.config["ELASTIC_APM"] = {
    "SERVICE_NAME": "dev-flask",
    'SECRET_TOKEN': '',
}
apm = ElasticAPM(app)


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/home")
def home():
    return "home!"


@app.route("/<int:num>")
def hello_num(num):
    import random
    if random.randint(1, 100) > 95:
        raise Exception(f"num")
    return f"Hello, {num}!"
