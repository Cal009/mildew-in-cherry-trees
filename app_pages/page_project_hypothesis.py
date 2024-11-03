import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    st.write("## Project Hypothesis and Validation")

    st.write("---")

    st.write("### Hypothesis 1 and Validation:")

    st.success(
        f"* Trees with powdery mildew have clear white markers on the leaves,\n"
        f" this can differentiate them from a healthy tree."    
    )

    st.info(
        f"We suspect that cherry leaves that are affected by powdery mildew show"
        f" clear markers on the surface of the leaf. Usually a white cotton-like growth appears to form around the leaf."
    )

    st.write("(To see this investigated thoroughly visit the mildew visualizer page.)")

    st.warning(
        f"The model was successful in determining the difference between healthy and affected leaves, and is now able to predict"
        f" with high levels of accuracy on unseen data. The model was trained to predict based on unseen data rather than adhere"
        f" too closely to the training data. This meant that it did not 'memorize' the training data allowing the business to use"
        f" the model in future cases with confidence in its accuracy."
    )

