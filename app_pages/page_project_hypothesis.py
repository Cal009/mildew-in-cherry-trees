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

    st.write("---")

    st.write("### Hypothesis 2 and Validation:")

    st.success(
        f"The model will be unable to predict as accurately if the background image is different from the"
        f" original beige background used to train with."
    )

    st.info(
        f"We suspect that due to the model being trained on images all with the same background,"
        f" it will be unable to remain as accurate when given an image with a different background."
    )

    st.warning(
        f"As the report shows, 10 images were passed through the model, however only 8/10 were predicted"
        f" correctly meaning the model accuracy dropped to approximately 80%. As agreed with the business owner,"
        f" the desired accuracy has to be 97% or above meaning that **yes** the background makes a difference to"
        f" the model accuracy. Knowing this it is vital to inform the business owner when future testing to achieve high accuracy reports."
    )

    st.write("---")

