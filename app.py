from flask import Flask

app = Flask(__name__)

from flask import request, render_template
import pickle


@app.route("/", methods = ["GET","POST"])
def index():
    if request.method == "POST":
        income = request.form.get("income")
        age = request.form.get("age")
        loan = request.form.get("loan")
        print(income, age, loan)
        model_DT = pickle.load(open("DecisionTreeModel", "rb"))
        model_LR = pickle.load(open("LogisticRegressionModel", "rb"))
        model_NN = pickle.load(open("NeuralNetworkModel","rb"))
        model_RF = pickle.load(open("RandomForestModel","rb"))
        model_XG = pickle.load(open("XGBoostModel","rb"))
        pred_DT = model_DT.predict([[float(income),float(age),float(loan)]])
        pred_LR = model_LR.predict([[float(income),float(age),float(loan)]])
        pred_NN = model_NN.predict([[float(income),float(age),float(loan)]])
        pred_RF = model_RF.predict([[float(income),float(age),float(loan)]])
        pred_XG = model_XG.predict([[float(income),float(age),float(loan)]])
        s = "[Decision Tree] The Predicted Default is : " + str(pred_DT)
        s1 = "[Logistic Regression] The Predicted Default is : " + str(pred_LR)
        s2 = "[Neural Network] The Predicted Default is : " + str(pred_NN)
        s3 = "[Random Forest] The Predicted Default is : " + str(pred_RF)
        s4 = "[XGBoost] The Predicted Default is : " + str(pred_XG)
        s5 = s + s1 + s2 + s3 + s4 
        return(render_template("index.html",result=s5))
    else:
        return(render_template("index.html",result="2"))
    
if __name__ == "__main__":
    app.run()
    
    
    
"""
        s = "[Decision Tree] The Predicted Default is : " + str(pred_DT)
        s1 = "[Logistic Regression] The Predicted Default is : " + str(pred_LR)
        s2 = "[Neural Network] The Predicted Default is : " + str(pred_NN)
        s3 = "[Random Forest] The Predicted Default is : " + str(pred_RF)
        s4 = "[XGBoost] The Predicted Default is : " + str(pred_XG)
        s5 = s + s1 + s2 + s3 + s4 
        
        """