from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route("/data")
def get_data():
    df = pd.read_csv("../data/stock_data.csv")
    return jsonify(df.tail(50).to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)
