import os


class Config(object):
    API_HASH = os.environ.get("0861a545777adba2d599304b6474aad1")
    BOT_TOKEN = os.environ.get("7917848836:AAFTxnNuqGibqYPyr-HJaaIhy8edlK7i8Lk")
    TELEGRAM_API = os.environ.get("9102574")
    OWNER = os.environ.get("5212197608")
    OWNER_USERNAME = os.environ.get("@Botyoutuber1")
    PASSWORD = os.environ.get("Raj")
    DATABASE_URL = os.environ.get("mongodb+srv://Ayush:AYUSHRA5354N@cluster0.lskh5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    LOGCHANNEL = os.environ.get("-1002206233283")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle", "extract-streams"]
