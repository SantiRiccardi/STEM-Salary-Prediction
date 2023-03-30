import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler 

def load_model():
    with open('/Users/santi/Bootcamp/Salarios en STEM/src/model/best_model.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

model = load_model()


page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))

if page == "Predict":
    st.title("STEM Salary Prediction in United States")
    st.image('/Users/santi/Bootcamp/Salarios en STEM/img/STEM.png')
    st.write(""" Please enter your data """)

    title = ('Software Engineer',               
        'Product Manager',                  
        'Software Engineering Manager',     
        'Data Scientist ',                  
        'Hardware Engineer ',               
        'Product Designer',                 
        'Technical Program Manager',        
        'Solution Architect',                
        'Management Consultant',             
        'Business Analyst')

    gender = ('Male',
             'Female',
             'Unknown')

    race = ('Race_Asian', 
            'Race_White', 
            'Race_Two_Or_More', 
            'Race_Black',
            'Race_Hispanic')
    region = ('northeast',
              'south',
              'west',
              'midwest')
    education = ('Masters_Degree',
        'Bachelors_Degree', 
        'Doctorate_Degree', 
        'Highschool', 
        'Some_College')

    level = ('junior','semi_senior','senior')
    
    # Diccionario con todos los campos con valor 0
    d = {'title':{'Software Engineer':0,               
                  'Product Manager':0,                  
                  'Software Engineering Manager':0,     
                  'Data Scientist':0,                  
                  'Hardware Engineer':0,               
                  'Product Designer':0,                 
                  'Technical Program Manager':0,        
                  'Solution Architect':0,                
                  'Management Consultant':0,             
                  'Business Analyst':0},

        'gender': {'Male':0, 'Female':0, 'Unknown':0},

        'race':{'Race_Asian':0, 
                'Race_White':0, 
                'Race_Two_Or_More':0, 
                'Race_Black':0,
                'Race_Hispanic':0},
        
        'region': {'northeast':0,
                   'south':0,
                   'west':0,
                   'midwest':0},

        'education':{'Masters_Degree':0,
                    'Bachelors_Degree':0, 
                    'Doctorate_Degree':0, 
                    'Highschool':0, 
                    'Some_College':0},

        'level':{'junior':0,'semi_senior':0,'senior':0}
    }

    # Carga de datos por parte del usuario
    title = st.selectbox("Title", title)
    gender = st.selectbox("Gender", gender)
    race = st.selectbox("Race", race)
    region = st.selectbox("Region", region)
    st.image('/Users/santi/Bootcamp/Salarios en STEM/img/Regions.png')
    education = st.multiselect("Education Level", education)
    level = st.selectbox("level", level)
    yearsofexperience = st.slider("Years of Experience", 0, 50, 0)
    
    # Diccionario modificado con valores cargados por el usuario
    d['title'][title]=1
    d['gender'][gender]=1
    d['region'][region]=1
    d['level'][level]=1
    d['race'][race]=1
    
    for ed in education:
        d['education'][ed]=1
    

    salary = st.button("Calculate Salary")
    if salary:
        test = {'yearsofexperience': yearsofexperience,
                'masters_degree': d['education']['Masters_Degree'],
                'bachelors_degree': d['education']['Bachelors_Degree'],
                'doctorate_degree': d['education']['Doctorate_Degree'],
                'highschool': d['education']['Highschool'],
                'some_college': d['education']['Some_College'],
                'race_asian': d['race']['Race_Asian'],
                'race_white': d['race']['Race_White'],
                'race_two_or_more': d['race']['Race_Two_Or_More'],
                'race_black': d['race']['Race_Black'],
                'race_hispanic': d['race']['Race_Hispanic'],
                'title_business analyst': d['title']['Business Analyst'],
                'title_data scientist': d['title']['Data Scientist'],
                'title_hardware engineer': d['title']['Hardware Engineer'],
                'title_management consultant': d['title']['Management Consultant'],
                'title_product designer': d['title']['Product Designer'],
                'title_product manager': d['title']['Product Manager'],
                'title_software engineer': d['title']['Software Engineer'],
                'title_software engineering manager': d['title']['Software Engineering Manager'],
                'title_solution architect': d['title']['Solution Architect'],
                'title_technical program manager': d['title']['Technical Program Manager'],
                'gender_female': d['gender']['Female'],
                'gender_male': d['gender']['Male'],
                'gender_unknown': d['gender']['Unknown'],
                'region_midwest': d['region']['midwest'],
                'region_northeast': d['region']['northeast'],
                'region_south': d['region']['south'],
                'region_west': d['region']['west'],
                'level_junior': d['level']['junior'],
                'level_semi_senior': d['level']['semi_senior'],
                'level_senior': d['level']['senior']}


        # Transformamos el diccionario test a DataFrame
        X = pd.DataFrame(test, index=[10])

        # Realizamos el Escalado Normalizado
        X_normalizado= StandardScaler().fit_transform(X)
        
        # Pasamos los datos a float
        X = X_normalizado.astype(float)

        # Realizamos la Prediccion
        salary = model.predict(X)

        # Imprimimos en pantalla el resultado
        st.subheader(f"The estimated salary is USD {salary[0]:.2f}")

  


