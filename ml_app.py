# Core Packages 
import streamlit as st
from streamlit.state.session_state import SessionState

# Additional packages 
import numpy as np
import joblib
import os

label_dict = {"No":0,"Yes":1}

target_label_map = {"Negative":0,"Positive":1}

# Encoding Functions
def get_feature_value(val):
	feature_dict = {"No":0,"Yes":1}
	for key,value in feature_dict.items():
		if val == key:
			return value 

def get_gender_value(val,my_dict):
	for key,value in my_dict.items():
		if val == key:
			return value 



# Load ML Models
@st.cache
def load_model(model_file):
	loaded_model = joblib.load(open(os.path.join(model_file),"rb"))
	return loaded_model


def ml_main():
	
	if 'flag' not in st.session_state:
			st.session_state.flag = 0 
	# Layout
	with st.form(key='Main'):
		col1,col2 = st.beta_columns(2)

		with col1:
			age = st.number_input("Age",10,100)
			gender = st.radio("Gender",("Female","Male"))
			polyuria = st.radio("Polyuria(Excessive urination)",["No","Yes"])
			polydipsia = st.radio("Polydipsia(Excess thirst)",["No","Yes"]) 
			sudden_weight_loss = st.selectbox("Sudden_weight_loss",["No","Yes"])
			weakness = st.radio("Weakness",["No","Yes"]) 
			polyphagia = st.radio("Polyphagia(Excessive hunger or increased appetite)",["No","Yes"]) 
			genital_thrush = st.selectbox("Genital_thrush",["No","Yes"]) 


		with col2:
			visual_blurring = st.selectbox("Visual_blurring",["No","Yes"])
			itching = st.radio("Itching",["No","Yes"]) 
			irritability = st.radio("Irritability",["No","Yes"]) 
			delayed_healing = st.radio("Delayed_healing",["No","Yes"]) 
			partial_paresis = st.selectbox("Partial_paresis",["No","Yes"])
			muscle_stiffness = st.radio("Muscle_stiffness",["No","Yes"]) 
			alopecia = st.radio("Alopecia(Hair Loss)",["No","Yes"]) 
			obesity = st.selectbox("Obesity",["No","Yes"])
		

		b1 = st.form_submit_button('Continue')
		if b1:
			st.session_state.flag = 1
			


	
	if st.session_state.flag == 1:
		with st.beta_expander("Your Selected Options"):
			result = {
			'age':age,
			'gender':gender,
			'polyuria':polyuria,
			'polydipsia':polydipsia,
			'sudden_weight_loss':sudden_weight_loss,
			'weakness':weakness,
			'polyphagia':polyphagia,
			'genital_thrush':genital_thrush,
			'visual_blurring':visual_blurring,
			'itching':itching,
			'irritability':irritability,
			'delayed_healing':delayed_healing,
			'partial_paresis':partial_paresis,
			'muscle_stiffness':muscle_stiffness,
			'alopecia':alopecia,
			'obesity':obesity
			}

			for key, value in result.items():
				output = '{} - {}'.format(key, value)
				st.text(output)	
		b2 = st.button('Confirm & Predict')
		if b2:
			st.session_state.flag = 2
		
		if st.session_state.flag == 2:
			encoded_result = []
			for i in result.values():
				if type(i) == int:
					encoded_result.append(i)
				elif i in ["Female","Male"]:
					gender_map = {"Female":0,"Male":1}
					res = get_gender_value(i,gender_map)
					encoded_result.append(res)
				else:
					encoded_result.append(get_feature_value(i))

			with st.beta_expander("Prediction Result"):
				single_sample = np.array(encoded_result).reshape(1,-1)

				# Loadign the Logistic Regression Model

				model = load_model("models/logistic_regression_model_diabetes.pkl")

				prediction = model.predict(single_sample)
				prediction_prob = model.predict_proba(single_sample)

				if prediction == 1:
					pred_output = "You have {}% chance of attaining Early Stage Diabetes".format(round(prediction_prob[0][1]*100,2))
					st.error(pred_output)
				else:
					pred_output = 'You are healthy! You are {}% safe'.format(round(prediction_prob[0][0]*100,2))
					st.success(pred_output)
				
			
			
			