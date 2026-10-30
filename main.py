import streamlit as st
import plotly.express as px
import pandas as pd

st.title("Pollution Dashboard")
st.subheader("created Michael Garcia.")

st.header("Pollution Rate by State in 2020")
df = pd.read_csv("airpollution.csv",sep=",")
# Plot chart
parameter = st.multiselect(label="Select states to filter out.", options=df['State'].tolist())

if parameter:
    filtered_df = df[~df['State'].isin(parameter)] # checks if State value is not in the parameter list.
else:
    filtered_df = df

fig = px.bar(filtered_df,
              x="State",
              y="Micrograms per cubic meter (PM2.5)(1)",
              title="Pollution by State")
fig.update_xaxes(dtick=1) # fixes auto cut off for too many columns. i.e. Ensures all states shown
st.plotly_chart(fig)

st.header("What does the data tell us?")
st.text("Sates with major urban centers bear the worst air pollution compared to states with smaller urban environments.")

