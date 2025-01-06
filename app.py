import numpy as np
import pandas as pd
import pickle
import streamlit as st
from datetime import datetime
from pathlib import Path
import matplotlib.pyplot as plt

# Load models using pickle
le_path = Path(__file__).parents[0] / r"C:\Users\peer1\OneDrive\Documents\Guvi_Projects\3.Flight Price and  Customer Satisfaction Prediction\Airline Satisfaction Prediction\Models\label_encoder.pkl"
le = pickle.load(open(le_path, "rb"))
forest_path = Path(__file__).parents[0] / r"C:\Users\peer1\OneDrive\Documents\Guvi_Projects\3.Flight Price and  Customer Satisfaction Prediction\Airline Satisfaction Prediction\Models\forest_model.pkl"
forest_model = pickle.load(open(forest_path, "rb"))
flight_model_path = r'C:\Users\peer1\OneDrive\Documents\Guvi_Projects\3.Flight Price and  Customer Satisfaction Prediction\Flight Price Prediction\model\flight_prediction.pkl'
flight_model = pickle.load(open(flight_model_path, 'rb'))

# Functions
def satisfaction_prediction(input_data):
    prediction = forest_model.predict(input_data)
    if prediction[0] == 0:
        return "The passenger is neutral or dissatisfied with their flight!"
    else:
        return "The passenger was satisfied with their flight!"

def label_encode(data):
    cat = ['Type of Travel', 'Class', 'Customer Type']
    for name in cat:
        data[name] = data[name].apply(lambda x: le.classes_[0] if x not in le.classes_ else x)
        data[name] = le.transform(data[name])
    return data

def flight_prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = flight_model.predict(input_data_reshaped)
    rounded_value = round(prediction[0], 2)
    return rounded_value

def main():
    st.sidebar.title("Airline Prediction Apps")
    app_mode = st.sidebar.selectbox("Choose the app", ["Passenger Satisfaction Prediction", "Flight Price Prediction"])

    if app_mode == "Passenger Satisfaction Prediction":
        st.title("✈️ Airline Passenger Satisfaction")
        st.subheader("Web App - Survey")

        customer_type = st.selectbox("Are you a New Customer for this airline?", ['Disloyal Customer', 'Loyal Customer'], index=1)
        type_travel = st.selectbox("What was the purpose of your flight?", ["Personal Travel", "Business Travel"])
        class1 = st.selectbox("What was the Class of your flight?", ['Eco', 'Business', 'Eco Plus'])

        online_boarding = st.radio("Satisfaction level for Online Boarding?", [0, 1, 2, 3, 4, 5], horizontal=True)
        inflight_wifi = st.radio("Satisfaction level of the Inflight Wifi Service?", [0, 1, 2, 3, 4, 5], horizontal=True)
        entertainment = st.radio("Satisfaction level of the Inflight Entertainment?", [0, 1, 2, 3, 4, 5], horizontal=True)
        seat_comfort = st.radio("Satisfaction level of the Seat Comfort?", [0, 1, 2, 3, 4, 5], horizontal=True)
        online_booking = st.radio("Satisfaction level of Ease of making an Online Booking?", [0, 1, 2, 3, 4, 5], horizontal=True)
        leg_room = st.radio("How would you rate the Leg Room Service?", [0, 1, 2, 3, 4, 5], horizontal=True)

        df_dict = {
            'Online boarding': online_boarding,
            'Inflight wifi service': inflight_wifi,
            'Type of Travel': type_travel,
            'Class': class1,
            'Inflight entertainment': entertainment,
            'Seat comfort': seat_comfort,
            'Ease of Online booking': online_booking,
            'Leg room service': leg_room,
            'Customer Type': customer_type
        }
        user_data = pd.DataFrame([df_dict])
        user_data_encoded = label_encode(user_data)

        st.write("### Input Data", user_data)

        if st.button("Passenger Satisfaction Result"):
            Satisfaction = satisfaction_prediction(user_data_encoded)
            if Satisfaction == "The passenger is neutral or dissatisfied with their flight!":
                st.error(Satisfaction, icon="🚨")
            else:
                st.success(Satisfaction)
                st.balloons()

            st.write("### Satisfaction Levels Bar Chart")
            user_data_chart = user_data.iloc[0, :-1].plot(kind='bar', figsize=(10, 5), color='skyblue')
            plt.title("Passenger Satisfaction Inputs")
            plt.ylabel("Satisfaction Level")
            plt.xticks(rotation=45)
            st.pyplot(plt)

    elif app_mode == "Flight Price Prediction":
        st.title("💸 Flight Price Prediction")

        sources = [f"Source_{source}" for source in ['Chennai', 'Delhi', 'Kolkata', 'Mumbai']]
        destinations = [f"Destination_{destination}" for destination in ['Cochin', 'Delhi', 'Hyderabad', 'Kolkata']]
        airlines = [f"Airline_{airline}" for airline in ['Air India', 'GoAir', 'IndiGo', 'Jet Airways', 'Jet Airways Business', 'Multiple carriers', 'Multiple carriers Premium economy', 'SpiceJet', 'Trujet', 'Vistara', 'Vistara Premium economy']]

        selected_source = st.selectbox('Select Source', [s.split("_")[1] for s in sources])
        source_mapping = {source: 1 if source.split("_")[1] == selected_source else 0 for source in sources}
        Source = list(source_mapping.values())

        selected_destination = st.selectbox('Select Destination', [d.split("_")[1] for d in destinations])
        destination_mapping = {destination: 1 if destination.split("_")[1] == selected_destination else 0 for destination in destinations}
        Destination = list(destination_mapping.values())

        dep_date = st.date_input("Departure Date")
        dep_time = st.time_input("Departure Time")

        arrival_date = st.date_input("Arrival Date")
        arrival_time = st.time_input("Arrival Time")

        Journey_Day = dep_date.day
        Journey_Month = dep_date.month

        Departure_Hour = dep_time.hour
        Departure_Min = dep_time.minute

        Arrival_Hour = arrival_time.hour
        Arrival_Min = arrival_time.minute

        Departure_Datetime = datetime.combine(dep_date, dep_time)
        Arrival_Datetime = datetime.combine(arrival_date, arrival_time)

        duration = Arrival_Datetime - Departure_Datetime
        Duration_Hours = duration.days * 24 + duration.seconds // 3600
        Duration_Minutes = (duration.seconds % 3600) // 60

        Total_Stops = st.number_input("Number of Stops", min_value=0, step=1, value=0)

        selected_airline = st.selectbox('Select Airline', [a.split("_")[1] for a in airlines])
        airline_mapping = {airline: 1 if airline.split("_")[1] == selected_airline else 0 for airline in airlines}
        Airlines = list(airline_mapping.values())

        journey_input = [Total_Stops, Journey_Day, Journey_Month, Departure_Hour, Departure_Min, Arrival_Hour, Arrival_Min, Duration_Hours, Duration_Minutes]
        airline_input = Airlines
        source_input = Source
        destination_input = Destination
        Input = journey_input + airline_input + source_input + destination_input

        st.write("### Flight Details Summary", pd.DataFrame(
            [Input],
            columns=[
                "Total Stops", "Journey Day", "Journey Month", "Departure Hour", "Departure Minute", 
                "Arrival Hour", "Arrival Minute", "Duration Hours", "Duration Minutes"
            ] + airlines + sources + destinations
        ))

        if st.button('Predict Price'):
            price_prediction = flight_prediction(Input)
            st.markdown(
                f"""
                <h3 style='text-align: center;'>You will have to pay approximately Rs. {price_prediction}</h3>
                """, unsafe_allow_html=True
            )

if __name__ == "__main__":
    main()
