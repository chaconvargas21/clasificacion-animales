from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():
    return render_template("menu.html")

@app.route("/predictor",methods=["POST"])
def predictor():
    return render_template("predictor.html")

@app.route("/clasificador",methods=["POST"])
def clasificador():
    return render_template("")

if __name__ == "__main__" :
    app.run(debug=True)