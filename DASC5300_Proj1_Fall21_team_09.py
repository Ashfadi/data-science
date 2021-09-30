#!/usr/bin/env python
# coding: utf-8

# # 1.Cleaning Data

# In[1]:


import pandas as pd
import numpy as np
df = pd.read_csv ('E:\Fall 2021\DASC 5300 (Foundation of Computing)\Project 1\Census Adult Data - dasc-5300-p1-census-adult.csv')
# using .replace for replacing some attributes to use them for our analysis
df1=df.replace({'United-States':'US'},regex=True)
df2=df1.replace({'Federal-gov':'Government'},regex=True)
df3=df2.replace({'Local-gov':'Government'},regex=True)
df4=df3.replace({'State-gov':'Government'},regex=True)
df5=df4.replace({'Self-emp-inc':'self-employed'},regex=True)
df6=df5.replace({'Self-emp-not-inc':'self-employed'},regex=True)
df7=df6.replace({'Preschool':'HS-grad'},regex=True)
df8=df7.replace({'1st-4th':'HS-grad'},regex=True)
df9=df8.replace({'5th-6th':'HS-grad'},regex=True)
df10=df9.replace({'7th-8th':'HS-grad'},regex=True)
df11=df10.replace({'9th':'HS-grad'},regex=True)
df12=df11.replace({'10th':'HS-grad'},regex=True)
df13=df12.replace({'11th':'HS-grad'},regex=True)
df14=df13.replace({'12th':'HS-grad'},regex=True)
df15=df14.replace({'Assoc-acdm':'Bachelors'},regex=True)
df16=df15.replace({'Assoc-voc':'Bachelors'},regex=True)
df17=df16.replace({'Some-college':'Bachelors'},regex=True)
df18=df17.replace({'Prof-school':'Masters'},regex=True)
df19=df18.replace("?",np.NaN)
df20=df19.dropna()
df20.to_csv('cleandata.csv',index=False)
df20


# # 1.1 Eliminated Lines

# In[2]:


df21 = df18[np.invert(df18.index.isin(df20.index))]
print (len(df21))
df21.to_csv('eliminatedlines.csv',index=False)
df21


# # 1.2 Discretizing gross income into two ranges with threshold 50K

# In[3]:


df22=df20[df20.gincome=='<=50K']
df22.to_csv('gincome_lessthanorequalto50K.csv',index=False)
df22


# In[4]:


df23=df20[df20.gincome=='>50K']
df23.to_csv('gincome_greaterthan50K.csv',index=False)
df23


# # 2. Sample Data

# In[5]:


df24 = pd.read_csv ('E:\Fall 2021\DASC 5300 (Foundation of Computing)\Project 1\cleandata.csv')
sample_data=df24.sample(175, random_state = 9201999)
sample_data.to_csv('sampledata.csv',index=False)
sample_data


# # 4.a Frequency Plot for different Age Groups for Sample Data

# In[6]:


import matplotlib.pyplot as plt
df25=pd.read_csv('E:\Fall 2021\DASC 5300 (Foundation of Computing)\Project 1\sampledata.csv',usecols=['Age'])
print (df25['Age'].value_counts(bins=[0,21,41,61,100]))
plt.hist(df25,bins=[0,21,41,61,100],ec='black')
plt.xlabel('Age Group')
plt.ylabel('Number of People')
plt.title('Number of People in different Age Groups')
ticks = [10,30,50,80]
labels = ["<21","21-40","41-60",">60"]
plt.xticks(ticks,labels)
plt.show()


# # 4.a Frequency Plot for different Age Groups for Cleaned Data

# In[7]:


df26=pd.read_csv('E:\Fall 2021\DASC 5300 (Foundation of Computing)\Project 1\cleandata.csv',usecols=['Age'])
print (df26['Age'].value_counts(bins=[0,21,41,61,100]))
plt.hist(df26,bins=[0,21,41,61,100],ec='black')
plt.xlabel('Age Group')
plt.ylabel('Number of People')
plt.title('Number of People in different Age Groups')
ticks = [10,30,50,80]
labels = ["<21","21-40","41-60",">60"]
plt.xticks(ticks,labels)
plt.show()


# # 4.b Pie Chart Showing Profession of people of Different Age Groups for Sample Data

# In[8]:


df27=pd.read_csv('E:\Fall 2021\DASC 5300 (Foundation of Computing)\Project 1\sampledata.csv')
df27['age_bins']=pd.cut(df27['Age'],bins=[0,20,40,60,100],labels=('<21','21-40','41-60','>60'))
print (df27.groupby('age_bins')['workclass'].value_counts())
people_1=[7,0]
workclass1=['Private','Government, self-employed, without-pay']
people_2=[75,19,4,0]
people_3=[38,11,9,0]
people_4=[5,0,7,0]
workclass=['Private','Government','self-employed','without-pay']
fig, axes = plt.subplots(2, 2, figsize=(16,8))
axes[0,0].pie(people_1,labels=workclass1,autopct='%0.0f%%')
axes[0,0].set(title='<21')
axes[0,1].pie(people_2,labels=workclass,autopct='%0.0f%%')
axes[0,1].set(title='21-40')
axes[1,0].pie(people_3,labels=workclass,autopct='%0.0f%%')
axes[1,0].set(title='41-60')
axes[1,1].pie(people_4,labels=workclass,autopct='%0.0f%%')
axes[1,1].set(title='>60')
axes[1, 0].legend(bbox_to_anchor=(0,0))


# # 4.b Pie Chart Showing Profession of people of Different Age Groups for Cleaned Data

# In[9]:


df28=pd.read_csv('E:\Fall 2021\DASC 5300 (Foundation of Computing)\Project 1\cleandata.csv')
df28['age_bins']=pd.cut(df28['Age'],bins=[0,20,40,60,100],labels=('<21','21-40','41-60','>60'))
print (df28.groupby('age_bins')['workclass'].value_counts())
people_1=[1812,118,66,2]
people_2=[12509,1939,1311,3]
people_3=[6913,1961,1720,2]
people_4=[1052,271,476,7]
workclass=['Private','Government','self-employed','without-pay']
fig, axes = plt.subplots(2, 2, figsize=(16,8))
axes[0,0].pie(people_1,labels=workclass,autopct='%0.2f%%')
axes[0,0].set(title='<21')
axes[0,1].pie(people_2,labels=workclass,autopct='%0.2f%%')
axes[0,1].set(title='21-40')
axes[1,0].pie(people_3,labels=workclass,autopct='%0.2f%%')
axes[1,0].set(title='41-60')
axes[1,1].pie(people_4,labels=workclass,autopct='%0.2f%%')
axes[1,1].set(title='>60')
axes[1, 0].legend(bbox_to_anchor=(0,0))


# # 4.c Grouping and Comparing Education for Males and Females for Sample Data

# In[80]:


df29=pd.read_csv('E:\Fall 2021\DASC 5300 (Foundation of Computing)\Project 1\sampledata.csv')
df29['age_bins']=pd.cut(df29['Age'],bins=[0,20,40,60,100],labels=('<21','21-40','41-60','>60'))
print (df29.groupby(['age_bins','sex'])['education'].value_counts())
X=["HS-grad","Bachelors","Masters","Doctorate"]
male1=[4,2,0,0]
female1=[1,0,0,0]
male2=[33,31,4,0]
female2=[10,19,1,0]
male3=[19,15,4,0]
female3=[7,11,1,1]
male4=[5,3,1,0]
female4=[3,0,0,0]
X_axis=np.arange(len(X))
fig, axes = plt.subplots(2, 2, figsize=(16,10))
axes[0,0].bar(X_axis-0.2,male1,0.4,label='Male')
axes[0,0].bar(X_axis+0.2,female1,0.4,label='Female')
axes[0,0].set(title='<21',xlabel='Education',ylabel='Total Number of People')
axes[0,0].set_xticks(X_axis)
axes[0,0].set_xticklabels(X)
axes[0,1].bar(X_axis-0.2,male2,0.4,label='Male')
axes[0,1].bar(X_axis+0.2,female2,0.4,label='Female')
axes[0,1].set(title='21-40',xlabel='Education',ylabel='Total Number of People')
axes[0,1].set_xticks(X_axis)
axes[0,1].set_xticklabels(X)
axes[1,0].bar(X_axis-0.2,male3,0.4,label='Male')
axes[1,0].bar(X_axis+0.2,female3,0.4,label='Female')
axes[1,0].set(title='41-60',xlabel='Education',ylabel='Total Number of People')
axes[1,0].set_xticks(X_axis)
axes[1,0].set_xticklabels(X)
axes[1,1].bar(X_axis-0.2,male4,0.4,label='Male')
axes[1,1].bar(X_axis+0.2,female4,0.4,label='Female')
axes[1,1].set(title='>60',xlabel='Education',ylabel='Total Number of People')
axes[1,1].set_xticks(X_axis)
axes[1,1].set_xticklabels(X)
axes[1, 0].legend(bbox_to_anchor=(0,0))
plt.show()


# # 4.c Grouping and Comparing Education for Males and Females for Cleaned Data

# In[81]:


df30=pd.read_csv('E:\Fall 2021\DASC 5300 (Foundation of Computing)\Project 1\cleandata.csv')
df30['age_bins']=pd.cut(df30['Age'],bins=[0,20,40,60,100],labels=('<21','21-40','41-60','>60'))
print (df30.groupby(['age_bins','sex'])['education'].value_counts())
X=['HS-grad','Bachelors','Masters','Doctorate']
male1=[744,302,1,0]
female1=[558,392,1,0]
male2=[4795,5080,587,86]
female2=[1921,3005,259,29]
male3=[3168,3350,872,169]
female3=[1401,1292,301,43]
male4=[648,426,113,39]
female4=[346,190,35,9]
X_axis=np.arange(len(X))
fig, axes = plt.subplots(2, 2, figsize=(16,10))
axes[0,0].bar(X_axis-0.2,male1,0.4,label='Male')
axes[0,0].bar(X_axis+0.2,female1,0.4,label='Female')
axes[0,0].set(title='<21',xlabel='Education',ylabel='Total Number of People')
axes[0,0].set_xticks(X_axis)
axes[0,0].set_xticklabels(X)
axes[0,1].bar(X_axis-0.2,male2,0.4,label='Male')
axes[0,1].bar(X_axis+0.2,female2,0.4,label='Female')
axes[0,1].set(title='21-40',xlabel='Education',ylabel='Total Number of People')
axes[0,1].set_xticks(X_axis)
axes[0,1].set_xticklabels(X)
axes[1,0].bar(X_axis-0.2,male3,0.4,label='Male')
axes[1,0].bar(X_axis+0.2,female3,0.4,label='Female')
axes[1,0].set(title='41-60',xlabel='Education',ylabel='Total Number of People')
axes[1,0].set_xticks(X_axis)
axes[1,0].set_xticklabels(X)
axes[1,1].bar(X_axis-0.2,male4,0.4,label='Male')
axes[1,1].bar(X_axis+0.2,female4,0.4,label='Female')
axes[1,1].set(title='>60',xlabel='Education',ylabel='Total Number of People')
axes[1,1].set_xticks(X_axis)
axes[1,1].set_xticklabels(X)
axes[1, 0].legend(bbox_to_anchor=(0,0))
plt.show()


# # 4.d Top 5 Occupations for Sample Data

# In[34]:


df31=pd.read_csv('E:\Fall 2021\DASC 5300 (Foundation of Computing)\Project 1\sampledata.csv')
df31['Occupation'].value_counts().head(5)


# # 4.d Top 5 Occupations for Cleaned Data

# In[35]:


df32=pd.read_csv('E:\Fall 2021\DASC 5300 (Foundation of Computing)\Project 1\cleandata.csv')
df32['Occupation'].value_counts().head(5)

