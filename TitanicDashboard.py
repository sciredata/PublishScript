import streamlit as st
import pandas as pd
import plotly.express as px
##
## streamlit run c:/_Apps/UDEMY/BuildAndDeployStreamlitDataProducts/PublishScript/TitanicDashboard.py
##
## Titanic Dashboard - Publisdhable Streamlit App 1
##
st.set_page_config(layout='wide')
st.title('Titanic Dashboard')

## Load DataFrame: PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
df = pd.read_csv('C:\\_Apps\\UDEMY\\BuildAndDeployStreamlitDataProducts\\DataFiles\\titanic.csv')
##
port_list = df['Embarked'].unique()                           ## Build Port List 
gender_list = df['Sex'].unique()                              ## Build Gender List 

col1,col2 = st.columns([1,1])
with col1:
    port_selected = st.selectbox(label='Select a port',options=port_list, key='dd1', index=1, help='Port of Departure', label_visibility='visible')
with col2:
    gender_selected = st.selectbox(label='Select a gender',options=gender_list, key='dd2', index=1, help='Gender', label_visibility='visible')
 
filtered_df = df.loc[(df['Embarked'] == port_selected) & (df['Sex'] == gender_selected)]           ## Filter data on selected port and gender

##  Age distribution Histogram   
plot = px.histogram(data_frame=filtered_df, x='Age', title='Distribution of Age', color='Survived', template='seaborn', facet_col='Survived')   
col1.plotly_chart(plot)
## Pie Chart
pie_chart_df = filtered_df.loc[:,['PassengerId','Survived']].groupby(['Survived']).count().reset_index()    ## Group by Survived and count PassengerId
pie_chart_df.rename({'PassengerId':'Count of passengers'}, axis='columns', inplace=True)                    ## Rename PassengerId
plot = px.pie(data_frame=pie_chart_df, values='Count of passengers', names='Survived', title='Count of surviving passengers', template='seaborn')
col2.plotly_chart(plot)
## Boxplot of fare prices
plot = px.box(data_frame=filtered_df, x='Survived', y='Fare', color='Survived', title='Distribution of Fare across survival status', template='seaborn')
st.plotly_chart(plot)
##