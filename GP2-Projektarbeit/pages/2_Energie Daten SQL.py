import pandas as pd
import streamlit as st
import altair as alt
import mysql.connector

st.title('Energie Messung aus SQL')
st.experimental_singleton
def init_connection():
    return mysql.connector.connect(**st.secrets['mysql'])

conn = init_connection()

st.experimental_memo(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()


rows = run_query('Select * from verbrauch_export;')


@st.experimental_memo
def load_data(rows):
    return pd.DataFrame(rows)
    
    st.dataframe(rows)

st.checkbox("Use container width", value=False, key="use_container_width")

df = load_data(rows)
df.columns = ['Zeitraum', 'Menge HT (kWh)', 'Menge NT (kWh)', 'Menge Total (kWh)', 'Maximale Leistung (kW)']
# Display the dataframe and allow the user to stretch the dataframe
# across the full width of the container, based on the checkbox value
st.dataframe(df, use_container_width=st.session_state.use_container_width)

#Eintrag erfassen
st.header('Neuen Eintrag erfassen')
neuTIME = list(st.text_input('Zeitraum (dd.mm.yyyy hh:mm-hh:mm)'))
neuHT = float(st.number_input('Menge HT (kWh)'))
neuNT = float(st.number_input('Menge NT (kWh)'))
neuMT = float(st.number_input('Menge Total (kWh)'))
neuML = float(st.number_input('Maximale Leistung (kW)'))


neuWert = [neuTIME, neuHT, neuNT, neuMT, neuML]
#neuWert = [neuTIME]

if st.button('Wert in Tabelle schreiben'):
    mycursor = conn.cursor()
    sql = ("""INSERT INTO gp2projekt.verbrauch_export ('Zeitraum', 'Menge HT (kWh)', 'Menge NT (kWh)', 'Menge Total (kWh)', 'Maximale Leistung (kW)') VALUES (%d, %s, %s, %s, %s)""")
#   sql = ("""INSERT INTO gp2projekt.verbrauch_export ('Menge HT (kWh)') VALUES (%s)""")
    val = neuWert
    mycursor.executemany(sql, val)
    myde.commit()
    





st.header('Darstellung')





option = st.selectbox(
    'Auswahl',
    ('Menge HT (kWh)', 'Menge NT (kWh)', 'Menge Total (kWh)', 'Maximale Leistung (kW)'))

st.write('You selected:', option)
# Chart erstellen für die Jeweiligen Zeilen

if option == 'Menge HT (kWh)': # Chart Hochtarif
    chart = alt.Chart(df).mark_line().encode(
            x=alt.X('Zeitraum', axis=alt.Axis(labelOverlap="greedy",grid=False)),
            y=alt.Y('Menge HT (kWh)'))
    st.altair_chart(chart, use_container_width=True)

if option == 'Menge NT (kWh)': # Chart Niedertarif
    chart = alt.Chart(df).mark_line().encode(
            x=alt.X('Zeitraum', axis=alt.Axis(labelOverlap="greedy",grid=False)),
            y=alt.Y('Menge NT (kWh)'))
    st.altair_chart(chart, use_container_width=True)

if option == 'Menge Total (kWh)': # Chart Energie Total
    chart = alt.Chart(df).mark_line().encode(
            x=alt.X('Zeitraum', axis=alt.Axis(labelOverlap="greedy",grid=False)),
            y=alt.Y('Menge Total (kWh)'))
    st.altair_chart(chart, use_container_width=True)

if option == 'Maximale Leistung (kW)': # Chart Maximale Leistungverbrauch
    chart = alt.Chart(df).mark_line().encode(
            x=alt.X('Zeitraum', axis=alt.Axis(labelOverlap="greedy",grid=False)),
            y=alt.Y('Maximale Leistung (kW)'))
    st.altair_chart(chart, use_container_width=True)
