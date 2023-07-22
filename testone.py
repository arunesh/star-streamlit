import streamlit as st
import pandas as pd
import numpy as np

class Car():
    make : str
    model : str
    year : int
    def __init__(self, input):
        NotImplemented


class UserData():
    name : str
    age : int
    zip : int
    gender : str
    home_owner : bool
    num_accidents : int
    use_paperless : bool
    prior_coverage : bool
    num_years_prior : int

    """ Takes in JSON to create an object. Should be one per user. """
    def __init__(self, input):
        NotImplemented

# Initialize num_cars if not already present in current session.
if 'num_cars' not in st.session_state:
    st.session_state.num_cars = 0

st.title('StarGPT Auto Insurance Quoting System')

st.subheader('Basic Information:')
customer_name = st.text_input("Whats your name ? ", key="name")
customer_age = st.selectbox("Age", range(15, 90), key="age")
customer_zip =  st.number_input('Zip Code', min_value=33301, key="zip", step=None, format="%d")
customer_gender = st.selectbox("Gender", ["Male", "Female"], key="gender")

customer_is_home_owner = st.selectbox("Are you a home owner ?", ["Yes", "No"], key="home_owner", index = 1)

if customer_is_home_owner == "Yes":
    home_info = st.text_input("More info on your home")

customer_num_accidents = st.number_input("Number of accidents in the last 5 years: ", min_value = 0, key="accidents", step=None, format="%d")

customer_is_paperless = st.selectbox("Would you like to sign up for paperless ?", ["Yes", "No"], key="paperless", index = 1)

customer_prior_coverage = st.selectbox("Do you have prior coverage ?", ["Yes", "No"], key="prior_coverage", index = 1)

if customer_prior_coverage == "Yes":
    num_years_prior_coverage = st.text_input("How many years of prior insurance coverage have you had ?", key="num_years_cov")

# Number of cars. Update a car in session state.

# Show existing cars. 
num_cars_entered = st.session_state.get("num_cars")

# Example list of cars.
temp_cars = [{"make":"df", "model":"df", "year":2003}, {"make":"ddf", "model":"dfdf", "year":2005}]

def populate_cars(all_cars):
    for car in all_cars:
        st.write("Make = " + car["make"])
        st.write("Model = " + car["model"])
        st.write("Year = " + car["year"])
        st.buttion("Remove this car")


populate_cars(st.session_state.get("all_cars"))

# Quoting system.

st.subheader('Add or remove a car: ')
col1, col2 = st.columns([.5,1])
with col1:
    st.button("Add a car", key="add_car")

with col2:
    st.button("Remove a car", key="remove_car")


car_make = st.text_input("Car make ", key="make")
car_model = st.text_input("Car model", key="model")
car_year =  st.number_input('Car year', min_value=1990, key="year", step=None, format="%d")


def add_car():
    print("Add a car")

st.button("Add a car", on_click=add_car)

car_make, car_model, car_year

print("Name = ", st.session_state.name)
print("Age = ", st.session_state.age)
print("Age = ", st.session_state.zip)
print("Gender = ", st.session_state.gender)

#Are you a home owner ?

#Number of accidents in the last 5 years:

#Sign up for paperless ?

#Prior coverage ?


#Car info:

#Year, make, model, miles, 


DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")



# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')

st.subheader('Raw data')
st.write(data)
st.subheader('Number of pickups by hour')

hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]

st.bar_chart(hist_values)

st.subheader('Map of all pickups')
st.map(data)

print("Reached the EOF")

