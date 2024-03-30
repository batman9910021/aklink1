# (c) adarsh-goel
# (c) sudor2spr @Opleech
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', '28167530'))
    API_HASH = str(getenv('API_HASH', '202a9e8b13b7663417ddacc671420ad9'))
    BOT_TOKEN = str(getenv('BOT_TOKEN', '7021038851:AAF2LUbIj6F1Z0w9HDCBryXz9HlVfiXu-3o'))
    name = str(getenv('name', 'aklimik_bot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '180'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1002124078334'))
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '195.154.182.77'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "6440245883").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = str(getenv('APP_NAME'))
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', 'ak_imax_premium'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', '195.154.182.77:8080')) if not ON_HEROKU or getenv('FQDN', '195.154.182.77:8080') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = "https://aklink.akmaxv2.workers.dev/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://abskck:abskck@cluster0.rxmsbtf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', 'Akimaxmovies_0'))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "")).split())) 
