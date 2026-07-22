from telegram import Update
from telegram.ext import ContextTypes

UPI_ID = "mohamedbilal20116-1@okicici"

async def payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "💳 *PAYMENT DETAILS*\n\n"
        f"🏦 UPI ID:\n`{UPI_ID}`\n\n"
        "📌 Payment complete pannitu screenshot anuppunga.\n"
        "✅ Admin verify pannitu panel activate pannuvanga.\n\n"
        "📞 Support: @BILALPANEL3"
    )

    if update.message:
        await update.message.reply_text(
            text,
            parse_mode="Markdown"
        )
    elif update.callback_query:
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(
            text,
            parse_mode="Markdown"
        )