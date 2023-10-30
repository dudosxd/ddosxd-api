# ddosxd-api

## Описание

`ddosxd-api` - это Python библиотека для работы с API ddosxd.ru. Библиотека предоставляет как синхронные, так и асинхронные методы для работы с API.

## Установка

Установите библиотеку с помощью pip:

```bash
pip3 install ddosxd-api
```


## Использование

```python
from ddosxdapi import SydneyApi, SydneyApiAsync

# Создайте экземпляр класса с вашим API ключом
api = SydneyApi('your_api_key')

# Используйте методы API
response = api.Chat('model_name', сообщения в формате клоузаи)

# Для асинхронных методов используйте SydneyApiAsync
async_api = SydneyApiAsync('your_api_key')

# Используйте асинхронные методы API
response = await async_api.Chat('model_name', ...)
```


## Методы

Все методы возвращают ответ от API в формате JSON.

- `Chat(model, messages)`
- `Prompt(model, prompt)`
- `Imagine(model, prompt, ar='1:1', negative='Bad quality', userId=0)`
- `Moderate(q, filters=['nsfw'])`
- `ChatStream(model, messages)`
- `PromptStream(model, prompt)`

Больше про API:
https://telegra.ph/Sydney-AI-bot-api-08-22

## Лицензия

MIT

