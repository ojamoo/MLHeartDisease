import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'age': 40, 'Sex':1, 'ChestPainType':1, 'RestingBP':140, 'Cholesterol': 289, 'FastingBS':0, 'RestingECG':1, 'MaxHR':172, 'ExerciseAngina': 0, 'Oldpeak':0.0, 'ST_Slope':2})

print(r.json())


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