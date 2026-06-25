from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dogs")
def dogs():
    return render_template("dogs.html")

@app.route("/cats")
def cats():
    return render_template("cats.html")

if __name__ == "__main__":
<<<<<<< HEAD
    app.run(debug=True)		
=======
    app.run(host="0.0.0.0", port=5000, debug=True) 
>>>>>>> aacebcd47996176c62afcd046af667e27431a8a9
