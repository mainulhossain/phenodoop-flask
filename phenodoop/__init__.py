from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Oh My God! This is a test."
if __name__ == "__main__":
    app.run()
