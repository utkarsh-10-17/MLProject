# Disease Prediction System

A Machine Learning-based web application for predicting heart disease and diabetes. This project uses trained ML models (serialized with `pickle`) and displays results via a Flask-powered web interface.

## Features
- **Disease Prediction:** Predicts heart disease and diabetes likelihood based on user inputs.
- **Web Interface:** User-friendly interface built with Flask, HTML, and CSS.
- **Serialized Models:** Efficient prediction using pre-trained models.

## Technologies
- **Languages:** Python
- **Libraries:** Scikit-learn, Pandas, NumPy, Flask, Pickle
- **Frontend:** HTML, CSS
- **Tools:** Flask for backend, Pickle for model storage

## Project Structure
├── app.py # Main Flask application ├── templates/index.html # Web interface ├── static/styles.css # CSS for the webpage ├── heart_disease_model.pkl # Heart disease ML model ├── diabetes_model.pkl # Diabetes ML model ├── datasets/ # CSV files for training ├── requirements.txt # Python dependencies


## How to Run
1. Clone the repository:  
   `git clone https://github.com/yourusername/disease-prediction.git`
2. Navigate to the project folder:  
   `cd disease-prediction`
3. Install dependencies:  
   `pip install -r requirements.txt`
4. Run the app:  
   `python app.py`
5. Access at `http://127.0.0.1:5000` in your browser.

## Datasets
The project uses publicly available datasets for heart disease and diabetes.

## Contact
- **Email:** utkarshghore@gmail.com  
- **GitHub:** [utkarsh-10-17](https://github.com/utkarsh-10-17)


