from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def head():
    return render_template("index.html", number1=34, number2=45)

@app.route("/robert")
def number():
    num1 = 23
    num2 = 54
    #var1, var2 = 23, 54 şeklinde yazabiliriz
    return render_template("body.html", value1=num1, value2=num2, sum=num1+num2)



if __name__== "__main__":
    app.run(debug=True)