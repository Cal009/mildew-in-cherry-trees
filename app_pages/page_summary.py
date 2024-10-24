import streamlit as st
import matplotlib.pyplot as plt

def page_summary():
    st.write("### Project Summary")

    st.info(
        f"** General Information**\n"
        f"* The powdery mildew that can be found on cherry tree's is caused by the fungus Podosphaera clandestina.\n"
        f"* This fungus can easily be spread by insects or wind pushing the fungus spores airborn\n"
        f"* The process for manually identifying these trees can be very tedious and time consuming for the business\n"
        f"* Multiple samples are collected via hand from the trees, assessed and then if"
        f" necessary a compound is applied to the diseased tree, aiming to kill the fungus.\n"
        f"* The given dataset contains 4208 samples with the data being split 50/50\n"
        f" between healthy and powdered mildew"
    )

    st.success(
        f"The project has 2 business requirements:\n"
        f"* **Business requirement 1:** Your study should include at least analysis on:\n"
        f"- average images and variability images for each class (healthy or powdery mildew)\n"
        f"- the differences between average healthy and average powdery mildew cherry leaves\n"
        f"- an image montage for each class.\n"
        f"* **Business requirement 2:**\n"
        f" - The client is interested in predicting if a cherry tree is healthy or contains powdery mildew. "
        )