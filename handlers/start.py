from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🛒 Buy Panel", callback_data="buy")],
        [InlineKeyboardButton("💰 Price List", callback_data="price")],
        [InlineKeyboardButton("💳 Payment", callback_data="payment")],
        [InlineKeyboardButton("📞 Contact", callback_data="contact")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
    "🔥 *WELCOME TO BILAL PANEL SHOP* 🔥\n\n"
    "👋 Welcome!\n\n"
    "🛒 Premium Digital Products\n"
    "⚡ Fast Delivery\n"
    "🔒 Secure Payments\n"
    "💬 24/7 Customer Support\n\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "📞 Support: @BILALPANEL3\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n\n"
    "👇 *Choose an option below* 👇",
    reply_markup=reply_markup,
    parse_mode="Markdown"
)