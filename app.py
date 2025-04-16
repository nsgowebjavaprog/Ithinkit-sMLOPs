from flask import Flask, render_template, jsonify

from src.pipeline.prediction_pipeline import PredictPipeline, CustomData

app = Flask(__name__)

@app.route('/')  # home page

def home_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port=8000)
