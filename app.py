import streamlit as st
import requests
import pandas as pd
import datetime



'''
# Le site des équations 🥳
'''

st.markdown('''
Bienvenue  ̴

Submit your image and let the magic work''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:

'''
## coordonnees
p_long = st.number_input('Pickup longitude')
p_lat = st.number_input('Pickup latitude')
d_long = st.number_input('Dropoff longitude')
d_lat = st.number_input('Dropoff latitude')

## date
d = st.date_input("Choose the date", datetime.date(2022, 5, 27))

## time
t = st.time_input('Choose the hour', datetime.time(8, 45))

# concatene les 2
date_time = datetime.datetime.combine(d, t)


## nombre de passagers
nb_passenger = st.selectbox('Number of passengers', (range(1, 8)))




'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''

st.write('Day/Time :', date_time)

params = {'pickup_datetime': str(date_time),
           'pickup_longitude':p_long,
           'pickup_latitude':p_lat,
           'dropoff_longitude':d_long,
           'dropoff_latitude':d_lat,
           'passenger_count': nb_passenger, }


st.write(params)


#print(paramss['nb_pass'])
url = 'https://taxifare.lewagon.ai/predict'
res = requests.get(url, params=params).json()


st.write("You have to pay $", res['fare'])
