import numpy as np

def get_medalTally(eve, yr, country):
    medalDf = eve.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
    f = 0
    if yr == 'Overall' and country == 'Overall':
        temp = medalDf
    if yr == 'Overall' and country != 'Overall':
        f = 1
        temp = medalDf[medalDf['region'] == country]
    if yr != 'Overall' and country == 'Overall':
        temp = medalDf[medalDf['Year'] == int(yr)]
    if yr != 'Overall' and country != 'Overall':
        temp = medalDf[(medalDf['Year'] == int(yr)) & (medalDf['region'] == country)]

    if f == 1:
        x = temp.groupby('Year').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Year').reset_index()
    else:
        x = temp.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Gold',
                                                                                   ascending=False).reset_index()
    x['total'] = x['Gold'] + x['Silver'] + x['Bronze']
    return x

def medal_tally(eve):
    medalTally = eve.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
    medalTally = medalTally.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Gold',ascending=False).reset_index()
    medalTally['total'] = medalTally['Gold'] + medalTally['Silver'] + medalTally['Bronze']

    return medalTally

def countryYear_list(eve):
    yrs = eve['Year'].unique().tolist()
    yrs.sort()
    yrs.insert(0, 'Overall')
    country = np.unique(eve['region'].dropna().values).tolist()
    country.sort()
    country.insert(0, 'Overall')
    return yrs, country

def data_overtime(eve,col):
    nations_over_time = eve.drop_duplicates(['Year', col])['Year'].value_counts().reset_index().sort_values('Year')
    nations_over_time.rename(columns={'Year': 'Editions', 'count': col}, inplace=True)
    return nations_over_time

def most_successful(eve,sport):
    temp=eve.dropna(subset=['Medal'])
    if sport!='Overall':
        temp=temp[temp['Sport']==sport]
    x=temp['Name'].value_counts().reset_index().head(15).merge(eve,on='Name',how='left')[['Name','count','Sport','region']].drop_duplicates('Name')
    x.rename(columns={'count':'Medals'},inplace=True)
    return x

def yearwise_medaltally(eve,country):
    temp=eve.dropna(subset=['Medal'])
    temp.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'], inplace=True)
    new = temp[temp['region'] == country]
    final = new.groupby('Year').count()['Medal'].reset_index()

    return final

def countryEvent_heatmap(eve,country):
    temp = eve.dropna(subset=['Medal'])
    temp.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'], inplace=True)
    new = temp[temp['region'] == country]
    pt=new.pivot_table(index='Sport', columns='Year', values='Medal', aggfunc='count').fillna(0).astype(int)
    return pt

def most_successful_countrywise(eve,country):
    temp=eve.dropna(subset=['Medal'])
    temp=temp[temp['region']==country]
    x=temp['Name'].value_counts().reset_index().head(10).merge(eve,on='Name',how='left')[['Name','count','Sport']].drop_duplicates('Name')
    x.rename(columns={'count':'Medals'},inplace=True)
    return x

def weight_v_height(eve,sport):
    athlete = eve.dropna(subset=['Name', 'region'])
    athlete['Medal'].fillna('No Medal', inplace=True)
    if sport!='Overall':
        temmp = athlete[athlete['Sport'] == sport]
        return temmp
    else:
        return athlete

def mvf(eve):
    athlete = eve.dropna(subset=['Name', 'region'])
    m = athlete[athlete['Sex'] == 'M'].groupby('Year').count()['Name'].reset_index()
    w = athlete[athlete['Sex'] == 'F'].groupby('Year').count()['Name'].reset_index()
    f = m.merge(w, on='Year')
    f.rename(columns={'Name_x': 'Male', 'Name_y': 'Female'}, inplace=True)
    f.fillna(0, inplace=True)
    return f