from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def get_sp500_prediction(): 
    temp_sp500_prediction = {
        "date": "01/06/2023",
        "curr_date": "3,895.08",
        "pred_date": "01/09/2023",
        "pred_price":"3950.03"
        "prob"
    }
    response = jsonify(temp_sp500_prediction)
    return response

if __name__ == '__main__':
    app.run()
