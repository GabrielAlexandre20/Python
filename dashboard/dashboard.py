import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df = pd.read_excel("03.24_Controle de Meta Transportes.xlsx", decimal=",", sheet_name=4, skiprows=4)
df["Data"] = pd.to_datetime(df["Data"])
df=df.sort_values("Data")

df["Month"] = df["Data"].apply(lambda x: str(x.year) + "-" + str(x.month))
month = st.sidebar.selectbox("Mês", df["Month"].unique())

df_filtered = df[df["Month"] == month]

df_filtered = df_filtered[(df_filtered["Cod"] != "3º") & (df_filtered["Cod"] != "R")]

col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

df_grouped = df_filtered.groupby(["Data", "Nome"])["Vl Nota"].sum().reset_index()
fig_date = px.bar(df_grouped, x="Data", y="Vl Nota", color="Nome", title="Faturamento por dia")
col1.plotly_chart(fig_date)

fig_valor = px.pie(df_grouped, values="Vl Nota", names="Nome", title="Faturamento por motorista")
col2.plotly_chart(fig_valor)

