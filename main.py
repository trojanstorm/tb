import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, CallbackContext

BOT_TOKEN = "6791439587:AAF1EY2RbGSoZgvSDGoaTa4InUefttzxe9Q"


# کانال‌هایی که کاربر باید عضو باشه
REQUIRED_CHANNELS = [
    {"name": "کانال اول", "link": "https://t.me/Sensoglitch"},
]

# لینک محتوای ویژه
SPECIAL_LINK = "https://t.me/+KR045CCo-yQyN2Rk"  # می‌تونی لینک دلخواه خودت بذاری

# تابع بررسی عضویت
async def check_membership(user_id, context: CallbackContext):
    not_joined = []
    for ch in REQUIRED_CHANNELS:
        try:
            chat = ch["link"].replace("https://t.me/", "@")
            member = await context.bot.get_chat_member(chat_id=chat, user_id=user_id)
            if member.status in ["left", "kicked"]:
                not_joined.append(ch)
        except:
            not_joined.append(ch)
    return not_joined

# شروع ربات
async def start(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    not_joined = await check_membership(user_id, context)

    if not_joined:
        buttons = [[InlineKeyboardButton(ch["name"], url=ch["link"])] for ch in not_joined]
        buttons.append([InlineKeyboardButton("✅ عضو شدم", callback_data="check_again")])
        reply_markup = InlineKeyboardMarkup(buttons)
        await update.message.reply_text(
            "🚫 شما هنوز عضو همه کانال‌ها نیستید!\n\nلطفاً عضو بشید و بعد روی دکمه «عضو شدم» کلیک کنید 👇",
            reply_markup=reply_markup
        )
    else:
        await send_link(update, context, from_callback=False)

# هندلر دکمه "عضو شدم"
async def button_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    not_joined = await check_membership(user_id, context)

    if not_joined:
        await query.edit_message_text(
            "🚫 هنوز عضو همه کانال‌ها نشدی!\nلطفاً عضو بشو و دوباره امتحان کن."
        )
    else:
        await send_link(update, context, from_callback=True)

# ارسال لینک محتوای ویژه به جای عکس
# ارسال لینک به صورت دکمه شیشه‌ای
async def send_link(update: Update, context: CallbackContext, from_callback=False):
    chat_id = update.effective_chat.id if not from_callback else update.callback_query.message.chat.id

    # دکمه شیشه‌ای با متن دلخواه
    buttons = [
        [InlineKeyboardButton("🔥 تماشای محتوای داغ 🔥", url=SPECIAL_LINK)]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    await context.bot.send_message(
        chat_id=chat_id,
        text="✅ شما عضو همه کانال‌ها هستید! برای مشاهده محتوای ویژه، روی دکمه زیر کلیک کنید:",
        reply_markup=reply_markup
    )


# اجرای ربات
if __name__ == "__main__":
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.run_polling()            member = await context.bot.get_chat_member(chat_id=chat, user_id=user_id)
            if member.status in ["left", "kicked"]:
                not_joined.append(ch)
        except:
            not_joined.append(ch)
    return not_joined

# شروع ربات
async def start(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    not_joined = await check_membership(user_id, context)

    if not_joined:
        buttons = [[InlineKeyboardButton(ch["name"], url=ch["link"])] for ch in not_joined]
        buttons.append([InlineKeyboardButton("✅ عضو شدم", callback_data="check_again")])
        reply_markup = InlineKeyboardMarkup(buttons)
        await update.message.reply_text(
            "🚫 شما هنوز عضو همه کانال‌ها نیستید!\n\nلطفاً عضو بشید و بعد روی دکمه «عضو شدم» کلیک کنید 👇",
            reply_markup=reply_markup
        )
    else:
        await send_link(update, context, from_callback=False)

# هندلر دکمه "عضو شدم"
async def button_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    not_joined = await check_membership(user_id, context)

    if not_joined:
        await query.edit_message_text(
            "🚫 هنوز عضو همه کانال‌ها نشدی!\nلطفاً عضو بشو و دوباره امتحان کن."
        )
    else:
        await send_link(update, context, from_callback=True)

# ارسال لینک محتوای ویژه به جای عکس
# ارسال لینک به صورت دکمه شیشه‌ای
async def send_link(update: Update, context: CallbackContext, from_callback=False):
    chat_id = update.effective_chat.id if not from_callback else update.callback_query.message.chat.id

    # دکمه شیشه‌ای با متن دلخواه
    buttons = [
        [InlineKeyboardButton("🔥 تماشای محتوای داغ 🔥", url=SPECIAL_LINK)]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    await context.bot.send_message(
        chat_id=chat_id,
        text="✅ شما عضو همه کانال‌ها هستید! برای مشاهده محتوای ویژه، روی دکمه زیر کلیک کنید:",
        reply_markup=reply_markup
    )


# اجرای ربات
if __name__ == "__main__":
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.run_polling()
