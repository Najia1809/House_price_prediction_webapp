from flask import Flask, render_template, request, jsonify
from sklearn.preprocessing import OneHotEncoder
import pickle
import pandas as pd
import numpy as np

# Initialize the Flask app
app = Flask(__name__)

# Load the pre-trained model
model_svc = pickle.load(open('model_svc.pkl', 'rb'))

# Load the processed dataset for the feature list
df = pd.read_csv('processed_data.csv')

# Define a function to get the unique values for dropdowns
def get_dropdown_values():
    unique_bedrooms = sorted(df['bedrooms'].unique())
    unique_bathrooms = sorted(df['bathrooms'].unique())
    unique_floors = sorted(df['floors'].unique())
    unique_waterfront = [0, 1]
    unique_view = sorted(df['view'].unique())
    unique_condition = sorted(df['condition'].unique())
    unique_yr_built = sorted(df['yr_built'].unique())

    # Add unique values for categorical features
    unique_streets = sorted(df['street'].unique())
    unique_cities = sorted(df['city'].unique())
    unique_statezips = sorted(df['statezip'].unique())

    return unique_bedrooms, unique_bathrooms, unique_floors, unique_waterfront, unique_view, unique_condition, unique_yr_built, unique_streets, unique_cities, unique_statezips

# Load the encoders or create a mapping from the processed data
street_mapping = {street: idx for idx, street in enumerate(sorted(df['street'].unique()))}
city_mapping = {city: idx for idx, city in enumerate(sorted(df['city'].unique()))}
statezip_mapping = {statezip: idx for idx, statezip in enumerate(sorted(df['statezip'].unique()))}

# Route for homepage
@app.route("/", methods=["GET", "POST"])
def index():
    # Get unique values for the dropdowns
    unique_bedrooms, unique_bathrooms, unique_floors, unique_waterfront, unique_view, unique_condition, unique_yr_built, unique_streets, unique_cities, unique_statezips = get_dropdown_values()

    if request.method == "POST":
        try:
            # Get form data
            bedrooms = int(request.form['bedrooms'])
            bathrooms = float(request.form['bathrooms'])
            sqft_living = int(request.form['sqft_living'])
            sqft_lot = int(request.form['sqft_lot'])
            floors = float(request.form['floors'])
            waterfront = int(request.form['waterfront'])
            view = int(request.form['view'])
            condition = int(request.form['condition'])
            sqft_above = int(request.form['sqft_above'])
            sqft_basement = int(request.form['sqft_basement'])
            yr_built = int(request.form['yr_built'])
            yr_renovated = int(request.form.get('yr_renovated', 0))
            
            # Use categorical values directly if that's how the model was trained
            street = request.form['street']
            city = request.form['city']
            statezip = request.form['statezip']

            # Create feature array with proper column names
            feature_names = [
                'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors',
                'waterfront', 'view', 'condition', 'sqft_above', 'sqft_basement',
                'yr_built', 'yr_renovated', 'street', 'city', 'statezip'
            ]

            all_features = [
                bedrooms, bathrooms, sqft_living, sqft_lot, floors,
                waterfront, view, condition, sqft_above, sqft_basement,
                yr_built, yr_renovated, street, city, statezip
            ]

            # Create DataFrame with feature names to match training data
            features_df = pd.DataFrame([all_features], columns=feature_names)
            
            # Predict the price using the model
            predicted_price = model_svc.predict(features_df)[0]
            predicted_price = float(predicted_price)  # Convert numpy type to Python float
            
            # Return JSON for AJAX requests
            if request.is_json or request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return jsonify({
                    'success': True,
                    'predicted_price': round(predicted_price, 2)
                })

        except Exception as e:
            print(f"Error during prediction: {str(e)}")
            if request.is_json or request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return jsonify({
                    'success': False,
                    'error': str(e)
                })

    return render_template('index.html', 
                           unique_bedrooms=unique_bedrooms, unique_bathrooms=unique_bathrooms,
                           unique_floors=unique_floors, unique_waterfront=unique_waterfront,
                           unique_view=unique_view, unique_condition=unique_condition,
                           unique_yr_built=unique_yr_built,
                           unique_streets=unique_streets, unique_cities=unique_cities, unique_statezips=unique_statezips)

if __name__ == "__main__":
    app.run(debug=True)
