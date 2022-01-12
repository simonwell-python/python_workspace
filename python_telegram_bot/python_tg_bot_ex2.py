import random
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton

hands = ["rock", "paper", "scissors"]

emoji = {"rock": "👊", "paper": "✋", "scissors": "✌️"}


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "剪刀石頭布！",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(emoji, callback_data=hand)
                    for hand, emoji in emoji.items()
                ]
            ]
        ),
    )


def judge(mine, yours):
    if mine == yours:
        return "平手"
    elif (hands.index(mine) - hands.index(yours)) % 3 == 1:
        return "我贏了"
    else:
        return "我輸了"


def play(update: Update, context: CallbackContext) -> None:
    try:
        mine = random.choice(hands)
        yours = update.callback_query.data
        update.callback_query.edit_message_text(
            "我出{}，你出{}，{}！".format(emoji[mine], emoji[yours], judge(mine, yours))
        )
    except Exception as e:
        print(e)


updater = Updater("5040646654:AAH_oyJ1TL7bx04po6QSwTqMgwHDgX3bkRI")

updater.dispatcher.add_handler(CommandHandler("start", start))
updater.dispatcher.add_handler(CallbackQueryHandler(play))

updater.start_polling()
updater.idle()
