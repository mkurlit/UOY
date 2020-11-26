#%%
## Ex 2
import pandas as pd 
sales = pd.read_csv('SalesData.csv')
P2 = sales.loc['P2',['Nov-18','Feb-19','Mar-19']]
B8 = sales.loc['B8', ['Nov-18', 'Feb-19', 'Mar-19']]
london = sales.loc[['L3','L2'],['Oct-18','Nov-18', 'Dec-18']]

ny = sales.loc[['N6','N4'],:].apply(lambda x: (max(x['N6'],x['N4']),x.idxmax()), \
    axis = 0,result_type = 'reduce').sort_values(ascending = False)[:3]

total_lowest = sales.apply(lambda x: (max(x),x.idxmax()), \
    axis = 0,result_type = 'reduce').sort_values(ascending = True)[0]

# %%
## Ex 3
increases = sales / sales.apply(lambda x: x.mean(), axis = 1, result_type = 'broadcast')
tops = increases.apply(lambda x: (max(x),x.idxmax()), axis = 1).sort_values(ascending = False)[[0,-1]]
avgs = increases.apply(lambda x: x.mean(), axis = 0).sort_values(ascending = False)[[0,-1]]