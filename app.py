from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/",methods=["get","post"])
def index():
    return(render_template("index.html"))

if __name__ == "__main__":
    app.run()

@app.route("/main",methods=["GET","POST"])
def main():
    q = request.form.get("q")
    print(q)
    return(render_template("main.html"))
    