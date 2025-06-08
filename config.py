# Google Maps API Configuration
GOOGLE_MAPS_API_KEY = "your api key here"

# Database Configuration
import os
BASEDIR = os.path.abspath(os.path.dirname(__file__))
SQLITE_DB_PATH = os.path.join(BASEDIR, 'health_assistant.db')
SQLALCHEMY_DATABASE_URI = f'sqlite:///{SQLITE_DB_PATH}'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'your-secret-key-here'  # Used for session management 
