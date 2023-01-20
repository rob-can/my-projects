from flask import Flask 

app = Flask(__name__)


@app.route("/")  #decorator
def head():
    return "<h1>Hello World from Flask!</h1>"

@app.route("/marina")  
def second():
    return "<h1>This is my second page</h1>"


@app.route("/third/subthird")
def third():
    return "<h2>This is the subpath of third page</h2>"


@app.route("/forth/<string:id>")  #dinamik değer çekiyor
def forth(id):
    return f'Id of this page is {id}'



if __name__ == "__main__":
    app.run(debug=True) #port default olarak 5000 de çalışır. browser da localhost:5000 yaz ve gör
    # app.run(debug=True, port=3000)
    # debug=True demek, hatalı kod yazıldığında bize hata detayını, debug hata ayıklama demektir
    