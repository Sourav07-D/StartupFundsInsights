import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.set_page_config(layout='wide',page_title='Startup Analysis')
df=pd.read_csv('startup_cleaned.csv')
df['date']=pd.to_datetime(df['date'],errors='coerce')
df['year'] = df['date'].dt.year
df['month']=df['date'].dt.month

def load_overall_analysis():
    st.title("Overall Analysis")
    #total invested amount
    total=round(df['amount'].sum())
    #max amount infused in a startup
    max=df.groupby('startup')['amount'].max().sort_values(ascending=False).head(1).values[0]
    #avg invested amount
    avg=round(df.groupby('startup')['amount'].sum().mean())
    #total no of startups
    num_startup=df['startup'].nunique()
    col1,col2,col3,col4=st.columns(4)
    with col1:
        st.metric('Total', str(total) + 'Cr')
    with col2:
        st.metric('Max', str(max) + 'Cr')
    with col3:
        st.metric('Avg', str(avg) + 'Cr')
    with col4:
        st.metric("Funded Startup",num_startup)

    st.header("MOM Graph")
    selected_option=st.selectbox('Select Type',['Total','Count'])
    if selected_option=='Total':
        temp_df = df.groupby(['year', 'month'])['amount'].sum().reset_index()
    else:
        temp_df = df.groupby(['year', 'month'])['amount'].count().reset_index()

    temp_df['x-axis'] = temp_df['month'].astype('str') + '-' + temp_df['year'].astype('str')
    fig4, ax4 = plt.subplots();
    ax4.plot(temp_df['x-axis'],temp_df['amount'])
    st.pyplot(fig4)

def load_investor_details(investor):
    st.title(investor)
    #load the last 5 investment of the investor
    last_5df=df[df['investors'].str.contains(investor)].head()[['date','startup','vertical','city','round','amount']]
    st.subheader("Most Recent Investments")
    st.dataframe(last_5df)

    col1,col2=st.columns(2)
    with col1:
        # Biggest investments
        big_ser = df[df['investors'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(
            ascending=False).head()
        st.subheader("Biggest Investments")
        # st.dataframe(big_ser)
        fig, ax = plt.subplots();
        ax.bar(big_ser.index, big_ser.values)
        st.pyplot(fig)

    with col2:
        vertical_ser=df[df['investors'].str.contains(investor)].groupby('vertical')['amount'].sum()
        st.subheader("Sectors Invested in")

        fig1, ax1 = plt.subplots();
        ax1.pie(vertical_ser,labels=vertical_ser.index,autopct="%0.01f%%")
        st.pyplot(fig1)

    col3, col4 = st.columns(2)
    with col3:
        stage_ser=df[df['investors'].str.contains(investor)].groupby('round')['amount'].sum()
        st.subheader("Stage ")

        fig2, ax2= plt.subplots();
        ax2.pie(stage_ser,labels=stage_ser.index,autopct="%0.01f%%")
        st.pyplot(fig2)

    with col4:
        city_ser=df[df['investors'].str.contains(investor)].groupby('city')['amount'].sum()
        st.subheader(" Available City")

        fig3, ax3 = plt.subplots();
        ax3.pie(city_ser,labels=city_ser.index,autopct="%0.01f%%")
        st.pyplot(fig3)


    year_ser=df[df['investors'].str.contains(investor)].groupby('year')['amount'].sum()
    st.subheader("YOR Investment")

    fig4, ax4 = plt.subplots();
    ax4.plot(year_ser.index,year_ser.values)
    st.pyplot(fig4)


st.dataframe(df)
st.sidebar.title("Startup Funding Analysis")
option=st.sidebar.selectbox("Select One",["Overall Analysis","Startup" ,"Investor"])

if option=="Overall Analysis":
    load_overall_analysis()
elif option=="Startup":
    st.sidebar.selectbox('Select Startup',sorted(df['startup'].unique().tolist()))
    btn1=st.sidebar.button("Find Startup Details")
    st.title("Startup Analysis")
elif option=='Investor':
    selected_investor=st.sidebar.selectbox('Select Investors',sorted(set(df['investors'].str.split(',').sum())))
    btn2 = st.sidebar.button("Find Investors Details")
    if btn2:
        load_investor_details(selected_investor)

    st.title("Investor Analysis")
else:
    pass

