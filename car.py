import streamlit as st
import pandas as pd
import joblib


model_path = 'EV_Population_model.pk1'
model = joblib.load(model_path)

car_brands = [
    "MAKE_TESLA", "MAKE_BMW", "MAKE_CHEVROLET", "MAKE_KIA", "MAKE_TOYOTA", 
    "MAKE_NISSAN", "MAKE_JEEP", "MAKE_FIAT", "MAKE_FORD", "MAKE_VOLVO", 
    "MAKE_CHRYSLER", "MAKE_LEXUS", "MAKE_ALFA ROMEO", "MAKE_JAGUAR", "MAKE_AUDI", 
    "MAKE_PORSCHE", "MAKE_MINI", "MAKE_MAZDA", "MAKE_DODGE", "MAKE_HONDA", 
    "MAKE_HYUNDAI", "MAKE_POLESTAR", "MAKE_MERCEDES-BENZ", "MAKE_VOLKSWAGEN", 
    "MAKE_LINCOLN", "MAKE_MITSUBISHI", "MAKE_SMART", "MAKE_LAND ROVER", 
    "MAKE_SUBARU", "MAKE_CADILLAC", "MAKE_THINK", "MAKE_FISKER", 
    "MAKE_AZURE DYNAMICS", "MAKE_BENTLEY", "MAKE_WHEEGO ELECTRIC CARS", "MAKE_LAMBORGHINI"
]


st.write("""
# CAFV Eligibility Prediction App
This app predicts the CAFV Eligibility.
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    Model_Year = st.sidebar.slider('Model Year', 1999, 2025, 1999)
    Make = st.sidebar.selectbox('Make', car_brands)
    Electric_Vehicle_Type = st.sidebar.selectbox('Electric Vehicle Type',['BEV','PHEV'] )
    Electric_range = st.sidebar.slider('Electric Range', 6, 337, 6)
    Base_MSRP = st.sidebar.slider('Base MSRP', 0, 845000, 100000)
    Legislative_district = st.sidebar.slider('Legislative District', 1, 49, 1)
    data = {
    'Model Year': Model_Year,
    'Electric Range': Electric_range,
    'Base MSRP': Base_MSRP,
    'Legislative District': Legislative_district,
    'Make_ALFA ROMEO': 1 if Make == "ALFA ROMEO" else 0,
    'Make_AUDI': 1 if Make == "AUDI" else 0,
    'Make_AZURE DYNAMICS': 1 if Make == "AZURE DYNAMICS" else 0,
    'Make_BENTLEY': 1 if Make == "BENTLEY" else 0,
    'Make_BMW': 1 if Make == "BMW" else 0,
    'Make_CADILLAC': 1 if Make == "CADILLAC" else 0,
    'Make_CHEVROLET': 1 if Make == "CHEVROLET" else 0,
    'Make_CHRYSLER': 1 if Make == "CHRYSLER" else 0,
    'Make_DODGE': 1 if Make == "DODGE" else 0,
    'Make_FIAT': 1 if Make == "FIAT" else 0,
    'Make_FISKER': 1 if Make == "FISKER" else 0,
    'Make_FORD': 1 if Make == "FORD" else 0,
    'Make_HONDA': 1 if Make == "HONDA" else 0,
    'Make_HYUNDAI': 1 if Make == "HYUNDAI" else 0,
    'Make_JAGUAR': 1 if Make == "JAGUAR" else 0,
    'Make_JEEP': 1 if Make == "JEEP" else 0,
    'Make_KIA': 1 if Make == "KIA" else 0,
    'Make_LAMBORGHINI': 1 if Make == "LAMBORGHINI" else 0,
    'Make_LAND ROVER': 1 if Make == "LAND ROVER" else 0,
    'Make_LEXUS': 1 if Make == "LEXUS" else 0,
    'Make_LINCOLN': 1 if Make == "LINCOLN" else 0,
    'Make_MAZDA': 1 if Make == "MAZDA" else 0,
    'Make_MERCEDES-BENZ': 1 if Make == "MERCEDES-BENZ" else 0,
    'Make_MINI': 1 if Make == "MINI" else 0,
    'Make_MITSUBISHI': 1 if Make == "MITSUBISHI" else 0,
    'Make_NISSAN': 1 if Make == "NISSAN" else 0,
    'Make_POLESTAR': 1 if Make == "POLESTAR" else 0,
    'Make_PORSCHE': 1 if Make == "PORSCHE" else 0,
    'Make_SMART': 1 if Make == "SMART" else 0,
    'Make_SUBARU': 1 if Make == "SUBARU" else 0,
    'Make_TESLA': 1 if Make == "TESLA" else 0,
    'Make_TH!NK': 1 if Make == "TH!NK" else 0,
    'Make_TOYOTA': 1 if Make == "TOYOTA" else 0,
    'Make_VOLKSWAGEN': 1 if Make == "VOLKSWAGEN" else 0,
    'Make_VOLVO': 1 if Make == "VOLVO" else 0,
    'Make_WHEEGO ELECTRIC CARS': 1 if Make == "WHEEGO ELECTRIC CARS" else 0,
    'Electric Vehicle Type_BEV': 1 if Electric_Vehicle_Type == "BEV" else 0,
    'Electric Vehicle Type_PHEV': 1 if Electric_Vehicle_Type == "PHEV" else 0,
}

    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()
st.subheader('User Input parameters') 
st.write(df)


# Make predictions
prediction = model.predict(df)  # Predict eligibility
prediction_proba = model.predict_proba(df)  # Get probabilities

# Display results
st.subheader('Prediction')
# eligibility = 'This Vehicle is Eligible for CAFV' if prediction[0] == 1 else 'This Vehicle is Not Eligible for CAFV'

st.write(prediction)  # Debugging output

