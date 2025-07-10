import os
from typing import List

API_ID = os.environ.get("API_ID", "27634013")
API_HASH = os.environ.get("API_HASH", "7b2dbd9636bfe069254beb85649099df")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
ADMIN = int(os.environ.get("ADMIN", "6701240300"))

LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002806658606"))
NEW_REQ_MODE = os.environ.get("NEW_REQ_MODE", "True").lower() == "true"  # Set "True" For accept new requests

DB_URI = os.environ.get("DB_URI", "mongodb+srv://dipaksinghasarkarss:Dipakss123@cluster0.7xzqr9t.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "Cluster0")

IS_FSUB = os.environ.get("IS_FSUB", "False").lower() == "true"  # Set "True" For Enable Force Subscribe
AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNEL", "-1001964648589 -1002245762167").split())) # Add Multiple channel ids
