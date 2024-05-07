from info import MAX_USER_STT_BLOCKS,MAX_USER_TTS_SYMBOLS
import logging
import math
from info import LOGS, MAX_USERS, MAX_USER_GPT_TOKENS
from db import count_users, count_all_limits
from gpt import count_gpt_tokens

# настраиваем запись логов в файл
logging.basicConfig(filename=LOGS, level=logging.ERROR, format="%(asctime)s FILE: %(filename)s IN: %(funcName)s MESSAGE: %(message)s", filemode="w")

# получаем количество уникальных пользователей, кроме самого пользователя
def check_number_of_users(user_id):
    count = count_users(user_id)
    if count is None:
        return None, "Ошибка при работе с БД"
    if count > MAX_USERS:
        return None, "Превышено максимальное количество пользователей"
    return True, ""

# проверяем, не превысил ли пользователь лимиты на общение с GPT
def is_gpt_token_limit(messages, total_spent_tokens):
    all_tokens = int(count_gpt_tokens(messages)) + int(total_spent_tokens)
    if all_tokens > MAX_USER_GPT_TOKENS:
        return None, f"Превышен общий лимит GPT-токенов {MAX_USER_GPT_TOKENS}"
    return all_tokens, ""

# проверяем, не превысил ли пользователь лимиты на преобразование аудио в текст
def is_stt_block_limit(message, duration):
    user_id = message

    # Переводим секунды в аудиоблоки
    audio_blocks = math.ceil(duration/15) # округляем в большую сторону
    # Функция из БД для подсчёта всех потраченных пользователем аудиоблоков
    all_blocks = count_all_limits(user_id,'stt_blocks') + audio_blocks

    # Проверяем, что аудио длится меньше 30 секунд
    if duration >= 30:
        return duration,'Превышен лимит'

    # Сравниваем all_blocks с количеством доступных пользователю аудиоблоков
    if all_blocks > MAX_USER_STT_BLOCKS:
        return all_blocks,'Превышен лимит'

    return audio_blocks,False

# проверяем, не превысил ли пользователь лимиты на преобразование текста в аудио
def is_tts_symbol_limit(user_id, text):
    all = count_all_limits(user_id, 'stt_blocks') + count_gpt_tokens(text)
    if all > MAX_USER_TTS_SYMBOLS:
        return all,'Превышен лимит'
    return all,False