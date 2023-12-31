from flask import Flask, request, jsonify, render_template
import numpy as np
import pickle
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import euclidean_distances

app = Flask(__name__)

model = pickle.load(open('desired-model-file-name.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))


@app.route('/')  #This is the route to display the home page
def home():
	return render_template("home.html",static_url_path='\static')

@app.route('/predict',methods=["POST"]) #This is the route to show the predictions
def predict():
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    final_features = scaler.transform(final_features)    
    prediction = model.predict(final_features)
    print("final features",final_features)
    print("prediction:",prediction)
    output = round(prediction[0], 2)
    print(output)

    if output == 0:
        return render_template('home.html', prediction_text='PATIENT IS NOT LIKELY TO HAVE A HEART DISEASE')
    else:
         return render_template('home.html', prediction_text='PATIENT IS LIKELY TO HAVE A HEART DISEASE')
        
@app.route('/predict_api',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)








    #try:
           #reading the inputs given by the user
           #Age = float(request.form["Age"])
           #Sex = float(request.form["Sex"])
           #ChestPainType = float(request.form["ChestPainType"])
           #RestingBP = float(request.form["RestingBP"])
           #Cholesterol = float(request.form["Cholesterol"])
           #FastingBS = float(request.form["FastingBS"])
           #RestingECG = float(request.form["RestingECG"])
           #MaxHR = float(request.form["MaxHR"])
           #ExerciseAngina = float(request.form["ExerciseAngina"])
           #Oldpeak = float(request.form["Oldpeak"])
           #ST_Slope = float(request.form["ST_Slope"])
    
    #inputList = [Age,Sex,ChestPainType,RestingBP,Cholesterol,FastingBS,RestingECG,MaxHR,ExerciseAngina,Oldpeak,ST_Slope]
    
    # load df_cols list
    #with open("df_cols.pkl", 'rb') as file:
            #pickle_df_cols = pickle.load(file)
            #file.close()

    # load model
	#with open("desired-model-file-name.pkl", 'rb') as file:
				#loaded_model = pickle.load(file)
				#file.close()
