import txttsp

def new():
    pyobj=txttsp
    file=open(f'C:/Users/Dell/OneDrive/Face_Recognition/Ai_Assistant/features/vesit_info/national_startup_day.txt','r')
    read=file.read()
    pyobj.speak(read)