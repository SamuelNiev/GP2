import time  # to simulate a real time data, time loop

import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import streamlit as st  # 🎈 data web app development
import altair as alt


st.set_page_config(
    page_title="Real-Time Data Science Dashboard",
    page_icon="✅",
    layout="wide",
)

# read csv from a github repo
dataset_url = "https://data.stadt-zuerich.ch/dataset/ewz_bruttolastgang_stadt_zuerich/download/2023_ewz_bruttolastgang.csv"

# read csv from a URL
def get_data() -> pd.DataFrame:
    return pd.read_csv(dataset_url)


df = get_data()
df.drop('status', axis=1)
del df['status']


st.dataframe(df)  # Same as st.write(df)

chart = alt.Chart(df).mark_line().encode(
            x=alt.X('zeitpunkt', axis=alt.Axis(labelOverlap="greedy",grid=False)),
            y=alt.Y('bruttolastgang'))
st.altair_chart(chart, use_container_width=True)