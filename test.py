import streamlit as st, pandas as pd, numpy as np

st.title("Stream LIT Practice")
st.header("Stream LIT Header")
st.subheader("Stream LIT Sub Header")
st.write("my content")
st.caption("my caption")

df=pd.DataFrame({'first column':[1,2,3,4,5],
'second column':[10,20,30,40,50]})

st.write(df)

x=st.sidebar.slider('X',0,20)
st.write(x*x)

if st.sidebar.checkbox('Checkbox'):
    st.balloons()
else: st.info('Test Dialog')
    # st.warning()

y=st.sidebar.text_input('Name')
st.write(y)

st.number_input('Number',50,100)
st.date_input('Date')

option=st.selectbox('Select Number :',[1,2,3,4,5])
st.write('Your Selected : ',option)


# print("Kiran Kumar Reddy")