import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  

st.write("""
In this project, we will study the factors that affect students' reading and math scores, including parental level of education, test preparation course, lunch, gender, and race/ethnicity	
""")
# Load the data from a CSV file
df = pd.read_csv("StudentsPerformance.csv")

#    First Graph
st.subheader("Parental Level of Education")
df1 = df.groupby("parental level of education")[["math score", "reading score"]].mean()
fig = plt.figure(figsize=(10, 6))
sns.scatterplot(x="math score", y="reading score", hue="parental level of education", data=df1)
plt.xlabel("Math Score")
plt.ylabel("Reading Score")
plt.title("Scatter Plot of Math Score vs. Reading Score (Colored by Parental Education)")
# Display the plot in Streamlit
st.pyplot(fig)
# Make some comments
st.write("""
We can see from the graph that students' math and reading scores are positively related to the parental level of education. The higher the parental level of education, the higher grades their kids can get. This quite makes sense since parents play a pretty important role in kids' education.
""")


#Second Graph
st.subheader("Test Preparation Course")
df2=df.groupby("test preparation course")[["math score", "reading score"]].mean()
st.write("Test preparation course & Scores:")
st.write(df2)
st.write(""" We can see from the table that the average math and reading scores are higher for the students who have completed the test preparation course.""")


#Third Graph
st.subheader("Lunch")
df3=df.groupby("lunch")[["math score", "reading score"]].mean()
data = {
    'lunch': list(df3.index)*2,
    'subject': ['math', 'math', 'reading', 'reading'],
    'score': list(df3['math score'])+list(df3['reading score'])
}
df3 = pd.DataFrame(data)
# Create a barplot of math and reading scores colored by lunch type
plt.figure(figsize=(8, 6))
sns.barplot(x="subject", y="score", hue="lunch", data=df3)
plt.xlabel('Subject')
plt.ylabel('Score')
plt.title('Barplot of Math and Reading Scores Colored by Lunch Type')
plt.legend(title='Lunch Type')
# Display the plot in Streamlit
st.pyplot(plt)
st.write(""" From the bar plot, we can see that the average math and reading scores are higher for students who have a standard lunch. This makes quite a bit of sense since when students receive more nutrients, they tend to perform better in their studies.""")


#Fourth Graph
# Create a figure with two subplots (one for math scores, one for reading scores)
st.subheader("Gender")
fig, axes = plt.subplots(1, 2, figsize=(12, 6))
# Plot the violin plot for math scores
sns.violinplot(x="gender", y="math score", data=df, palette="Set1", split=True, ax=axes[0])
axes[0].set_xlabel("Gender")
axes[0].set_ylabel("Math Score")
axes[0].set_title("Violin Plot of Math Scores by Gender")
# Plot the violin plot for reading scores
sns.violinplot(x="gender", y="reading score", data=df, palette="Set2", split=True, ax=axes[1])
axes[1].set_xlabel("Gender")
axes[1].set_ylabel("Reading Score")
axes[1].set_title("Violin Plot of Reading Scores by Gender")
# Adjust layout
plt.tight_layout()
# Display the plot in Streamlit
st.pyplot(fig)
st.write(""" From the violin plot, we can see that females tend to perform better than males in reading, while male students tend to outperform female students in math.""")


#Fifth graph
st.subheader("Race/ethnicity")
df5 = df.groupby("race/ethnicity")[["math score", "reading score"]].mean()
fig = plt.figure(figsize=(10, 6))
sns.scatterplot(x="math score", y="reading score", hue="race/ethnicity", data=df5)
plt.xlabel("Math Score")
plt.ylabel("Reading Score")
plt.title("Scatter Plot of Math Score vs. Reading Score (Colored by Race/ethnicity)")
# Display the plot in Streamlit
st.pyplot(fig)
# Make some comments
st.write("""
We can see from the graph that students of group E race/ethnicity perform the best in both Math and reading tests.
""")

#Final Part
st.subheader("Intersting Prediction")

# Define the options for the dropdown
options = ["Yes", "No"]

# Create a dropdown select box
selected_option = st.selectbox("Did you complete the Test Preparation courses?", options)

# Check the selected option and conditionally display a message
if selected_option == "Yes":
    st.write("You tend to get a better grade.")
else:
     st.write("Try to get more prepared so that you can get a better grade.")
