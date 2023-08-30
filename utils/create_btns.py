from telebot import types

def create_default_btns():
    btn1 = types.KeyboardButton("ℹ️ Job info")
    btn2 = types.KeyboardButton("🖨 Printer state")
    btn3 = types.KeyboardButton("♨️ CPU temperature")
    btn4 = types.KeyboardButton("📸 Get frame")

    return [btn1, btn2, btn3, btn4]
