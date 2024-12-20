# ![Cherry-tree](https://github.com/Cal009/mildew-in-cherry-trees/blob/main/readme_images/cherry-tree.jpg) Cherry Leaf Mildew Detector 

## Table of Contents
1. [Dataset Content](#dataset-content)
2. [Business Requirements](#business-requirements)
3. [Hypothesis and Validation](#hypothesis-and-validation)
4. [Rational for the model](#rationale-for-the-model)
5. [Implementing the business requirements](#the-rationale-to-map-the-business-requirements-to-the-data-visualisations-and-ml-tasks)
6. [ML Business Case](#ml-business-case)
7. [Dashboard Design](#dashboard-design)
8. [CRISP-DM](#cross-industry-standard-process-for-data-mining-crisp-dm)
9. [Bugs](#unfixed-bugs)
10. [Deployment](#deployment)
11. [Technologies Used](#technologies-used)
12. [Credits](#credits)

### Deployed version of this site can be found [here](https://cherry-leaf-detector-7dd715ad1b7d.herokuapp.com/)

## Dataset Content

- The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
- The dataset contains +4 thousand images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.

## Business Requirements

The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute. The company has thousands of cherry trees located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.

- 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
- 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

## Hypothesis and Validation

**Hypothesis 1:**: Infected leaves have clear marks differentiating them from the healthy leaves.
- __How to Validate__: Research about the disease and build an average image study.<br/>

**Hypothesis 2:**: The model will be unable to predict as accurately if the background image is different from the original beige background used to train with.
- __How to Validate__: Use a variety of images with different backgrounds to determine the models accuracy.<br/>

### Hypothesis 1: 

#### _Infected leaves have clear marks differentiating them from the healthy leaves._

#### 1. Introduction

We suspect that cherry leaves that are affected by powdery mildew show clear markers on the surface of the leaf. Usually a white cotton-like growth appears to form around the leaf.

When we are dealing with an image dataset, it is important to normalise the images in the dataset. Normalized data is easy to interpret making it easier to understand. When all the features of a dataset are on the same scale, it also becomes easier to identify and visualize the relationships between different features and make meaningful comparisons, this is especially useful in our use case scenario.

#### 2. Observation

An image montage shows a clear difference between the two, infected and healthy

![montage_healthy](https://github.com/Cal009/mildew-in-cherry-trees/blob/main/readme_images/healthy_leaf.png)
![montage_infected](https://github.com/Cal009/mildew-in-cherry-trees/blob/main/readme_images/powdery_mildew_leaf.png)

Difference between average and variability images show that the affected leaves have more white markings in the center.

![average_variability](https://github.com/Cal009/mildew-in-cherry-trees/blob/main/readme_images/average_and_variability.png)

However the image difference between average infected and average healthy shows no difference.

![average_image](https://github.com/Cal009/mildew-in-cherry-trees/blob/main/readme_images/average_images.png)

### 3. Conclusion

The model was successful in being able to generalize and make accurate predictions by detecting the differences between healthy and infected. A sign of a good model shows that it did not 'memorize' the data set given to it when training allowing it to maintain its accuracy when presented with unseen data. This means the business can successfully use this model for the forseeable fututre, knowing it will provide accurate results.

### Hypothesis 2: 

#### _The model will be unable to predict as accurately if the background image is different from the original beige background used to train with._

#### 1. Introduction

We suspect that due to the model being trained on images all with the same background, it will be unable to remain as accurate when given an image with a different background.

It is important to check for a detail like this incase it does provide a discrepency, allowing us to inform he business owner.

#### 2. Observation

Shown below is a collage of all the images used to test this hypothesis against the running ML model.

![leaf_collage](https://github.com/Cal009/mildew-in-cherry-trees/blob/main/readme_images/leaf_collage.png)

All images have a different background to the origninal data set and once put through the Ml model the data below shows the accuracy.

![random_background_report](https://github.com/Cal009/mildew-in-cherry-trees/blob/main/readme_images/random_sample_report.png)

#### 3. Conclusion

As the report shows, 10 images were passed through the model, however only 8/10 were predicted correctly meaning the model accuracy dropped to approximately 80%. As agreed with the business owner, the desired accuracy has to be 97% or above meaning that **yes** the background makes a difference to the model accuracy. Knowing this it is vital to inform the business owner when future testing to achieve high accuracy reports.

## Rationale for the model

The model has 1 input layer, 3 hidden layers (2 ConvLayer, 1 FullyConnected), 1 output layer.

### Objective

When setting the hyperparameters, number of hidden layers and choosing the optimizer was merely based on trial and error. I found that during the testing stage it was a fine line with the decision as the error margin was so low for the business requirements. A sign of a well trained model is its ability to remain accurate on unseen data.

### Choosing the hyperparameters

#### - Convolutional layer size:
Conv1d and Conv2d are the main two convolutional layersr used. In our project it was more appropriate to use Conv2d (2 dimensional) as we are working with image data. Conv1d  is mainly used on sequential data with one spatial dimension whereas Conv2d is mainly used on image data as it applies 2 dimensional convolution height and width.

#### Activation Function: 
Relu is used for its simplicity, speed and its ability to work well with the given dataset. Relu usually produces higher-performance models due to its ability to train deep neural networks effectively. If the ReLU function is used for activation in a neural network in place of a sigmoid function, the value of the partial derivative of the loss function will have values of 0 or 1 which prevents the gradient from vanishing. More information can be found [here](https://www.kdnuggets.com/2022/02/vanishing-gradient-problem.html#:~:text=If%20the%20ReLU%20function%20is,prevents%20the%20gradient%20from%20vanishing.)

#### Pooling:
Pooling is a key concept in machine learning that plays a significant role in improving the performance of deep learning models. It is a process of down sampling the feature maps obtained from convolutional layers to reduce their spatial dimensions while retaining their most important features. In this project we use whats known as MaxPooling. MaxPooling is useful when the background of the image is dark and we are interested in only the lighter pixels of the image (powdery mildew is white). More on [Pooling](https://mohitmishra786687.medium.com/pooling-a-key-concept-in-machine-learning-81c05dcbce98#:~:text=Recap%20of%20the%20importance%20of,reducing%20the%20number%20of%20parameters.)

#### Output Activation function:
Our model required the use of either sigmoid or softmax. Our model that was trained was unable to reach a suitable accuracy rating when using sigmoid and therefore the choice was made to use softmax as this did provide us with the correct outcome.


## The rationale to map the business requirements to the Data Visualisations and ML tasks
The business requirements were split into multiple user stories. **They were then manually tested and all the tasks/functions work as intended**

### Business Requirement 1: Data Visualization
>The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.

**User Stories:**

- As a client I want a clear and interactive dashboard that displays all the data findings in an understandable manner.

- As a client I want to display the difference between average and variability images in order to differentiate between healthy and infected leaves

- As a client I want to display the difference between the average healthy leaf and average leaf affected by the powdery mildew in order to visually differentiate between the two.

- As a client I want to display an image montage of either healthy leaves or those affected by powdery mildew in order to visually differentiate between the two.

The user stories were addressed when creating the Data Visualization notebook and are then displayed on the streamlit dashboard.
Breaking down the Data Visualization notebook:

- The difference between an average infected leaf and a healthy one

- Image montage for either infected or healthy leaves.

### Business Requirement 2: Classification
>The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

**User Story:**

- As a client I want the ML model to have an overall accuracy rating of at least 97%

The user story was adhered to when creating the ML model and acchieved over the required accuracy. That can then be used in the dashboard to upload more images and still receive the same level of accuracy.

## ML Business Case

#### MildewCLF

- We want the ML model to predict if a given tree has the powdery mildew or not base on historical image data. It is a supervised model, a 2-class, single-label classification model.
- As agreed with the client, the success metrics are to be 97% or above
- Heuristics: The current diagnostic requires a member of staff to spend around 30 minutes on each tree, taking a few samples from the tree leaves and verifying visually if the leaf is healthy or has powdery mildew. If the tree has powdery mildew on it, the employee will apply a specific amount of a specific compound to kill the fungus.
- The training data to fit the model came from a leaves database provided by the Farmy Foods company. The dataset contained 4206 images of cherry leaves, 50% healthy, 50% affected by powdery mildew.

## Dashboard Design

#### Page 1: Quick Project Summary
- Quick Project study
    - General information
        - The powdery mildew that can be found on cherry tree's is caused by the fungus Podosphaera clandestina.
        - This fungus can easily be spread by insects or wind pushing the fungus spores airborn
        - The process for manually identifying these trees can be very tedious and time consuming for the business.
        - Multiple samples are collected via hand from the trees, assessed and then if necessary a compound is applied to the diseased tree, aiming to kill the fungus.
    - Project Dataset
        - The given dataset contains 4208 samples with the data being split 50/50 between healthy and powdered mildew
    - Business Requirements
        - The client is interested in conducting a study to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew.
        - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

#### Page 2: Mildew Visualizer
- This page will answer business requirement 1
    - Checkbox 1 - Difference between average and variability image
    - Checkbox 2 - Differences between average infected tree and normal tree
    - Checkbox 3 - Image montage

#### Page 3: Mildew Detector
- This page will deal with business requirement 2
- A link to download a set of infected and uninfected images for live prediction.
- User interface with a file uploader widget. The user should upload multiple infected images. It will display the image and a prediction statement, indicating if the leaf is tree is infected with the powdery mildew or not and the probability associated with the statement.
- Table with the image name and prediction results
- Donwload button to download the results.

#### Page 4: Project hypothesis and validation
- A section for each hypothesis and the validation beneath it. Each hypothesis will be broken down into introduction, observation and conclusion.

#### Page 5: ML Performance Metrics
- Label Frequencies for Train, Validation and Test Sets
- Classification Report
- Confusion Matrix
- Model History - Accuracy and Losses
- Model evaluation result

## Cross-Industry standard process for data mining (CRISP-DM)
CRISP-DM is known as an industry-proven way to guide data mining efforts.
    - As a methodology, it includes descriptions of the typical phases of a project, the tasks involved with each phase, and an explanation of the relationship between each task.
    - As a process model, CRISP-DM provides an overview of the data mining life cycle

Source for the information can be found at [IBM](https://www.ibm.com/docs/sr/spss-modeler/saas?topic=dm-crisp-help-overview)

Below you can see a snippit of an example of CRISP-DM in use for this project. It outlined each process that needed taking for data visualization.

![CRISP-DM](https://github.com/Cal009/mildew-in-cherry-trees/blob/main/readme_images/crisp-dm.png)

    
## Unfixed Bugs

- No unfixed bugs present.

## Technologies Used

- Heroku was used to deploy the project
- Jupiter Notebook: to create and edit code for the project
- Kaggle: for the dataset
- Github was used to store the project code after deploying from gitpod
- Gitpod: Used to write the code and commit and push to github
- Python was the main language used
- numpy==1.19.2
- pandas==1.1.2
- matplotlib==3.3.1
- seaborn==0.11.0
- plotly==4.12.0

- streamlit==0.85.0

- scikit-learn==0.24.2
- tensorflow-cpu==2.6.0
- keras==2.6.0
- protobuf==3.20
- altair<5

## Credits

Credit given to cla-cif and their Cherry-Powdery-Mildew-Detector, giving me ideas and guidance on the documentaion of the project.
Credit to Code Institute for providing the project template
Credit to Code Institute for the malaria walkthrough project.

### Content

The leaves data set was linked from [Kaggle](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves)

### Media

- The photo used in the README file was found on [Pexels](https://www.pexels.com) from Julia Filirovska

### Heroku

- The App live link is: `https://YOUR_APP_NAME.herokuapp.com/`
- Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
- The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large, then add large files not required for the app to the .slugignore file.

## Cloud IDE Reminders

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to _Account Settings_ in the menu under your avatar.
2. Scroll down to the _API Key_ and click _Reveal_
3. Copy the key
4. In the terminal, run `heroku_config`
5. Paste in your API key when asked

## Acknowledgements

- Thank you to Mo Shami for the one to one guidance.
