[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/tizhproger/telehelper)
# Telehelper
Userbot based on Theleton with modified modules from FTG

This bot requires PostgreSQL database for storing notes and some config data. Most of variables are saved with Heroku VARS.

Instructions:

1) Create Telegram app (https://core.telegram.org/api/obtaining_api_id)
2) Deploy bot on heroku
3) Get PostgreSQL credentials (https://dashboard.heroku.com/apps/your_app_name/resources)
4) Connect to your DB using this credentials
5) Open db_tables.txt document in this repo
6) Copy and paste all creation commands
7) Create all necessary tables in DB
8) Use bot and be happy :)
