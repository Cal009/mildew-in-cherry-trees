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
        f"* **Business requirement 1:**\n"
        f" - The client is interested in conducting a study to visually differentiate"
        f" a cherry leaf that is healthy from one that contains powdery mildew.\n"
        f"* **Business requirement 2:**\n"
        f" - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew. "
        )

    st.success(
        f"**Conclusion:**\n\n"
        f" Overall this Machine Learning Model was able to achieve the desired outcome, being able to accurately differentiate between a healthy cherry leaf"
        f" and one thats affected by the powdery mildew, linking to business requirement 1. It was able to do this with a high accuracy score which can be found further in this dashboard."
        f" It can then also be used for future predictions so long as it maintains the same structure as the training data, linking to business requirement 2."
        f" The overall project meets all business requirements and is suitable for future use within the buiness."
    )