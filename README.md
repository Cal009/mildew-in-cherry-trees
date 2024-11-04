# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## Cloud IDE Reminders

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to _Account Settings_ in the menu under your avatar.
2. Scroll down to the _API Key_ and click _Reveal_
3. Copy the key
4. In the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you, so do not share it. If you accidentally make it public, then you can create a new one with _Regenerate API Key_.

## Table of Contents
1. [Dataset Content](#dataset-content)
2. [Business Requirements](#business-requirements)
3. [Hypothesis and Validation](#hypothesis-and-validation)
4. [Implementing the business requirements](#the-rationale-to-map-the-business-requirements-to-the-data-visualisations-and-ml-tasks)
5. [ML Business Case](#ml-business-case)
6. [Dashboard Design](#dashboard-design)
7. [Bugs](#unfixed-bugs)
8. [Deployment](#deployment)
9. [Technologies Used](#technologies-used)
10. [Credits](#credits)

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

## The rationale to map the business requirements to the Data Visualisations and ML tasks

- Business Requirement 1: Data Visualization

    - We will display the "mean" and "standard deviation" images for powedery mildew and healthy leaves.
    - We will display the difference between average diseased and healthy leaves.
    - We will display an image montage for either dieseased or healthy leaves.

- Business Requirement 2: Classification

    - We want to predict if a given tree is healthy or not.
    - We want to build a binary classifier and generate reports.

## ML Business Case

#### MildewCLF

- We want the ML model to predict if a given tree has the powdery mildew or not base on historical image data. It is a supervised model, a 2-class, single-label classification model.
- As agreed with the client, the success metrics are to be 97% or above
- Heuristics: The current diagnostic requires a member of staff to spend around 30 minutes on each tree, taking a few samples from the tree leaves and verifying visually if the leaf is healthy or has powdery mildew. If the tree has powdery mildew on it, the employee will apply a specific amount of a specific compound to kill the fungus.

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
- User interface with a file uploader widget. The user should upload multiple infected images. It will display the image and a prediction statement, indicating if the leaf is tree is infected with the powdery mildew or not and the probability associated with he statement.
- Table with the image name and prediction results
- Donwload button to download the results.

#### Page 4: Project hypothesis and validation

#### Page 5: ML Performance Metrics
- Label Frequencies for Train, Validation and Test Sets
- Model History - Accuracy and Losses
- Model evaluation result

    
## Unfixed Bugs

- You will need to mention unfixed bugs and why they were unfixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable for consideration, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

## Technologies Used

- Here, you should list the libraries used in the project and provide an example(s) of how you used these libraries.

## Credits

- In this section, you need to reference where you got your content, media and from where you got extra help. It is common practice to use code from other repositories and tutorials. However, it is necessary to be very specific about these sources to avoid plagiarism.
- You can break the credits section up into Content and Media, depending on what you have included in your project.

### Content

- The text for the Home page was taken from Wikipedia Article A.
- Instructions on how to implement form validation on the Sign-Up page were taken from [Specific YouTube Tutorial](https://www.youtube.com/).
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/).

### Media

- The photos used on the home and sign-up page are from This Open-Source site.
- The images used for the gallery page were taken from this other open-source site.

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

## Acknowledgements (optional)

- Thank the people who provided support throughout this project.
