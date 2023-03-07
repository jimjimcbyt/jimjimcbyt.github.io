from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/")
def index():
    keyword = None
    return render_template("Blox.html", keyword=keyword)
if __name__=="__main__":
    app.run(host="0.0.0.0", port="0987", debug=True)