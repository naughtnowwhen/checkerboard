from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
@app.route('/<x>')
@app.route('/<x>/<y>')
@app.route('/<x>/<y>/<colorA>/<colorB>')
def index(x='8', y='8', colorA = 'red', colorB = 'blue'):
    return render_template("index.html", x=int(x), y=int(y), colorA=colorA, colorB=colorB)


if __name__ == "__main__":
    app.run(debug=True)
