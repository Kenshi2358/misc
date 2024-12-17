import os
from flask import Flask, render_template

current_file_path = os.path.abspath(__file__)
root_dir = os.path.dirname(current_file_path)

# app = Flask(__name__)
app = Flask(__name__, template_folder="/Users/shahnert/Desktop/Repos/misc/flask/proj1/templates")
app.config["EXPLAIN_TEMPLATE_LOADING"] = True

@app.route("/")
def index():
    return render_template("index.html")

print(root_dir)

if __name__ == '__main__':
    app.run(debug=True)
