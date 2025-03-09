# Daily Step Tracker :walking_man: 👣 📈


The **Daily Step Tracker** is a web application that helps users track their daily step counts, visualize trends, and get AI-powered insights. It provides a simple and intuitive interface for uploading step count data, viewing historical trends, and generating predictions for future step counts.

---

## Features

- **User Authentication**: Users can sign up and log in to access their personalized step count data.
- **Data Upload**: Users can upload their daily step count data manually or via a CSV file.
- **Trend Analysis**: Visualize daily step trends using interactive line graphs.
- **Active vs. Inactive Days**: Categorize days as active or inactive based on step count thresholds.
- **Weekly/Monthly Averages**: View average step counts per week or month.
- **AI-Powered Insights**:
  - Predict step counts for the next 7 days using linear regression.
  - Receive simple recommendations (e.g., "Increase activity on weekends").
- **User-Specific Data**: Each user’s data is stored separately, ensuring privacy and personalization.

---

## Technologies Used

### Backend
- **Flask**: A lightweight Python web framework for building the backend API.
- **SQLite**: A lightweight database for storing user and step count data.
- **Scikit-Learn**: A machine learning library for generating step count predictions.

### Frontend
- **Streamlit**: A Python library for building interactive web apps.
- **Matplotlib**: A plotting library for creating visualizations.
- **Seaborn**: A statistical data visualization library.

### Deployment
- **Render**: A cloud platform for deploying the Flask backend.
- **Streamlit Sharing**: A platform for deploying the Streamlit frontend.

---

## How It Works

1. **User Authentication**:
   - Users sign up or log in using a username and password.
   - Each user is assigned a unique `user_id` to ensure data privacy.

2. **Data Upload**:
   - Users can upload their daily step count data manually .
   - The data is stored in a SQLite database.

3. **Trend Analysis**:
   - Users can view their daily step trends using interactive line graphs.
   - Days are categorized as active or inactive based on step count thresholds.

4. **AI-Powered Insights**:
   - The app predicts step counts for the next 7 days using linear regression.
   - Users receive simple recommendations to improve their activity levels.

---

**Link to the site: https://daily-step-tracker-frontend-qteej6n4nuzpwbtkwfjzcv.streamlit.app/

---
##Screenshots

###LoginPage 


