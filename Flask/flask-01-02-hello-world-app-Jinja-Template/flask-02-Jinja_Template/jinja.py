from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def head():
    return render_template("index.html", number1=100, number2=30)


@app.route("/marina/aa")
def number():
    # num1 = 12
    # num2 = 28
    #var1, var2 = 23, 54 şeklinde yazabiliriz
    return render_template("body.html", value1=12, value2=28, sum=12+28)



if __name__== "__main__":
    app.run(debug=True)