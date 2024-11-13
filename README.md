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

## Display Adaptation (1080p)
This application has been designed to deliver the best visual and interactive experience on **24-inch displays with 1080p resolution**. To ensure compatibility:

- **Target Resolution**: 1920×1080 (Full HD).
- **Scaling Recommendations**: Adjust the browser’s zoom level based on your display settings:
  - For a 24-inch monitor: Use a zoom level of 100%.
  - For smaller screens or higher resolutions: Adjust the zoom level to fit the layout properly.
- For unsupported resolutions or devices, resizing or scaling the browser window may help achieve better compatibility.

## Technologies Used
### Frontend
- **HTML**: `index.html`
- **CSS**: `index.css`
- **JavaScript**: `script.js`
- **Visualization Tool**: Chart.js

### Backend
- **OpenAI API**: [https://api.openai.com/v1/chat/completions](https://api.openai.com/v1/chat/completions), used for generating personalized reports.
- **Local Machine Learning API**: After installing Flask and Flask-CORS, the API can be started from the `5105_ml` directory by running `python app.py` in the terminal. The `app.py` script processes the `best_rf_model.pkl` file, converting it into a JSON format readable by JavaScript for frontend integration.

## Setup Instructions

### Frontend
1. Clone the repository:
   ```sh
   git clone <repository_url>
   cd <repository_folder>
   ```
2. Open the `index.html` file in a browser.

### Backend API
1. Navigate to the `5105_ml` folder.
2. Install required dependencies:
   ```sh
   pip install flask
   pip install flask-cors
   ```
3. Start the local API server:
   ```sh
   python app.py
   ```
4. Ensure the `best_rf_model.pkl` file is in the same directory as `app.py`.

### Connecting Frontend and Backend
Update the API endpoint in `script.js` to match the local backend server, e.g., `http://127.0.0.1:5000`.

## How to Use
1. Input data manually or upload a CSV file.
2. View the results:
   - Total carbon emissions.
   - Visualizations comparing emissions to industry averages.
3. Generate a personalized report based on user data and emissions results.

## Further Information

For a more detailed look at our research process and implementation steps, please visit our **Wiki**. The wiki provides in-depth explanations and welcomes your feedback. We’re excited to receive any comments, suggestions, or guidance to help us improve this project and create a more effective tool for emissions tracking.

