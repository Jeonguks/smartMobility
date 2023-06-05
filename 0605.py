import streamlit as st
from PIL import Image

image = Image.open('pig.jpg')

st.image(image, caption='YOUR FACE')


st.write('# BMI Calculator')
def det(bmi):
    st.balloons()
    if(bmi<=18.5):
        return '저체중'
    elif(bmi<=23):
        return '정상'
    elif(bmi<=25):
        return '과체중'
    else:
        return '비만'

height = st.number_input('Insert your height ( cm ) ',100,250,170,5)
st.write('Height: ',height,' cm')
weight = st.number_input ('Insert your weight (kg)',0,150,60,5)
st.write (weight, 'kg')
bmi = weight/( (height/100) **2)
if st. button('Calculate') :
    st.write('Your BMI : ', round (bmi, 2)) 
    st.write('당신은', det(bmi),' 입니다.')