class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 8117180
    API_HASH = "34ce938c495ce1b2ae0e97fb237e8695"

    CASH_API_KEY = "73STYO8G8T2FWYIT"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://xkktuvotvfgbyd:d42e4a2d16d27e30fb17de003fe69fb080e340d50367e3ed36da136c56c8f411@ec2-52-207-137-57.compute-1.amazonaws.com:5432/d5ms5utuhj2agc"  # A sql database url from elephantsql.com

    EVENT_LOGS = ()  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://zewdatabase:ijoXgdmQ0NCyg9DO@zewgame.urb3i.mongodb.net/ontap?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://graph.org/file/6ed3863209d0be9c968de.jpg"

    SUPPORT_CHAT = "agoraworld"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = ""  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "wget -N monitoring.platform360.io/agent360.sh && bash agent360.sh 6419a758575ecc59860d6f97"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 6181817811  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = 6181817811 5876293679 6121546292 6272710217 2022350202  # User id of sudo users
    DEV_USERS = 6181817811 5876293679 6121546292 6272710217 2022350202  # User id of dev users
    DEMONS = 6181817811 5876293679 6121546292 6272710217 2022350202  # User id of support users
    TIGERS = 6181817811 5876293679 6121546292 6272710217 2022350202  # User id of tiger users
    WOLVES = 6181817811 5876293679 6121546292 6272710217 2022350202  # User id of whitelist users

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
