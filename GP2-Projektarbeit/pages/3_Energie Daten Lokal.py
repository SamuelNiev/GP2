import pandas as pd
import streamlit as st
import altair as alt


df = pd.read_csv("/home/admin/GP2-Projektarbeit/Verbrauch_Export.csv")  # lesen der CSV Datein vom Ordner


st.title('Energiemessung')  # Titel
st.write(df, use_column_width=True)  # Visualisierung des Dataframes in Streamlit

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

