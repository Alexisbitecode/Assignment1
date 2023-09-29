import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # Add this import statement

st.subheader("First Graph")

# Load the data from a CSV file
df = pd.read_csv("StudentsPerformance.csv")
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

st.subheader("Second Table")

# Second table
df2=df.groupby("test preparation course")[["math score", "reading score"]].mean()
st.write("Test preparation course & Scores:")
st.write(df2)
st.write(""" We can see from the table that the average math and reading scores are higher for the students who have completed the test preparation course.""")
