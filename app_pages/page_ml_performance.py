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

    model_clf = plt.imread(f"outputs/{version}/clf_report.png")
    st.image(model_clf, caption='Classification Report')  

    st.warning(
        f"**Classification Report**\n\n"
        f"Precision: Percentage of correct predictions. The ratio of true positives to the sum of a true positive and false positive.\n\n"
        f"Recall: Percentage of positive cases detected. The ratio of true positives to the sum of true positives and false negatives.\n\n"
        f"F1 Score: Percentage of correct positive predictions. Weighted harmonic mean of precision and recall such that the best score is 1.0 and the worst is 0.0.\n\n"
        f"Support: The number of actual occurrences of the class in the specified dataset.")

    model_cm = plt.imread(f"outputs/{version}/confusion_matrix.png")
    st.image(model_cm, caption='Confusion Matrix')

    st.warning(
        f"**Confusion Matrix**\n\n"
        f"Confusion Matrix is a performance measurement for a classifier."
        f" It is a table with 4 different combinations of predicted and actual values.\n\n"
        f"True Positive / True Negative: the prediction matches the reality.\n\n"
        f"False Positive / False Negative: the prediction is opposite of reality (the leaf was predicted infected while it's actually healthy).\n\n"
        f"A good model is one which has high TP and TN rates, while low FP and FN rates.")

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
        f" With this in mind the lower the loss value is, the more accurate the model becomes, meaning more accurate predictions for the business to use.\n\n"
    )

    st.write("---")

    st.write("### Generalised Performance on Test Set")
    st.dataframe(pd.DataFrame(load_test_evaluation(version), index=['Loss', 'Accuracy']))