from flask import Flask
import random
app = Flask(__name__)

@app.route("/")
def randomnum():
    return f'you got{random.randint(1,100)}'

app.run(debug=True)

