from telegram import Update
from telegram.ext import ContextTypes

async def buy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🛒 *BILAL PANEL SHOP*\n\n"
        "Available Plans:\n\n"
        "✅ 1 Day - ₹60\n"
        "✅ 3 Days - ₹130\n"
        "✅ 7 Days - ₹220\n"
        "✅ 15 Days - ₹460\n"
        "✅ 30 Days - ₹700\n\n"
        "💳 To order, click Payment and complete your payment."
    )

    if update.message:
        await update.message.reply_text(text, parse_mode="Markdown")
    elif update.callback_query:
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(
            text,
            parse_mode="Markdown"
        )