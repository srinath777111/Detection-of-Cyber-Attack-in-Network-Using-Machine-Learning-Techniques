import streamlit as st
from keras.preprocessing import image
from PIL import Image
import numpy as np
import tensorflow as tf
import pickle
import pandas as pd

img_height, img_width = 224, 224
df1=pd.read_csv('UNSW_NB15_testing-set.csv')
df1=df1.drop(["Unnamed: 0"],axis=1)
df_test = df1.drop(['label'], axis=1)
import pandas as pd
from sklearn.preprocessing import LabelEncoder


# Initialize the LabelEncoder
le = LabelEncoder()

# Apply LabelEncoder to the specified columns
df_test['proto']=le.fit_transform(df_test['proto'])
df_test['service']=le.fit_transform(df_test['service'])
df_test['state']=le.fit_transform(df_test['state'])
df_test['attack_cat']=le.fit_transform(df_test['attack_cat'])

# Title for the dashboard
st.title('Detection of Cyber Attack in Network using Machine Learning Techniques')

# Header text
st.subheader("enter a column number")




# Define model
model = pickle.load(open('m', "rb"))


st.write('You have selected:', model)

hi = st.number_input("Integer")
hi = int(hi)
if st.button("Detect") :
    st.write(df_test.iloc[hi:hi+1,:-1])
    prediction  =  model.predict(df_test.iloc[hi:hi+1,:-1])
    match prediction:
        case 0:
            st.write("Analysis")
        case 1:
            st.write('Backdoor')
        case 2:
            st.write('DoS')
        case 3:
            st.write('Exploits')
        case 4:
            st.write('Fuzzers')
        case 5:
            st.write('Generic')
        case 6:
            st.write('Normal')
        case 7:
            st.write('Reconnaissance')
        case 8:
            st.write('Shellcode')
        case 9:
            st.write('Worms')
    st.write(prediction)

