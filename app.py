from flask import Flask
from src.model import Model

app = Flask(__name__)

# At beginning, we load model from MLflow
model = Model()

@app.route('/', methods=['GET'])
def home():
    return "OK !", 200

if __name__ == "__main__":
    app.run(port=5000)