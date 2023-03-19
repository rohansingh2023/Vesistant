import datetime

def date():
    try:
        date = datetime.datetime.now().strftime("%b %d %Y")
    except Exception as e:
        print(e)
        date = False
    return date

def time():
    strTime=datetime.datetime.now().strftime("%H:%M:%S")
    return strTime