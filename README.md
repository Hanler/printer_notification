# 3D printer notification system

### About

The project makes it easier to **control the 3D printing process**. Together with **OctoPrint**, the **notification.py** module sends a **notification message** about the finished printing via the **Telegram bot**. The **main.py** module provides access to important information about the **printer's state**, **current job**, and the Raspberry Pi server's **CPU temperature**. It's also possible to **obtain a frame** from the Raspberry Pi's camera via the Telegram bot.

### Used hardware and software:
- **Raspberry Pi 3B** with the installed **OctoPi** OS
- **OctoPrint** software
- **Telegram bot** from this repository that runs on a Raspberry server
- **Cooler soft** - my mini soft to control the Raspberry's fan [also public on my github](https://github.com/Hanler/cooler_soft)
