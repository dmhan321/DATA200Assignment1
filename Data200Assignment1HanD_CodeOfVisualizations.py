"""
This Streamlit App includes five visualizations, 
with Bart Chart(1) and Box Plot(3) containing interactive dropdown options, 
and Scatter Plot(2) containing an interactive slider element.
"""

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# Streamlit App
st.title("Visualizations with Interactive Elements")

data = pd.read_csv(r"Fish.csv")
df_fish = pd.DataFrame(data)
features = df_fish.columns[1:]



# Visualization 1: Bar Chart
st.subheader("1: Bar Chart")

# Interactive element: Dropdown for the features
selected_option = st.selectbox("Select a feature", features)

if selected_option:
    df = df_fish.groupby('Species')[selected_option].mean().reset_index(name='mean')
    #st.dataframe(df)
    fig, ax = plt.subplots()
    ax.bar(df['Species'], df['mean'] )
    plt.xlabel("Species")
    plt.ylabel("Average {}".format(selected_option))
    plt.title("Bar Chart of Average {} by Species".format(selected_option))
    st.pyplot(fig)

    st.write("Observation:")
    if selected_option == 'Weight':
        st.write("Pike has the highest average weight and Smelt has the lowest.")
    elif selected_option == 'Length1':
        st.write("Pike has the highest average length1 and Smelt has the lowest.")
    elif selected_option == 'Length2':
        st.write("Pike has the highest average length2 and Smelt has the lowest.")
    elif selected_option == 'Length3':
        st.write("Pike has the highest average length3 and Smelt has the lowest.") 
    elif selected_option == 'Height':
        st.write("Bream has the highest average height and Smelt has the lowest.")
    elif selected_option == 'Width':
        st.write("Whitefish has the highest average width and Smelt has the lowest.")       



# Visualization 2: Scatter Plot with Slider
st.subheader("2: Scatter Plot")

# Interactive element: Slider for the number of data points
num_points = st.slider("Select the Number of Data Points you want to display", 1, 158, 100)

fig, ax = plt.subplots()
ax.scatter(df_fish['Weight'].head(num_points), df_fish['Width'].head(num_points))
plt.xlabel('Weight')
plt.ylabel('Width')
plt.title('Weight and Width of fishes with {} Data Points'.format(num_points))
st.pyplot(fig)

st.write("Observation:")
st.write("There is a positive correlation between the fish weight and width.")




# Visualization 3: Box Plot
st.subheader("3: Box Plot")

# Interactive element: Dropdown for the features
selected_feature = st.selectbox("Select a feature to display", features)
df_Perch = df_fish[df_fish["Species"] == 'Perch']

if selected_feature:
    fig, ax = plt.subplots()
    ax.boxplot(df_Perch[selected_feature])
    plt.ylabel('{}'.format(selected_feature))
    plt.title('Box plot of Perch {}'.format(selected_feature))
    st.pyplot(fig)

st.write("Observation:")
st.write("The distribution of Perch {} is negatively skewed.".format(selected_feature))



# Visualization 4: Histogram
st.subheader("4: Histogram")  
st.dataframe(df_Perch['Weight'])
fig, ax = plt.subplots()
ax.hist(df_Perch['Weight'])

plt.title('Weight of Perch')
st.pyplot(fig)

st.write("Observation:")
st.write("The majority of Perch weighed between 0 and 320")



# Visualization 5: Pie Chart
st.subheader("5: Pie Chart")
fig, ax = plt.subplots()
species = df_fish.groupby('Species', axis=0).count()
plt.title('Distribution of fish by species')
labels = species.index
ax.pie(species['Weight'],labels=labels)
st.pyplot(fig)

st.write("Observation:")
st.write("Perch had the highest proportion and Whitefish had the lowest.")

# Visualization 6:
st.subheader("Detailed Data View")
st.dataframe(df_fish)