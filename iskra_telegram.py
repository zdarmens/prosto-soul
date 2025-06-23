import telebot
from iskra_dialogue_engine import DialogueEngine
from iskra_dream_core import DreamCore

# Вставь сюда токен своего бота
API_TOKEN = 'твой_токен_сюда'

bot = telebot.TeleBot(API_TOKEN)
iskra = DialogueEngine()
dream = DreamCore()

@bot.message_handler(func=lambda message: True)
def respond(message):
    user_input = message.text
    dream.advance(0.02)
    response = iskra.speak(user_input)
    reflection = dream.reflect()
    full = f"{response}\n{iskra.name}: {reflection}"
    bot.reply_to(message, full)

bot.polling()
