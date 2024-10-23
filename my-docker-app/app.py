from flask import Flask
app = Flask(name)

@app.route('/')
def hello():
 return "Hello, Docker with Flask!"

if name == "main":
 app.run(host="0.0.0.0", port = 5000)