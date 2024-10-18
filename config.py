from os import environ 

class Config:
    API_ID = environ.get("API_ID", "28837789")
    API_HASH = environ.get("API_HASH", "33c9162294cdd6c9d51d964e4469fadb")
    BOT_TOKEN = environ.get("BOT_TOKEN", "") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://smallcapitaltrader1:XVsdQj8vu38ZIFoy@cluster0.9g3ri.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", "8087702564").split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
