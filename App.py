import streamlit as st
import pandas as pd
import preprocessor,helper
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff

eve=pd.read_csv('athlete_events.csv')
reg=pd.read_csv('noc_regions.csv')

eve=preprocessor.preprocess(eve,reg)
st.sidebar.title('Olympics Analysis')

user_menu=st.sidebar.radio(
    'Select an option',
    ('Medal Tally','Overall Analysis','Country-wise Analysis','Athlete-wise Analysis')
)

if user_menu=='Medal Tally':
    st.sidebar.header('Medal Tally')
    yrs,country=helper.countryYear_list(eve)

    selected_yr=st.sidebar.selectbox('Select Year',yrs)
    selected_country = st.sidebar.selectbox('Select Country', country)

    medal_tally=helper.get_medalTally(eve,selected_yr,selected_country)
    if selected_yr=='Overall' and selected_country=='Overall':
        st.title('Overall Tally')
    if selected_yr!='Overall' and selected_country=='Overall':
        st.title('Medal Tally in '+str(selected_yr)+' Olympics')
    if selected_yr=='Overall' and selected_country!='Overall':
        st.title(selected_country+' Overall Performance')
    if selected_yr!='Overall' and selected_country!='Overall':
        st.title(selected_country+' performance in '+ str(selected_yr)+' Olympics')
    st.dataframe(medal_tally)

if user_menu=='Overall Analysis':
    editions=eve['Year'].unique().shape[0]
    cities=eve['City'].unique().shape[0]
    sports=eve['Sport'].unique().shape[0]
    events=eve['Event'].unique().shape[0]
    athletes=eve['Name'].unique().shape[0]
    nations=eve['region'].unique().shape[0]

    st.title('Top Statistics')
    col1,col2,col3=st.columns(3)
    with col1:
        st.header('Editions')
        st.title(editions)
    with col2:
        st.header('Hosts')
        st.title(cities)
    with col3:
        st.header('Sports')
        st.title(sports)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header('Events')
        st.title(events)
    with col2:
        st.header('Nations')
        st.title(nations)
    with col3:
        st.header('Athletes')
        st.title(athletes)

    nations_over_time=helper.data_overtime(eve,'region')
    fig = px.line(nations_over_time, x='Editions', y='region')
    st.title('Participating Nations over the years')
    st.plotly_chart(fig)

    events_over_time = helper.data_overtime(eve, 'Event')
    fig = px.line(events_over_time, x='Editions', y='Event')
    st.title('Events over the years')
    st.plotly_chart(fig)

    athletes_over_time = helper.data_overtime(eve, 'Name')
    fig = px.line(athletes_over_time, x='Editions', y='Name')
    st.title('Athletes over the years')
    st.plotly_chart(fig)

    st.title('No of events over time [Every sport]')
    fig,ax=plt.subplots(figsize=(10,10))
    x = eve.drop_duplicates(['Year', 'Sport', 'Event'])
    ax=sns.heatmap(x.pivot_table(index='Sport', columns='Year', values='Event', aggfunc='count').fillna(0).astype(int),
                annot=True)
    st.pyplot(fig)

    st.title('Most Successful Athletes')
    sport_list=eve['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0,'Overall')
    selected_sport=st.selectbox('Select a Sport',sport_list)
    x=helper.most_successful(eve,selected_sport)
    st.table(x)

if user_menu=='Country-wise Analysis':
    st.sidebar.title('Country wise Analysis')

    country_list=eve['region'].dropna().unique().tolist()
    country_list.sort()
    selected_country=st.sidebar.selectbox('Select a Country',country_list)


    countrydf=helper.yearwise_medaltally(eve,selected_country)
    fig = px.line(countrydf, x='Year', y='Medal')
    st.title('Medal Tally of '+selected_country +' over the years')
    st.plotly_chart(fig)

    st.title(selected_country +' excels in following sports')
    pt=helper.countryEvent_heatmap(eve,selected_country)
    fig,ax=plt.subplots(figsize=(10,10))
    ax=sns.heatmap(pt,annot=True)
    st.pyplot(fig)

    st.title('Top 10 Athelets of '+selected_country)
    top10=helper.most_successful_countrywise(eve,selected_country)
    st.table(top10)

if user_menu=='Athlete-wise Analysis':
    athlete = eve.dropna(subset=['Name', 'region'])
    x1 = athlete['Age'].dropna()
    x2 = athlete[athlete['Medal'] == 'Gold']['Age'].dropna()
    x3 = athlete[athlete['Medal'] == 'Silver']['Age'].dropna()
    x4 = athlete[athlete['Medal'] == 'Bronze']['Age'].dropna()
    fig = ff.create_distplot([x1, x2, x3, x4], ['Overall Age', 'Gold Medalist', 'Silver Medalist', 'Bronze Medalist'],
                             show_hist=False, show_rug=False)
    fig.update_layout(autosize=False, width=1000, height=600)
    st.title('Distribution of Age')
    st.plotly_chart(fig)

    x = []
    name = []
    famous_sports = ['Basketball', 'Judo', 'Football', 'Tug-Of-War', 'Athletics',
                     'Swimming', 'Badminton', 'Sailing', 'Gymnastics',
                     'Art Competitions', 'Handball', 'Weightlifting', 'Wrestling',
                     'Water Polo', 'Hockey', 'Rowing', 'Fencing',
                     'Shooting', 'Boxing', 'Taekwondo', 'Cycling', 'Diving', 'Canoeing',
                     'Tennis', 'Golf', 'Softball', 'Archery',
                     'Volleyball', 'Synchronized Swimming', 'Table Tennis', 'Baseball',
                     'Rhythmic Gymnastics', 'Rugby Sevens',
                     'Beach Volleyball', 'Triathlon', 'Rugby', 'Polo', 'Ice Hockey']
    for spr in famous_sports:
        temp = athlete[athlete['Sport'] == spr]
        x.append(temp[temp['Medal'] == 'Gold']['Age'].dropna())
        name.append(spr)

    fig = ff.create_distplot(x, name, show_hist=False, show_rug=False)
    fig.update_layout(autosize=False, width=1000, height=600)
    st.title('Distribution of Age wrt Sports[Gold Medalist]')
    st.plotly_chart(fig)

    st.title('Height vs Weight')
    sport_list = eve['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, 'Overall')
    selected_sport = st.selectbox('Select a Sport', sport_list)
    temmp=helper.weight_v_height(eve,selected_sport)
    fig,ax=plt.subplots()
    ax=sns.scatterplot(x=temmp['Weight'],y=temmp['Height'],hue=temmp['Medal'],style=temmp['Sex'],s=60)
    st.pyplot(fig)

    st.title('Men vs Women Participation over the years')
    f=helper.mvf(eve)
    fig = px.line(f, x='Year', y=['Male', 'Female'])
    fig.update_layout(autosize=False, width=1000, height=600)
    st.plotly_chart(fig)