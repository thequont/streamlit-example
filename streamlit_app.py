import streamlit as st
import pandas as pd
df = pd.DataFrame(pd.read_csv("data.csv"))
df['time'] = pd.to_datetime(df['time'])
clist = df['ID'].unique()
country = st.sidebar.selectbox("Select ID:",clist)
st.header("T over time")
fig = px.line(df[df['ID'] == ID], 
    x = "time", y = "T", title = ID)
st.plotly_chart(fig)

st.header("data dump")
st.write(df)
