import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)
from telegram.ext import MessageHandler, filters
from rembg import remove
from io import BytesIO
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

BOT_TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🛒 Buy Panel", callback_data="buy")],
        [InlineKeyboardButton("💰 Price List", callback_data="price")],
        [InlineKeyboardButton("💳 Payment", callback_data="payment")],
        [InlineKeyboardButton("📞 Contact", callback_data="contact")],
    ]

    await update.message.reply_text(
        "👋 Welcome to *BILAL PANEL SHOP*\n\nChoose an option below:",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )
    if query.data == "buy":
        text = "🛒 Buy Panel\n\nSelect your plan."

    elif query.data == "price":
        text = (
            "💰 Price List\n\n"
            "1 Day - ₹60\n"
            "3 Days - ₹130\n"
            "7 Days - ₹220\n"
            "15 Days - ₹460\n"
            "30 Days - ₹700"
        )

    elif query.data == "payment":
        text = "💳 UPI ID:\nmohamedbilal20116-1@okicici"

    elif query.data == "contact":
        text = "📞 Support: @BILALPANEL3"

    else:
        text = "Unknown option."

    await query.edit_message_text(text)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
async def remove_bg(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo = update.message.photo[-1]
    file = await photo.get_file()

    image_bytes = BytesIO()
    await file.download_to_memory(image_bytes)
    image_bytes.seek(0)

    output = remove(image_bytes.read())

    result = BytesIO(output)
    result.name = "removed_bg.png"
    result.seek(0)

    await update.message.reply_document(document=result)
    if query.data == "buy":
        text = "🛒 Buy Panel\n\nSelect your plan."
    elif query.data == "price":
        text = (
            "💰 Price List\n\n"
            "1 Day - ₹60\n"
            "3 Days - ₹130\n"
            "7 Days - ₹220\n"
            "15 Days - ₹460\n"
            "30 Days - ₹700"
        )
    elif query.data == "payment":
        text = "💳 UPI ID:\nmohamedbilal20116-1@okicici"
    elif query.data == "contact":
        text = "📞 Support: @BILALPANEL3"
    else:
        text = "Unknown option."

    await query.edit_message_text(text)
def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.add_handler(MessageHandler(filters.PHOTO, remove_bg))

    print("✅ BILAL PANEL SHOP Bot Started")
    app.run_polling()

if __name__ == "__main__":
    main()