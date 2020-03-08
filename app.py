from flask import Flask
import sys
sys.path.append("..")
# from flask_cors import CORS
from flask import request
# from flask_ngrok import run_with_ngrok
from src.Modules.prediction import prediction
from src.Modules.recommender import recommendation
import logging
from flask import render_template


# CORS(app)
# run_with_ngrok(app)
app = Flask(__name__)


@app.route('/ml/recommend', methods=['GET'])
# Main function for recommendation
def recommend():
    user_id = request.args.get('userid')
    recommend_model = recommendation(user_id)
    try:
        return recommend_model.recommend_with_existing_model()
    except Exception as err:
        logging.exception(err)


@app.route('/ml/predict', methods=['GET'])
def predict():
    userid = request.args.get('userid')
    predict_model = prediction(userid)
    try:
        return predict_model.predict()
    except Exception as err:
        logging.exception(err)

@app.route('/login', methods=["POST"])
def login():
    data=request.get_json()
    username=data["name"]
    password=data[" password"]

    logging.debug(data)
    return render_template("login.html")
# @app.route('/user/add',methods=['GET'])
# def add_to_list():
#     items=request.args.getlist('items')
#     logging.debug("mssg",items)
#     return (items[1])

@app.route('/')
def welcome():
    return "Welcome To Smart Flask List API"

if __name__ == '__main__':
    app.run(debug=True)

