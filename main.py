import telebot
from telebot import types
from api_utils.get_state import get_state

from credentials import chat_id, api_key, username, password
from errors.BadResponse import BadResponse
from errors.JobError import JobError
from errors.StateError import StateError
from utils.convert_time import convert_time
from utils.create_btns import create_default_btns
from utils.get_temp import get_temp
from api_utils.get_frame import get_frame
from api_utils.get_job import get_job

bot = telebot.TeleBot(api_key)

heat_state_dict = {
    1: "🟠",
    0: "🟢",
    -1: "🔵"
}

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btns = create_default_btns()
    markup.add(*btns)
    bot.send_message(message.chat.id, text="Initialization of Ender 3 S1 printer system confirmed.\nOperational status: ready ✅\nFurther directives can be provided upon request 🫡", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "ℹ️ Job info"):
        try:
            state, arr_info = get_job()
            if(state == "Operational"):
                bot.send_message(message.chat.id, text="🔵 State: Operational\nReady to print")
            elif(state == "Printing"):
                arr_info[1] = convert_time(arr_info[1])
                arr_info[2] = convert_time(arr_info[2])
                arr_info[3] = convert_time(arr_info[3])
                bot.send_message(message.chat.id, text="🟡 State: Printing\nFile name: {}\nEstimated time: {}\nPrinting/Left: {}/{}".format(*arr_info))
            else:
                bot.send_message(message.chat.id, text="🔵 State: {}".format(state))
        except BadResponse as e:
            bot.send_message(message.chat.id, text="❌ Negative. Response error {}".format(e.code))
        except JobError as e:
            bot.send_message(message.chat.id, text="❌ Negative\nError: {}\nState: {}".format(e.message, e.state))
        except Exception:
            bot.send_message(message.chat.id, text="❌ Negative\nRuntime error")

    elif(message.text == "🖨 Printer state"):
        try:
            bed_info, tool_info = get_state()
            bot.send_message(message.chat.id, text="Bed {} | Tool {}\nCurrent temp: {} | {}\nTarget temp: {} | {}".format(
                    heat_state_dict[bed_info[0]], heat_state_dict[tool_info[0]],
                    bed_info[1], tool_info[1],
                    bed_info[2], tool_info[2]
                    )
                )
        except BadResponse as e:
            bot.send_message(message.chat.id, text="❌ Negative. Response error {}".format(e.code))
        except StateError as e:
            bot.send_message(message.chat.id, text="❌ Negative\nError: {}".format(e.message))
        except Exception:
            bot.send_message(message.chat.id, text="❌ Negative\nRuntime error")

    elif(message.text == "♨️ CPU temperature"):
        try:
            temp = get_temp()
            bot.send_message(message.chat.id, text="The CPU temp is {}".format(str(temp)))
        except:
            bot.send_message(message.chat.id, text="❌ Negative. Error during temperature measurement")

    elif(message.text == "📸 Get frame"):
        if(str(message.chat.id) == chat_id):
            bot.send_message(message.chat.id, text="✅ Security clearance verified")
            try:
                frame = get_frame()
                bot.send_photo(message.chat.id, frame)
            except Exception as e:
                bot.send_message(message.chat.id, text="❌ Negative. Frame capture unsuccessful. Error {}".format(e.code))
        else:
            bot.send_message(message.chat.id, text="❌ Negative. Security clearance not granted")

    else:
        bot.send_message(message.chat.id, text="❌ Negative. Unknown command")

bot.polling(none_stop=True)
