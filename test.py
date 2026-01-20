from flask import Flask

app=Flask(__name__)
@app.route('/')
def index():
    return "Thanks for watching!"

app.run(debug=True)
