import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

add_selectbox = st.sidebar.selectbox(
    "목차",
    ("체질량 계산기", "Gap Minder", "My Page")
)
if add_selectbox =="체질량 계산기":

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
elif add_selectbox == "Gap Minder":
    st.write('# Gap Minder')
    data = pd.read_csv('gapminder.csv')
    st.write(data)

    colors = []
    for x in data ['continent']:
        if x == 'Asia':
            colors.append ('tomato')
        elif x == 'Europe':
            colors.append ('blue')
        elif x == 'Africa':
            colors.append ('olive')
        elif x =='Americas':
            colors.append ('green')
        else:
            colors.append ('orange')

    data['colors']=colors
    
    year = st.slider('Select Year ',1952,2007,1952, step = 5)
   

    data=data[data['year']==year]

    fig, ax = plt.subplots()
    ax.scatter(data['gdpPercap'],data['lifeExp'],s=data['pop']*0.000002,color=data['colors'])
    st.pyplot(fig)
else:
    st.write('# My page')
