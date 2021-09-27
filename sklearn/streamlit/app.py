import streamlit as st
import numpy as np
import joblib
import sklearn

model = joblib.load('./save/model.joblib')

st.title("Iris flower species classification")
st.sidebar.title("Features")

parameter_list = [
    'Sepal length (cm)',
    'Sepal Width (cm)',
    'Petal length (cm)',
    'Petal Width (cm)']

parameter_input_values = []
parameter_default_values = ['5.2', '3.2', '4.2', '1.2']

# Display
for parameter_name, parameter_default in zip(parameter_list, parameter_default_values):
    value = st.sidebar.slider(label=parameter_name, key=parameter_name,
                              value=float(parameter_default),
                              min_value=0.0,
                              max_value=8.0,
                              step=0.1)

    parameter_input_values.append(value)

if st.button("Show values"):
    parameter_input_values

result = model.predict_proba([parameter_input_values])
names = ['setosa', 'versicolor', 'virginica']
name = names[np.argmax(result[0])]
st.title(f'Prediction: {name}')
st.image(f"img/{name}.jpeg", width=512)
