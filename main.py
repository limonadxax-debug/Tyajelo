import telebot
import requests
import os

TOKEN = os.getenv("8398346820:AAGg38kxnby3igtKWlVSq-dIX22-_xPn8zo")
HF_TOKEN = os.getenv("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")

bot = telebot.TeleBot(TOKEN)

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

@bot.message_handler(func=lambda message: True)
def chat(message):
    try:
        payload = {
            "inputs": f"<s>[INST] Ты дружелюбный чат-бот как в character.ai. Отвечай живо и по-человечески.\nПользователь: {message.text} [/INST]"
        }
        response = requests.post(API_URL, headers=headers, json=payload, timeout=60)
        data = response.json()

        if isinstance(data, list) and len(data) > 0:
            bot.reply_to(message, data[0]["generated_text"])
        else:
            bot.reply_to(message, "Хм, модель сейчас тупит 🤔 Попробуй ещё раз")
    except Exception as e:
        bot.reply_to(message, "Ошибка 😢 Проверь токен Hugging Face или попробуй позже")

bot.polling()

