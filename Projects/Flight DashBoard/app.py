import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from dbhelper import DB

db = DB()

st.sidebar.title('Flights Analytics')
option = st.sidebar.selectbox('Menu',['Select One','Check Flights','Analytics'])

if option == 'Check Flights':
    st.title('Check Flights')
    col1,col2 = st.columns(2)

    with col1:
        cites = db.fetch_flights_city()
        source = st.selectbox('Source',cites)

    with col2:
        cites = db.fetch_flights_city()
        destination = st.selectbox('Destination',cites)

    if st.button('Search'):
        data = db.fetch_Source_destination_details(source,destination)
        st.dataframe(data)

elif option == 'Analytics':
    st.title('Analytics')
    Airline,frequency = db.fetch_Airline_frequency()
    
    fig = go.Figure(
        data=[
            go.Pie(
                labels=Airline,
                values=frequency
            )
        ]
    )

    fig.update_layout(
        title="Number of Flights by Airline | Airline having Most Number Of Flights"
    )

    st.plotly_chart(fig)


    source,frequency = db.busy_airpory_city()
    fig = px.bar(
        x=source,
        y=frequency,
        labels={
            "x": "City name",
            "y": "Number of Flights"
        },
        title="Flights by City | Most Busy City In Flights"
    )

    st.plotly_chart(fig, use_container_width=True)

    airline,avg_price = db.Fetch_avg_price()
    fig = px.bar(
        x=airline,
        y=avg_price,
        labels={
            "x": "Airline names",
            "y": "Average Price"
        },
        title="Average Price by Airline | Most Expensive Airline"
    )

    st.plotly_chart(fig, use_container_width=True)



else:
    st.title('Flight Dashboard')
    st.write("""

## Overview

The Flight Dashboard is an interactive data visualization tool designed to analyze and monitor flight operations efficiently. It provides valuable insights into airline performance, flight schedules, delays, cancellations, routes, and overall travel trends through easy-to-understand charts and visualizations.

This dashboard helps users explore key performance indicators (KPIs), identify operational patterns, and make data-driven decisions. By transforming raw flight data into meaningful insights, the dashboard enables better understanding of airline operations and supports performance analysis.

### Key Features

* Total number of flights and airlines

* Flight status analysis (On-Time, Delayed, Cancelled)

* Airline performance comparison

* Departure and arrival trends

* Route and destination analysis

* Delay analysis by airline, airport, or time

* Interactive filters for date, airline, airport, and route

* Dynamic charts and KPI cards for quick insights


### Objective

The primary objective of this Flight Dashboard is to provide a comprehensive overview of flight operations, helping users identify trends, improve operational efficiency, and support informed decision-making through interactive visual analytics.

""")