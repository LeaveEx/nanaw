
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = "3330416" # integer value, dont use ""
    API_HASH = "551d747d492ad11a10054fbf672d16e3"
    TOKEN = "5262608425:AAEbUDcE2inIrSqmzdSTTJUDlVHeZF5pJw8"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 1680004937 # If you dont know, run the bot and do /id in your private chat with it, also an integer
    
    SUPPORT_CHAT = "senzusupp"  # Your own group for support, do not add the @
    START_IMG = ""
    EVENT_LOGS = (-1001561812932)  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    MONGO_DB_URI= "mongodb+srv://newsenzu:newsenzu@cluster0.m1mw8vk.mongodb.net/?retryWrites=true&w=majority"
    # RECOMMENDED
    DATABASE_URL = "postgres://cuzdcojj:2AN8Z057twoa-wDUIM5XIQsUTzqxkbqU@rajje.db.elephantsql.com/cuzdcojj"  # A sql database url from elephantsql.com
    CASH_API_KEY = (
        "D0ZCZ67KL8OTL0PY"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "5LB4TAKPEKZ0"  # Get your API key from https://timezonedb.com/api

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = [1680004937]  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8
    

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
