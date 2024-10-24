import streamlit as st
import matplotlib.pyplot as plt

def page_project_hypothesis():
    st.write("### Project Hypothesis")

    st.success(
        f"* We predict that cherry trees with powdery mildew will have a clear mark on the samples\n"
        f" making it stand out from the healthy sample with no marks on it.\n"
        f"* An image montage shows the white mildew that appears to be on the infected samples"

    )