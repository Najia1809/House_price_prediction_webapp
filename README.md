# House Price Prediction Web App

This is a simple web application built using **Flask**, **scikit-learn**, and **Pandas** for predicting house prices. It uses a pre-trained machine learning model (SVC model) to predict the price of a house based on various features like the number of bedrooms, bathrooms, living area, etc. The model was trained on a processed dataset containing real estate data.

## Features

- User-friendly form to input property details.
- Predict house prices using a machine learning model.
- Real-time predictions with AJAX.
- Dark/Light mode toggle.
- Responsive design for mobile and desktop devices.

## Tech Stack

- **Backend**: Flask (Python web framework)
- **Frontend**: HTML, CSS (with a dark/light mode toggle), JavaScript (jQuery for AJAX requests)
- **Machine Learning Model**: Scikit-learn (SVC - Support Vector Classifier)
- **Data Processing**: Pandas, NumPy
- **Styling**: Custom CSS for UI/UX design

## Installation

### Prerequisites

- Python 3.x
- Virtual environment (optional but recommended)

### Steps to Run the Application

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/RasikhAli/House-Price-Prediction-Web-App.git
   cd House-Price-Prediction-Web-App
   ```

2. Create a virtual environment (optional):

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. Install the necessary dependencies from the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

4. Ensure that the pre-trained model `model_svc.pkl` and the dataset `processed_data.csv` are in the project directory. These files are essential for the app to run. If they are not available, you need to train the model using your own dataset.

5. Start the Flask development server:

   ```bash
   python app.py
   ```

6. Open your web browser and go to `http://127.0.0.1:5000` to access the application.

## Files and Directory Structure

- `app.py`: The main Flask app file that handles routing and model prediction.
- `index.html`: The HTML template for the front-end form and display.
- `styles.css`: The custom styles for the application UI.
- `model_svc.pkl`: The pre-trained machine learning model file (make sure this file is present).
- `processed_data.csv`: The dataset containing the feature information for the model (ensure this file is available).

## How It Works

1. **Homepage**: Displays a form with several dropdowns and input fields to collect property information like the number of bedrooms, bathrooms, lot size, and more.
2. **Prediction**: Once the user submits the form, the application sends the data to the Flask backend using an AJAX request. The backend then processes the data, uses the pre-trained machine learning model to predict the house price, and returns the result to be displayed on the page.
3. **Styling**: The app has a clean, modern design with a dark/light mode toggle for better user experience.

## Contributing

Feel free to fork this repository, create an issue, or submit a pull request if you'd like to contribute or suggest improvements.

## License

This project is open-source and available under the MIT License.
