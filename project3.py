import streamlit as st
import pandas as pd
import plotly.express as px

# Title
st.title("🎓 Student Performance Dashboard")

# Sample Data
data = {
    "Student": ["Alice", "Bob", "Charlie", "David", "Emma"],
    "Math": [85, 70, 90, 60, 95],
    "Science": [88, 75, 92, 65, 97],
    "English": [78, 80, 85, 70, 88],
    "Attendance (%)": [92, 85, 96, 78, 98]
}
df = pd.DataFrame(data)

# Sidebar filter
st.sidebar.header("Filter")
selected_students = st.sidebar.multiselect("Select Students", df["Student"], default=df["Student"])

# Filtered Data
filtered_df = df[df["Student"].isin(selected_students)]

# Show Data
st.subheader("Student Scores")
st.dataframe(filtered_df)

# Line Chart
st.subheader("📈 Scores Comparison")
fig = px.line(filtered_df.set_index("Student").T, title="Subject-wise Scores")
st.plotly_chart(fig)

# Bar Chart for Attendance
st.subheader("📊 Attendance Overview")
bar = px.bar(filtered_df, x="Student", y="Attendance (%)", color="Student", title="Attendance Percentage")
st.plotly_chart(bar)

# Conclusion
st.markdown("✅ This dashboard helps track performance and attendance trends for students.")

