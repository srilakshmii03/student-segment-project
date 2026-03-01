import streamlit as st
import pandas as pd

st.set_page_config(page_title="Student Segmentation Dashboard", layout="wide")

st.title("Student Segmentation & Course Recommendation")
st.write(
    "This dashboard segments learners based on engagement and spending behavior "
    "and provides personalized course recommendations using clustering."
)

df = pd.read_csv("data/final_user_segments.csv")

st.subheader("Learner Segments Overview")
st.dataframe(df)

st.subheader("Cluster Summary")
summary = df.groupby("cluster")[["total_courses", "total_spent"]].mean()
st.table(summary)

st.subheader("Select a Learner")
user_id = st.selectbox("Choose UserID", df["UserID"].unique())

user_data = df[df["UserID"] == user_id]
st.write(user_data)

cluster = int(user_data["cluster"].values[0])

st.subheader("Recommended Learning Path")
if cluster == 0:
    st.write("Advanced & Certification Courses")
elif cluster == 1:
    st.write("Intermediate & Skill-Building Courses")
else:
    st.write("Beginner-Friendly Starter Courses")