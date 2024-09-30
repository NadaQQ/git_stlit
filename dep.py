import streamlit as st
st.title('hello world')

from joblib import load

model = load('model.pkl')

st.write('##salary prediction')

x= st.slider('Experiance',0,40)
y= model.predict([[x]])

st.write('salary is', y)