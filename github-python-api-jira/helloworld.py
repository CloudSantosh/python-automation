from flask import Flask

#creating a flask app instance
app=Flask(__name__)

@app.route("/")
def hello():
    return "Hello This is my first flask Application"

if __name__=="__main__":
    app.run('0.0.0.0')