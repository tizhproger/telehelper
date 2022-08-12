[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/tizhproger/telehelper)
# Telehelper
Userbot based on Theleton with modified modules from FTG

This bot requires PostgreSQL database for storing notes and some config data. Most of variables are saved with Heroku VARS.

Instructions:

1) Create Telegram app (https://core.telegram.org/api/obtaining_api_id)
2) Create private channel and save its name
3) Obtain session string with script: (https://colab.research.google.com/drive/1v8KpiYpui3XuGretQj5DX7zugh4GufZp?usp=sharing)
4) Deploy bot on heroku via button
5) Get PostgreSQL credentials (https://dashboard.heroku.com/apps/your_app_name/resources)
6) Connect to your DB using this credentials
7) Open db_tables.txt document in this repo
8) Copy and paste all creation commands
9) Create all necessary tables in DB
10) Run your app on heroku (https://dashboard.heroku.com/apps/your_app_name/resources)
11) Use bot and be happy :)
