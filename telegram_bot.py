from telegram.ext import Updater, CommandHandler
from scraper import coletar_resultados_aviator
from predictor import prever

TOKEN = "SEU_TOKEN_TELEGRAM"

def start(update, context):
    update.message.reply_text("Olá! Envie /prever para obter a previsão do Aviator com IA.")

def prever_tf(update, context):
    dados = coletar_resultados_aviator()
    resultado = prever(dados)
    update.message.reply_text(f"Previsão IA: {resultado}x")

updater = Updater(TOKEN)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("prever", prever_tf))
updater.start_polling()
updater.idle()
