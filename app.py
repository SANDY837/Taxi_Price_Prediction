# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 19:37:59 2022

@author: sande
"""




import pandas as pd

import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open("C:/Users/sande/Desktop/Taxi_Streamlit-app/taxi-fare.sav", 'rb'))


    
    

def main():
     # giving a title
    st.title('Taxi Price Prediction')
    
    
    # getting the input data from the user
    
    
    latitude_of_pickup = st.text_input('latitude_of_pickup')
    
    latitude_of_dropoff= st.text_input('latitude_of_dropoff')
    no_of_passenger = st.text_input('no_of_passenger')
    
    
    
    
    # code for Prediction
    price = ''
    
    # creating a button for Prediction
    
    if st.button('Predict Price'):
        
        price=loaded_model.predict(pd.DataFrame([[40.721319,40.712278,1]]
                                        ,columns=["latitude_of_pickup","latitude_of_dropoff","no_of_passenger"]))

        
    st.success(price)
    
    
    
if __name__ == '__main__':
    main()