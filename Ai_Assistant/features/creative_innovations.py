import txttsp

def new():
    pyobj=txttsp
    file=open(f'C:/Users/Dell/OneDrive/Face_Recognition/Ai_Assistant/features/vesit_info/creative_innovations.txt','r')
    read=file.read()
    pyobj.speak(read)