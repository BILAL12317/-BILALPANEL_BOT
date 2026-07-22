from telegram import Update
from telegram.ext import ContextTypes

ADMIN_ID = 5053534694

async def admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    if user_id != ADMIN_ID:
        await update.message.reply_text("❌ You are not authorized to use this command.")
        return

    text = (
        "🛠️ *BILAL PANEL SHOP ADMIN PANEL*\n\n"
        "✅ Admin Login Successful\n\n"
        "📋 Available Features:\n"
        "• 👥 Users\n"
        "• 📦 Orders\n"
        "• 📢 Broadcast\n"
        "• 📊 Statistics\n"
        "• ⚙️ Settings\n\n"
        "🚧 More features will be added in the next update."
    )

    await update.message.reply_text(
        text,
        parse_mode="Markdown"
    )