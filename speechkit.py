import requests

from creds import get_creds


IAM_TOKEN, FOLDER_ID = get_creds()
def speech_to_text(data: bytes):

    # Указываем параметры запроса
    params = "&".join([
        "topic=general",  # используем основную версию модели
        f"folderId={FOLDER_ID}",
        "lang=ru-RU"  # распознаём голосовое сообщение на русском языке
    ])


    # Аутентификация через IAM-токен
    headers = {
        'Authorization': f'Bearer {IAM_TOKEN}',
    }

    response = requests.post(f'https://stt.api.cloud.yandex.net/speech/v1/stt:recognize?{params}', headers=headers, data=data)
    # Читаем json в словарь
    decode_data = response.json()

    # Проверяем, не произошла ли ошибка при запросе
    if decode_data.get('error_code') is None:
        return True, decode_data.get('result')
    else:
        return False, 'При запросе в SpeechKit произошла ошибка'

def text_to_speech(text):

    headers = {'Authorization': f'Bearer {IAM_TOKEN}'}
    data = {
        'text': text,
        'folderId': FOLDER_ID,
        'lang': 'ru-RU',
        'voice':'marina',
        'emotion':'whisper',
        'speed':1.5
    }
    url = 'https://tts.api.cloud.yandex.net/speech/v1/tts:synthesize'

    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        return True, response.content
    else:
        return False, "При запросе в SpeechKit возникла ошибка"