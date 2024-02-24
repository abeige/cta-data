# Adam Beigel
# 24 February 2023

import os
from dotenv import load_dotenv

load_dotenv()
bus_api_key = os.getenv('BUS_API_KEY')
train_api_key = os.getenv('TRAIN_API_KEY')
