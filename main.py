import pandas as pd 
import numpy as np
#read from csv 
data=pd.read_csv('bank_marketing.csv')
client=data[["client_id","age","job","marital","education","credit_default","housing","loan"]]
campaign=data[['client_id',"campaign","month","day","duration","pdays","previous","poutcome","y"]]
economics=data[["client_id","emp_var_rate","cons_price_idx","euribor3m","nr_employed"]]

#step 2 cleaning data
#renaming
client=client.rename(columns={
    "client_id":"id"
})
campaign=campaign.rename(columns={
    "campaign":"number_contacts",
    "duration":"contact_duration",
    "previous":"previous_campaign_contacts",
    "y":"campaign_outcome",
    "poutcome":"previous_outcome"
})
economics=economics.rename(columns={
    "euribor3m":"euribor_three_months",
    "nr_employed":"number_employed"
})
#cleaning education column
client['education']=client['education'].str.replace(".","_")
client['education']=client['education'].replace('unknown',np.nan)
#remove period from job
client['job']=client['job'].str.replace(".","")
#changing failure/success to binary
campaign['campaign_outcome']=campaign['campaign_outcome'].map({"yes":1,"no":0})
campaign['previous_outcome']=campaign['previous_outcome'].map({"success":1,"failure":0,"nonexistent":np.nan})
campaign['campaign_id']=1
#adding last_contact_date (year-month-day)
campaign['month']=campaign['month'].str.capitalize()
campaign['year']="2022"
campaign['day']=campaign['day'].astype(str)
campaign['last_contact_date']=campaign['year']+"-"+campaign['month']+"-"+campaign['day']
campaign['last_contact_date']=pd.to_datetime(campaign['last_contact_date'],format='%Y-%b-%d')
#removing redundant data
campaign.drop(['year','month','day'],axis=1,inplace=True)

#step 3 saving dataFrames int csv files
#saving dataFrames as csv files
client.csv=client.to_csv(index=False)
campaign.csv=campaign.to_csv(index=False)
economics.csc=economics.to_csv(index=False)

print(client.head())