#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly.graph_objects as go
fig = go.Figure(data=go.Bar(y=[2, 3, 1]))
fig.show()


# In[6]:


import plotly.express as px
import numpy as np
import pandas as pd
from jupyter_dash import JupyterDash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output


# In[7]:


import plotly.express as px
import numpy as np
import pandas as pd
from jupyter_dash import JupyterDash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output


# In[8]:


data = pd.read_excel("Blue_Bucket_data_2015-Aug2021.xlsx")
data


# In[10]:


#start of pie charts code
import numpy as np

import pandas as pd

import plotly.express as px
Tides_Data= pd.read_csv("TIDES_2015-2021.csv")
Blue_Bucket_Data = pd.read_excel("Blue_Bucket_data_2015-Aug2021.xlsx")

Blue_Bucket_Data_cleaned = Blue_Bucket_Data.drop(columns=["Unnamed: 67", "Unnamed: 68"])

Tides_Data["Month"] = [float("NaN") for element in range(0,27344)]

Tides_Data["Year"] = [float("NaN") for element in range(0,27344)]

Merged_Data = Tides_Data.append(Blue_Bucket_Data_cleaned, sort=False)

trash_types = Merged_Data.iloc[:,14:64]
dataf = {'Type': trash_types.columns, 'Sum': trash_types.sum()}
trash_quantity = pd.DataFrame(dataf)
sortedTrash = trash_quantity.sort_values(by = 'Sum', ascending = False)
topNine = sortedTrash[:9]

otherTrash = Merged_Data.iloc[:,25:64]
dataf = {'Type': otherTrash.columns, 'Sum': otherTrash.sum()}
otherTrash = pd.DataFrame(dataf)
otherSum = otherTrash.sum()['Sum']

topTen = topNine.append({'Type': "Other", 'Sum': otherSum}, ignore_index = True)
figTopTen = px.pie(topTen, values="Sum", names="Type", title="Top 10 types of trash collected")
#, color_discrete_sequence=px.colors.sequential.blues
figTopTen.show()


# In[11]:


data2 = data.sort_values(by="Cleanup Date")
plot = px.line(data2, x="Cleanup Date", y="Cigarette Butts", title="Time Series of Cigarette Butts")
plot.show()


# In[12]:


#single use plastics
import pandas as pd
import numpy as np
from datetime import datetime
datag = pd.read_csv("Tides_and_Blue_Bucket_Data.csv")
datag['Cleanup Timestamp'] = pd.to_datetime(datag['Cleanup Date'], format="%Y-%m-%d %H:%M:%S")
dff = datag.groupby('Cleanup Timestamp').agg('sum')
dff.reset_index(level=0, inplace=True)
dff['Single Use Plastics'] = dff['Cigarette Butts'] + dff['Food Wrappers (candy, chips, etc.)'] + dff['Take Out/Away Containers (Plastic)'] + dff['Bottle Caps (Plastic)'] + dff['Lids (Plastic)'] + dff['Straws, Stirrers'] + dff['Beverage Bottles (Plastic)'] + dff['Grocery Bags (Plastic)'] + dff['Other Plastic Bags'] + dff['Cups, Plates (Plastic)'] + dff['Fishing Net & Pieces'] + dff['Fishing Line (1 yard/meter = 1 piece)'] + dff['6-Pack Holders'] + dff['Balloons'] + dff['Beverages Sachets'] + dff['Cigarette Lighters'] + dff['Tobacco Packaging/Wrap'] + dff['Diapers'] + dff['Tampons/Tampon Applicators'] + dff['Other Plastic/Foam Packaging'] + dff['Other Plastic Bottles (oil, bleach, etc.)'] + dff['Gloves & Masks (PPE)']
dff['Cumulative Single Use Plastics'] = dff['Single Use Plastics'].cumsum()
import plotly.express as px

figsup = px.line(dff, x="Cleanup Timestamp", y="Cumulative Single Use Plastics", title="Cumulative single use plastics collected over time")

per_month = dff.set_index('Cleanup Timestamp').groupby(pd.Grouper(freq='M'))['Single Use Plastics'].sum()

x = per_month.index
y = per_month.values

dfg = pd.DataFrame({'Month': x, 'Single Use Plastics': y})

figsu = px.line(dfg, x='Month', y='Single Use Plastics', title='Single use plastics collected over time')


# In[13]:


total_pounds = round(sum(data['Pounds']), 2)
total_trips = len(data)


# In[15]:


import plotly.graph_objects as go # or plotly.express as px
#fig = go.Figure() # or any Plotly Express function e.g. px.bar(...)
# fig.add_trace( ... )
# fig.update_layout( ... )

import dash
from dash import dcc
from dash import html

#             html.H3('Ocean trash dashboard', style={'margin-bottom': '0px', 'color': 'white'})

app = dash.Dash()
app.layout = html.Div([
    html.Div([
            html.H6(children='Title',
                    style={
                        'textAlign': 'center',
                        'color': 'white'}
                    ),
 
            html.P("Pacifica Beach Coalition: Ocean Trash Dashboard",
                   style={
                       'textAlign': 'center',
                       'color': 'black',
                       'fontSize': 50}
                   )], className="total_pounds",
        ),
        #])
    #], className='title', id = 'title1'),
    html.Div([
            html.H6(children='Total pounds of trash collected',
                    style={
                        'textAlign': 'center',
                        'color': 'white'}
                    ),
 
            html.P("Total pounds of trash collected: " + f"{total_pounds}",
                   style={
                       'textAlign': 'center',
                       'color': 'blue',
                       'fontSize': 20}
                   )], className="total_pounds",
        ),
    html.Div([
            html.H6(children='Total trips taken',
                    style={
                        'textAlign': 'center',
                        'color': 'white'}
                    ),
 
            html.P("Total trips taken: " + f"{total_trips}",
                   style={
                       'textAlign': 'center',
                       'color': 'blue',
                       'fontSize': 20}
                   )], className="total_trips",
        ),
    html.Div([
        dcc.Graph(figure=plot)
    ], className='plot', id='plot1'),
    html.Div([
        dcc.Graph(figure=figTopTen)
    ], className='figTopTen', id='plot2'),
    html.Div([
        dcc.Graph(figure=figsu)
    ], className='figsu', id='plot4'),
    html.Div([
        dcc.Graph(figure=figsup)
    ], className='figsup', id='plot3')
])


# In[ ]:


app.run_server(debug=True, use_reloader=False)


# In[ ]:





# In[ ]:




