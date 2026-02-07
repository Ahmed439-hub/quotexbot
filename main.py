import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Railway ke liye better token reading
TOKEN = os.getenv("8336951628:AAFw7Aw9TpFfV2cdkqSx6F4cU9bgFNIV1II") or os.getenv("8336951628:AAFw7Aw9TpFfV2cdkqSx6F4cU9bgFNIV1II")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Assalamualaikum! Bot is running ✅")

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello bhai! Kese ho? 😊")

async def hi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi! Kya haal hai? 🔥")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Commands:\n"
        "/start - Start bot\n"
        "/hello - Hello message\n"
        "/hi - Hi message\n"
        "/help - Help\n\n"
        "Koi bhi text bhejo → main echo kar dunga"
    )

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"You said: {update.message.text}")

def main():
    print("=== Bot Starting ===")
    
    if not TOKEN:
        print("❌ ERROR: TELEGRAM_TOKEN missing!")
        print("Railway Variables mein 'TELEGRAM_TOKEN' add kiya hai? Redeploy kiya?")
        return
    else:
        print(f"✅ Token loaded successfully (length: {len(TOKEN)} chars)")

    app = Application.builder().token(TOKEN).build()

    # Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("hello", hello))
    app.add_handler(CommandHandler("hi", hi))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("🚀 Bot is now running on Railway...")
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
