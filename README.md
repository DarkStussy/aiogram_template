# DESCRIPTION

Very simple aiogram bot template. Reference and idea: https://github.com/Tishka17/tgbot_template

Stack: aiogram, PostgreSQL (SQLAlchemy + asyncpg), aioschedule, redis.

# How to use

### 1. Create and activate virtual environment
### 2. Then install requirements

```
python install -r requirements.txt
```

### 3. Rename .env.example to .env and edit file

```
BOT_TOKEN=  <-(Here bot token from BotFather

PG_HOST=localhost
PG_USERNAME=postgres
PG_PASSWORD= <-(your postgres password)
PG_DATABASE= <-(here database name)
```

### 4. Change admin IDs in config.py (line 34)

### 5. Now start bot to check
```
python app.py
```

