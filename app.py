from flask import Flask,jsonify,render_template,request
import joblib
import os
import numpy as np


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/predict',methods=['POST','GET'])
def predict():
    item_weight = float(request.form['item_weight'])
    item_visibility = float(request.form['item_visibility'])
    item_type = float(request.form['item_type'])
    item_mrp = float(request.form['item_mrp'])
    outlet_location_type = float(request.form['outlet_location_type'])
    outlet_type = float(request.form['outlet_type'])
    item_fat_content=float(request.form['item_fat_content'])
    outlet_establishment_year=float(request.form['outlet_establishment_year'])
    outlet_size=float(request.form['outlet_size'])


    x=np.array([[item_weight,item_fat_content,item_visibility,item_type,item_mrp,outlet_establishment_year,outlet_size,outlet_location_type,outlet_type]])
    scaler_path=r'X:\Aiml project\modules\sc.sav'
    sc=joblib.load(scaler_path)


    x_std=sc.transform(x)

    model_path=r"X:\Aiml project\modules\random_forest_grid.sav"
    model=joblib.load(model_path)
    model_prediction=model.predict(x_std)
    Y_prediction=model_prediction[0]
    return jsonify({'prediction':float(Y_prediction)})





if __name__=='__main__':
    app.run(debug=True,port=4892)

