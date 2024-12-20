# 5105group
# Welcome to Our GHG Emissions Calculator Project!

## Project Overview

Greetings, and welcome to our project! We’re thrilled to have you here and appreciate your interest in our efforts to tackle climate change through data-driven solutions. As concerns around climate change grow, organizations are increasingly focused on tracking and reducing their greenhouse gas (GHG) emissions. However, for many companies, especially those without expertise in carbon auditing, accurately calculating emissions can be a significant challenge. Our project aims to address this need by developing an intuitive GHG emissions calculator tailored specifically for office buildings in Singapore.

This tool will empower companies to:
- Calculate their annual GHG emissions with ease.
- Track emissions trends over time.
- Identify opportunities for energy savings and carbon reduction.

By offering two calculation methods and incorporating both local and international emission factors, we hope to make emissions tracking accessible, accurate, and practical for a diverse range of users.

## Project Structure

As a team of dedicated students, we’ve pooled our skills and knowledge to develop this project. After an initial collaborative phase focused on data collection and preprocessing, we have divided into two specialized subgroups, each responsible for critical aspects of the project:

### Subgroup A: 
Focused on the analytical and computational core, Subgroup A is responsible for building the backbone of the emissions calculator. Key tasks include:
- **Data Analysis and Calculations**: Developing methodologies to ensure accurate and reliable emissions calculations tailored to the unique characteristics of Singapore's office buildings.
- **Predictive Model Building**: Creating sophisticated prediction models to estimate emissions, even when detailed activity data is unavailable, thereby broadening the tool’s applicability.
- **Database Development**: Designing a robust database structure to efficiently store and retrieve emissions data, benchmarks, and other relevant information. Subgroup A ensures the scientific rigor and reliability of the tool, empowering users to make data-informed decisions.

### Subgroup B: 
Committed to creating an intuitive user experience, Subgroup B is responsible for the front-end development. Their work includes:
- **User-Friendly Interface Design**: Building an accessible web interface that allows users, regardless of their technical expertise, to easily input data and interpret their emissions results.
- **Interactive and Engaging Visuals**: Crafting interactive visualizations and dashboards to display emissions data in a clear, insightful way, tailored for different stakeholders such as sustainability teams and management.
- **Enhancing User Experience**: Prioritizing a clean, user-centered design to ensure a smooth, engaging experience. Subgroup B is dedicated to making the tool as enjoyable to use as it is informative.

Together, these two subgroups are working to make our GHG emissions calculator an invaluable resource for Singapore’s office buildings, contributing to a more sustainable future.


## Carbon Emissions Calculator Overview

- **Standardized Calculator**: Calculates total carbon emissions based on user inputs.
- **Prediction Calculator**: Predicts emissions using a machine learning model.

Users can input data manually or upload CSV files. The results include total emissions, data visualizations comparing emissions to industry averages, and a personalized report generated by OpenAI's API.

- **Display Adaptation (1080p)**：
This application has been designed to deliver the best visual and interactive experience on **24-inch displays with 1080p resolution**. To ensure compatibility:

- **Target Resolution**: 1920×1080 (Full HD).
- **Scaling Recommendations**: Adjust the browser’s zoom level based on your display settings:
  - For a 24-inch monitor: Use a zoom level of 100%.
  - For smaller screens or higher resolutions: Adjust the zoom level to fit the layout properly.
- For unsupported resolutions or devices, resizing or scaling the browser window may help achieve better compatibility.

###  Technologies Used
- **HTML**: `index.html`
- **CSS**: `index.css`
- **JavaScript**: `script.js`
- **Visualization Tool**: Chart.js
- **OpenAI API**: [https://api.openai.com/v1/chat/completions](https://api.openai.com/v1/chat/completions), used for generating personalized reports.
- **Local Machine Learning API**: After installing Flask and Flask-CORS, the API can be started from the `5105_ml` directory by running `python app.py` in the terminal. The `app.py` script processes the `best_rf_model.pkl` file, converting it into a JSON format readable by JavaScript for frontend integration.

### Setup Instructions
- **Frontend**
  Navigate to the following GitHub path: 5105group/subgroupB. Download and extract the file named "510_Front-end_website_implementation.zip".
  After extracting, open the index.html file to view the front-end interface. Follow the steps below to demonstrate the API functionality as part of the presentation.

- **Backend API**
1. Navigate to the `5105group/subgroupB` folder.(Download "demofinal" to your computer and unzip it all)
2. Install required dependencies:
   ```sh
   pip install flask
   pip install flask-cors
   ```
3. Start the local API server: cmd CD demofinal/5105ML/5105ML
   ```sh
   python app.py
   ```
4. Ensure the `best_rf_model.pkl` file is in the same directory as `app.py`.

- **Connecting Frontend and Backend**
Update the API endpoint in `script.js` to match the local backend server, e.g., `http://127.0.0.1:5000`.

### OPENAI API
Key Security and Backup Program Description：
  Although I have encrypted the OpenAI API key, the project requires the code to be uploaded to GitHub, and since GitHub is a public platform, even 
  though the key is encrypted, there is still a possibility that OpenAI's automated scanning system will detect the key and treat it as a leak, which could 
  result in the key being revoked.To address this potential problem, I have placed an alternate key in the Google Doc. This alternate key is only used in emergency situations, such as 
  when the reports section of a front-end web page displays “No Data Fetch”, you can follow the steps below to replace the key in the JavaScript file 
  to ensure that the feature works properly
  
https://docs.google.com/document/d/1t5dLr-_05mcakdf8fZ-jpFWaSNDTKdL3lv9-nJvT9F8/edit?usp=sharing

- **How to Use**
1. Input data manually or upload a CSV file.
2. View the results:
   - Total carbon emissions.
   - Visualizations comparing emissions to industry averages.
3. Generate a personalized report based on user data and emissions results.

## Further Information

For a more detailed look at our research process and implementation steps, please visit our **Wiki**. The wiki provides in-depth explanations and welcomes your feedback. We’re excited to receive any comments, suggestions, or guidance to help us improve this project and create a more effective tool for emissions tracking.

