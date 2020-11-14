import schedule
import webbrowser
from bot import alsoc


def also():
    webbrowser.open('https://youtube.com')
    print("completed")


schedule.every(60).seconds.do(also)
schedule.every(60).seconds.do(alsoc)

# schedule.every().wednesday.at('3:50').do()
while 1:
    schedule.run_pending()
