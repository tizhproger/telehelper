[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/tizhproger/telehelper)
# Telehelper
Userbot based on Theleton with modified modules from FTG

This bot requires PostgreSQL database for storing notes and some config data. Most of variables are saved with Heroku VARS.

Instructions:

1) Create Telegram app (https://core.telegram.org/api/obtaining_api_id)
2) Create private channel and save its name
3) Deploy bot on heroku via button
4) Get PostgreSQL credentials (https://dashboard.heroku.com/apps/your_app_name/resources)
5) Connect to your DB using this credentials
6) Open db_tables.txt document in this repo
7) Copy and paste all creation commands
8) Create all necessary tables in DB
9) Use bot and be happy :)
