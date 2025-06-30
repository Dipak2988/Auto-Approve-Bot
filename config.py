import os
from typing import List

API_ID = os.environ.get("API_ID", "29214489")
API_HASH = os.environ.get("API_HASH", "eb5bd88f71851a9c069eeb42ec0958aa")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
ADMIN = int(os.environ.get("ADMIN", "1362402982"))

LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002522789827"))
NEW_REQ_MODE = os.environ.get("NEW_REQ_MODE", "True").lower() == "true"  # Set "True" For accept new requests

DB_URI = os.environ.get("DB_URI", "mongodb+srv://dipaksinghasarkar32:Dipak2988@cluster0.4lqyh1s.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "Cluster0")

IS_FSUB = os.environ.get("IS_FSUB", "True").lower() == "true"  # Set "True" For Enable Force Subscribe
AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNEL", "-1001964648589 -1002245762167").split())) # Add Multiple channel ids
