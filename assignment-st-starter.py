# import packages
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# show the title
st.title('Titanic App by Yufei Han')

# read csv and show the dataframe
df = pd.read_csv('train.csv')
df

# create a figure with three subplots, size should be (15, 5)
fig, ax = plt.subplots(1,3,figsize=(15,5))

# show the box plot for ticket price with different classes
# you need to set the x labels and y labels
#1
ax[0].boxplot(df.Fare[df['Pclass'] == 1])
ax[0].set_xticklabels(['Fare'])
ax[0].set_xlabel('PClass = 1')
#2
ax[1].boxplot(df.Fare[df['Pclass'] == 2])
ax[1].set_xticklabels(['Fare'])
ax[1].set_xlabel('PClass = 2')
#3
ax[2].boxplot(df.Fare[df['Pclass'] == 3])
ax[2].set_xticklabels(['Fare'])
ax[2].set_xlabel('PClass = 3')

# a sample diagram is shown below

