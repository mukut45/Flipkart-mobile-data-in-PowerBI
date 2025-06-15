#!/usr/bin/env python
# coding: utf-8

# In[23]:


import pandas as pd
df = pd.read_csv(r"D:\Information Technology\Flipkart data\Flipkart data\Flipkart_Mobiles.csv")
print(df.head())


# In[7]:


df.info()


# In[11]:


df.isnull().sum()


# In[13]:


df['Rating'] = df['Rating'].fillna(df['Rating'].mean()) # fill the missing values with its mean


# In[17]:


df.isnull().sum() # check here


# In[19]:


# Fill missing values in 'Memory' and 'Storage' columns with 'Unknown'
df['Memory'] = df['Memory'].fillna('Unknown')
df['Storage'] = df['Storage'].fillna('Unknown')


# In[21]:


df.isnull().sum() #  check here


# In[29]:


print(df.describe()) # describing the data here for statical analysis


# In[61]:


# Convert all string (object) columns to lowercase
df = df.apply(lambda col: col.str.lower() if col.dtype == 'object' else col)


# In[63]:


unique_brands = df['Brand'].unique()
unique_brands


# In[67]:


top_selling = (
    df.groupby(['Brand', 'Model'])['Selling Price']
    .sum()
    .reset_index()
    .sort_values(by='Selling Price', ascending=False)
)
print(top_selling.head(10))


# In[69]:


# Sort by Rating in descending order and get top 10
top_rated = (
    df.sort_values(by='Rating', ascending=False)
    [['Brand', 'Model', 'Rating']]
    .drop_duplicates()  # Optional: Avoid duplicate models
    .head(10)
)
print(top_rated)


# In[71]:


# Filter rows where Brand is 'google pixel' (case-insensitive)
google_pixel_models = df[df['Brand'].str.lower() == 'google pixel']['Model'].unique()

# Print the models
print(google_pixel_models)


# In[87]:


# model-rating pairs and sort by Rating descending
google_pixel_unique = (
    google_pixel_df[['Model', 'Rating']]
    .drop_duplicates()
    .sort_values(by='Rating', ascending=False)
)

print(google_pixel_unique)


# In[91]:


# model-rating pairs and sort by Rating descending
lg_unique = (
    lg_df[['Model', 'Rating']]
    .drop_duplicates()
    .sort_values(by='Rating', ascending=False)
)

print(lg_unique)


# In[93]:


# Filter for Nokia brand (case-insensitive)
nokia_df = df[df['Brand'] == 'nokia']

# Group by model and count the number of listings/sales
nokia_best_selling = (
    nokia_df.groupby('Model')
    .size()
    .reset_index(name='Count')
    .sort_values(by='Count', ascending=False)
)

# Display top 10 best-selling Nokia models
print(nokia_best_selling.head(10))


# In[97]:


# Filter for lenovo brand (case-insensitive)
lenovo_df = df[df['Brand'] == 'lenovo']

# Group by model and count the number of listings/sales
lenovo_best_selling = (
    lenovo_df.groupby('Model')
    .size()
    .reset_index(name='Count')
    .sort_values(by='Count', ascending=False)
)

# Display top 10 best-selling lenovo models
print(lenovo_best_selling.head(10))


# In[ ]:




