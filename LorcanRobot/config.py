import json
import os


def get_user_list(config, key):
    with open("{}/LorcanRobot/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    API_ID = ""
    API_HASH = ""
    ARQ_API_KEY = ""
    ARQ_API_URL = ""
    TOKEN = ""
    ALLOW_CHATS = True

    OWNER_ID = 
    OWNER_USERNAME = ""
    SUPPORT_CHAT = ""
    JOIN_LOGGER = ()  
    EVENT_LOGS = ()  
    ERROR_LOGS = ()

    # RECOMMENDED
    MONGO_DB_URI = ""
    SQLALCHEMY_DATABASE_URI = ""
    LOAD = []
    NO_LOAD = []
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = ""
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")
    DONATION_LINK = None
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True
    STRICT_GBAN = True
    WORKERS = (8)
    BAN_STICKER = ""
    ALLOW_EXCL = True
    CASH_API_KEY = ""
    TEMP_DOWNLOAD_DIRECTORY = "./"
    HEROKU_APP_NAME = None
    HEROKU_API_KEY = None
    INFOPIC = True
    TIME_API_KEY = "awoo"
    WALL_API = "awoo"
    BL_CHATS = []
    SPAMMERS = None
    REM_BG_API_KEY = "xYCR1ZyK3ZsofjH7Y6hPcyzC"
    OPENWEATHERMAP_ID = "887da2c60d9f13fe78b0f9d0c5cbaade"


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
