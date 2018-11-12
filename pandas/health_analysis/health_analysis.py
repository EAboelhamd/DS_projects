
# coding: utf-8

# In[152]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[148]:


benefits = pd.read_csv('./data/BenefitsCostSharing.csv',parse_dates=['BusinessYear'])


# In[49]:


#benefits.info()


# In[149]:


benefits.head()
#del benefits[['CoinsInnTier2','CopayInnTier2'.'Exclusions','MinimumStay']]


# In[5]:


benefits.shape


# ## Clean the data (Delete the coulmns) 

# In[150]:


print('Row is Null',benefits['CoinsInnTier2'].isnull().sum())
# Delete this columns becouse all data NaN
del benefits['CoinsInnTier2']
print('Done Delete')


# In[151]:


print('Row is Null',benefits['CopayInnTier2'].isnull().sum())
# Delete this columns becouse all data NaN
del benefits['CopayInnTier2']
print('Done Delete')


# In[153]:


print('Row is Null',benefits['Exclusions'].isnull().sum())
# Delete this columns becouse all data NaN
del benefits['Exclusions']
print('Done Delete')


# In[154]:


print('Row is Null',benefits['MinimumStay'].isnull().sum())
# Delete this columns becouse all data NaN
del benefits['MinimumStay']
print('Done Delete')


# In[155]:


benefits.drop_duplicates()
print('Done'+ ''+ 'drop_duplicates')


# In[156]:


benefits.shape


# In[157]:


benefits.columns


# In[76]:


#benefits['BenefitName'].unique().tolist()


# In[158]:


print('Max_BenefitName_value:- ',benefits['BenefitName'].value_counts().max())
print('Max_BenefitName:- ',benefits['BenefitName'].value_counts().index.max())
print('unique_beN_Values:- ',benefits['BenefitName'].value_counts().index.unique())
print('unique_beN_Values_number:- ',benefits['BenefitName'].value_counts().unique())


# In[159]:


print('type of BusinessYear:- ',benefits['BusinessYear'].dtype)
print(benefits['BusinessYear'].value_counts().index.unique())
print('All record all 2014:- ',benefits['BusinessYear'].value_counts().unique())


# In[160]:


#print('unique_beN_Values:- ',benefits['BenefitName'].value_counts().index.unique())
plt.title('Benefists_Name _2014')
plt.ylabel('Benefists_values')
#plt.pie(benefits['BenefitName'].value_counts().unique())
plt.plot(benefits['BenefitName'].value_counts().unique(),'r')

#plt.hist(benefits['BenefitName'].value_counts().index.unique())
#add


# In[161]:


benefits.groupby('BenefitName').BenefitName.count()


# In[125]:


plt.title('Benefists_Name _2014')
plt.ylabel('Benefists_values')
plt.plot(benefits.groupby('BenefitName').BenefitName.count(),'g')


# In[130]:


plt.plot(benefits.groupby('BenefitName').BenefitName.count().unique())


# In[162]:


print('Sum row is unll:- ',benefits['StateCode'].isnull().sum())
benefits['StateCode'].fillna(method='ffill')
print('Done Fill!!')


# In[163]:


benefits['StateCode'].value_counts().index.unique()


# In[164]:


benefits.groupby('StateCode').StateCode.count()


# In[137]:


benefits.describe()


# In[168]:


print('Sum row is unll:- ',benefits['BenefitName'].isnull().sum())
benefits['BenefitName'].fillna(method='ffill')
print('Done Fill!!')


# In[179]:


#benefits['CoinsInnTier1'].fillna(method='ffill')
print(benefits['CoinsInnTier1'].isnull().sum())
print(benefits['CoinsInnTier1'].dtype)
benefits['CoinsInnTier1'].to_numeric

benefits['CoinsInnTier1'].fillna(method='backfill')
print(benefits['CoinsInnTier1'].isnull().sum())

#print('done', benefits.isnull().any())

