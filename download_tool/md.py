from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN="6898159215:AAFgUwjN2-t-w8dYQz_maETKushzStgzEwA"
proxy_url = 'http://131.186.37.99:8080'
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')
app = ApplicationBuilder().token(TOKEN).proxy(proxy_url).build()
app.add_handler(CommandHandler("hello", hello))
app.run_polling()

