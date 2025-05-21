import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport

st.title("CSV Profiling Report Generator")

# Upload CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
 # Read the CSV file into a DataFrame
 df = pd.read_csv(uploaded_file)

 # Display the DataFrame (optional)
 st.subheader("Data Preview")
 st.dataframe(df.head())

 st.write("Generating the profiling report. Please wait...")
 
 # Generate the profiling report
 profile = ProfileReport(df, title="Data Profiling Report", explorative=True)
 
 # Get the HTML as a string; this avoids writing to disk
 report_html = profile.to_html()
 
 # Provide a download button for the HTML report
 st.download_button(
     label="Download Profiling Report (HTML)",
     data=report_html,
     file_name="data_profile.html",
     mime="text/html"
 )

 st.success("Report generated!")
else:
 st.info("Upload a CSV file to generate a profiling report.")
