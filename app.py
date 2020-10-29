from flask import Flask, render_template, request
import json
import rouelette

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        tag = request.form.get("tag")
        course = rouelette.get_course(tag)
    else:
        tag = ""
        course = rouelette.get_course()
    tags = rouelette.tags()
    return render_template('index.html', course=course, tags=tags, tag=tag)
