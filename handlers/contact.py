from telegram import Update
from telegram.ext import ContextTypes

SUPPORT_USERNAME = "@BILALPANEL3"

async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "📞 *BILAL PANEL SHOP - SUPPORT*\n\n"
        f"👤 Telegram: {SUPPORT_USERNAME}\n\n"
        "💬 Order, payment, panel activation, "
        "all support-ku message pannunga.\n\n"
        "🕒 Support: 24/7"
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