import os
from dotenv import load_dotenv

load_dotenv()

API_VERSION = "1.0"
DEBUG = False
DEFAULT_UNITS = "metric"
MAX_HISTORY_DAYS = 30
SUPPORTED_SOURCES = ["open-meteo", "weatherapi"]
API_KEY = os.getenv("API_KEY")
