MAX_SYMBOLS = 250
MAX_SYMBOLS_FOR_SESSION = 500

IAM_TOKEN = 't1.9euelZqKns6ajp7OmcjHnYzKm5rPje3rnpWay5bMzY-Xm5PGnsnOjMiOm5jl9Pc2TRdO-e8QbVvo3fT3dnsUTvnvEG1b6M3n9euelZrHzZWJx5vPzJWWi4zPlsiSxu_8xeuelZrHzZWJx5vPzJWWi4zPlsiSxr3rnpWaj4qbjs3OkY-NlJrJnsaZzou13oac0ZyQko-Ki5rRi5nSnJCSj4qLmtKSmouem56LntKMng.gzkYGsitbx9aAzkq0tTQwK3YXJugHcLwYEKJnB5yeS25NLqDBxZilzh-cvX_Z3BkcAKVflHQVABbqOTYYZoYBA'
FOLDER_ID = 'b1g728oi29cantfjoijl'

HOME_DIR = '/home/student/finalProject'

MODEL_TEMPERATURE = 0.7

TOKEN = "6540713603:AAExQI3nPP-zan2D8IHcnD415mxnsT-cv5E"  # token телеграм-бота

MAX_USERS = 3  # максимальное кол-во пользователей
MAX_GPT_TOKENS = 120  # максимальное кол-во токенов в ответе GPT
COUNT_LAST_MSG = 4  # кол-во последних сообщений из диалога

# лимиты для пользователя
MAX_USER_STT_BLOCKS = 10  # 10 аудиоблоков
MAX_USER_TTS_SYMBOLS = 5_000  # 5 000 символов
MAX_USER_GPT_TOKENS = 2_000  # 2 000 токенов

LOGS = rf'{HOME_DIR}\logs.txt'  # файл для логов
DB_FILE = rf'{HOME_DIR}\messages.db'  # файл для базы данных
SYSTEM_PROMPT = [{'role': 'system', 'text': 'Ты веселый собеседник. Общайся с пользователем на "ты". '
                                            'Поддерживай диалог.'
                                           }]  # список с системным промтом


IAM_TOKEN_PATH=f'{HOME_DIR}/creds/iam_token.txt'
FOLDER_ID_PATH=f'{HOME_DIR}/creds/folder_id.txt'
BOT_TOKEN_PATH=f'{HOME_DIR}/creds/bot_token.txt'