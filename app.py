from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, world!"

if __name__ == "__main__":
    # listen on all interfaces so container exposes it
    app.run(host="0.0.0.0", port=5000)
