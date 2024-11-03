import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
from src.machine_learning.evaluate_clf import load_test_evaluation


def page_ml_performance_metrics():
    version = 'v1'

    st.info(
        f"This page shows how the dataset was divided and how the model performed on the data."
    )

    st.write("### Image distribution between Train, Validation and Test")

    labels_distribution = plt.imread(f"outputs/{version}/labels_distribution.png")
    st.image(labels_distribution, caption='Image distribution between Train, Validation and Test')

    st.warning(
        f"The cherry leaves dataset was divided into three groups: \n\n"
        f" • Train set (70% of the dataset) is the initial data that is used to train the model, which will learn how to generalise and make predictions on unseen data.\n\n"
        f" • Validation set (10% of the dataset) is then used to fine tune the model performance. It does this after every epoch which is one cycle of the training set through the model.\n\n"
        f" • The test set (20% of the dataset) tells us about the model accuracy using data that it has not seen before."
    )

    st.write("---")


    st.write("### Model Performance")
    col1, col2 = st.beta_columns(2)
    with col1: 
        model_acc = plt.imread(f"outputs/{version}/model_training_acc.png")
        st.image(model_acc, caption='Model Training Accuracy')
    with col2:
        model_loss = plt.imread(f"outputs/{version}/model_training_losses.png")
        st.image(model_loss, caption='Model Training Losses')

    st.warning(
        f"• The loss value implies how well or not a model behaves after each optimization period.\n\n"
        f"• The loss function quantifies the error margin between the model's predictions and the actual target value."
        f"With this in mind the lower the loss value is, the more accurate the model becomes, meaning more accurate predictions for the business.\n\n"
    )

    st.write("---")

    st.write("### Generalised Performance on Test Set")
    st.dataframe(pd.DataFrame(load_test_evaluation(version), index=['Loss', 'Accuracy']))