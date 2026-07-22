import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

BOT_TOKEN = "8844663921:AAE8xpgYFxXwS3XgNu6IfYXe4Y0XqSiohr0"


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


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

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

    print("✅ BILAL PANEL SHOP Bot Started")
    app.run_polling()


if __name__ == "__main__":
    main()