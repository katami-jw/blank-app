import streamlit as st
import pandas as pd

data = {"menu" : ["pepperoni","teriyaki","margherita","thin crust","pan style crust","cheese","tomato","habanero","chicken"],"cost" : [1800,2100,1900,0,100,100,150,100,200]}
df_data = pd.DataFrame(data)

st.title('pizza order')

pizza = st.selectbox(
    "pizza menu",
    ("pepperoni", "teriyaki", "margherita"))

crust = st.radio(
    "crust",
    ["thin crust", "pan style crust"])

toppings = st.multiselect(
    "add toppings",
    ["cheese", "tomato", "pepperoni", "chicken"])

count = st.number_input("Insert a number",min_value=1, value="min", step=1)

order = toppings + [pizza,crust]

df_order = df_data.query('menu in @order')

st.write('total amount　▶ ',sum(df_order["cost"]))