import re
import os
from os import environ
from pyrogram import enums
from Script import script
import asyncio
import json
from collections import defaultdict
from pyrogram import Client

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

#main variables
API_ID = int(environ.get('API_ID', '23580732'))
API_HASH = environ.get('API_HASH', '81ca3df48f25d954b2ebef5aec715a73')
BOT_TOKEN = environ.get('BOT_TOKEN', '7754700986:AAGHpruS_VdqYrrJuoZBE4jEX5e1SjVV4Wc')
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1302460619').split()]
USERNAME = environ.get('USERNAME', 'https://telegram.me/irlwolf')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002452376610'))
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS','-1002409821863').split()]
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://irlwolf:9aEpUre0fkmBjHVz@cluster0.jkd3o.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_URI2 = environ.get('DATABASE_URI2', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "irlwolf")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Rahul')
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', '-1002452376610'))
QR_CODE = environ.get('QR_CODE', 'https://envs.sh/wam.jpg')
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]

#this vars is for when heroku or koyeb acc get banned, then change this vars as your file to link bot name
BIN_CHANNEL = int(environ.get('BIN_CHANNEL', ''))
URL = environ.get('URL', '')

# verify system vars
IS_VERIFY = is_enabled('IS_VERIFY', True)
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', ''))
TUTORIAL = environ.get("TUTORIAL", "https://youtube.com/shorts/ghgse-h0-60?si=UY_La7SlfofI378V")
TUTORIAL2 = environ.get("TUTORIAL2", "https://youtube.com/shorts/frHzCXS78AM?si=--0NfhfwZrnkWkW7")
TUTORIAL3 = environ.get("TUTORIAL3", "https://youtube.com/shorts/frHzCXS78AM?si=--0NfhfwZrnkWkW7")
VERIFY_IMG = environ.get("VERIFY_IMG", "https://graph.org/file/45a270fc6a0a1c183c614.jpg")
SHORTENER_API = environ.get("SHORTENER_API", "zii2MApF3pahz6kNXg9fhTx1iot1")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", "shareus.io")
SHORTENER_API2 = environ.get("SHORTENER_API2", "dc8d1cbea8c19307fbfd4b023f603eba9fb659de")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", "modijiurl.com")
SHORTENER_API3 = environ.get("SHORTENER_API3", "6aa4611571be03be41fbb20298aa5c25a9a8fab1")
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", "shrinkme.io")
TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "3600"))
THREE_VERIFY_GAP = int(environ.get('THREE_VERIFY_GAP', "21600"))

# languages search
LANGUAGES = ["hindi", "english", "telugu", "tamil", "kannada", "malayalam"]

auth_channel = environ.get('AUTH_CHANNEL', '-1002470891127')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', '-1002452479026'))

# bot settings
AUTO_FILTER = is_enabled('AUTO_FILTER', True)
PORT = os.environ.get('PORT', '8080')
MAX_BTN = int(environ.get('MAX_BTN', '8'))
AUTO_DELETE = is_enabled('AUTO_DELETE', True)
DELETE_TIME = int(environ.get('DELETE_TIME', 600))
IMDB = is_enabled('IMDB', False)
FILE_CAPTION = environ.get('FILE_CAPTION', f'{script.FILE_CAPTION}')
IMDB_TEMPLATE = environ.get('IMDB_TEMPLATE', f'{script.IMDB_TEMPLATE_TXT}')
LONG_IMDB_DESCRIPTION = is_enabled('LONG_IMDB_DESCRIPTION', False)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False)
SPELL_CHECK = is_enabled('SPELL_CHECK', True)
LINK_MODE = is_enabled('LINK_MODE', True)
PM_SEARCH = is_enabled('PM_SEARCH', False)
