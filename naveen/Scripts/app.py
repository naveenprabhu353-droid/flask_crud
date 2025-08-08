from flask import Flask
app=flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<hl>hai</h2>"

if __name__="__main__":
    app.run(debug=true)
