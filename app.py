import streamlit as st
import pandas as pd
import joblib

# Load the trained model
@st.cache_resource
def load_model():
    return joblib.load('model.pkl')

model = load_model()

st.title("Wellness Tourism Package Prediction")
st.write("Enter the customer's details to predict if they will purchase the new Wellness Tourism Package.")

with st.form("prediction_form"):
    st.header("Customer Details")
    
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input("Age", min_value=18, max_value=100, value=30)
        type_of_contact = st.selectbox("Type of Contact", ["Self Enquiry", "Company Invited"])
        city_tier = st.selectbox("City Tier", [1, 2, 3])
        occupation = st.selectbox("Occupation", ["Salaried", "Small Business", "Large Business", "Free Lancer"])
        gender = st.selectbox("Gender", ["Male", "Female"])
        number_of_person_visiting = st.number_input("Number of Persons Visiting", min_value=1, max_value=10, value=2)
        preferred_property_star = st.selectbox("Preferred Property Star", [3.0, 4.0, 5.0])
        marital_status = st.selectbox("Marital Status", ["Single", "Married", "Divorced", "Unmarried"])
        
    with col2:
        number_of_trips = st.number_input("Number of Trips", min_value=1.0, max_value=10.0, value=2.0)
        passport = st.selectbox("Passport", [0, 1])
        own_car = st.selectbox("Own Car", [0, 1])
        number_of_children_visiting = st.number_input("Number of Children Visiting", min_value=0.0, max_value=5.0, value=0.0)
        designation = st.selectbox("Designation", ["Executive", "Manager", "Senior Manager", "AVP", "VP"])
        monthly_income = st.number_input("Monthly Income", min_value=1000.0, max_value=100000.0, value=20000.0)
        
        st.header("Interaction Details")
        duration_of_pitch = st.number_input("Duration of Pitch", min_value=1.0, max_value=100.0, value=15.0)
        number_of_followups = st.number_input("Number of Followups", min_value=1.0, max_value=10.0, value=3.0)
        product_pitched = st.selectbox("Product Pitched", ["Basic", "Standard", "Deluxe", "Super Deluxe", "King"])
        pitch_satisfaction_score = st.selectbox("Pitch Satisfaction Score", [1, 2, 3, 4, 5])

    submit_button = st.form_submit_button(label="Predict Purchase")

if submit_button:
    # Create a DataFrame from the inputs
    input_data = pd.DataFrame([{
        "Age": age,
        "TypeofContact": type_of_contact,
        "CityTier": city_tier,
        "DurationOfPitch": duration_of_pitch,
        "Occupation": occupation,
        "Gender": gender,
        "NumberOfPersonVisiting": number_of_person_visiting,
        "NumberOfFollowups": number_of_followups,
        "ProductPitched": product_pitched,
        "PreferredPropertyStar": preferred_property_star,
        "MaritalStatus": marital_status,
        "NumberOfTrips": number_of_trips,
        "Passport": passport,
        "PitchSatisfactionScore": pitch_satisfaction_score,
        "OwnCar": own_car,
        "NumberOfChildrenVisiting": number_of_children_visiting,
        "Designation": designation,
        "MonthlyIncome": monthly_income
    }])
    
    # Make prediction
    try:
        prediction = model.predict(input_data)
        if prediction[0] == 1:
            st.success("The customer is likely to purchase the Wellness Tourism Package.")
        else:
            st.error("The customer is unlikely to purchase the Wellness Tourism Package.")
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")
