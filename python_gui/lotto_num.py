# 로또번호 생성 프로그램 만들기

# 자동으로 로또 번호 생성하기
import random

lotto_num = range(1,46)
for i in range(5) : 
    print(random.sample(lotto_num,6))

# tkinter로 표출하기

import tkinter
import tkinter.font
import random

lotto_num = range(1,46)

def buttonClick() : 
    print(random.sample(lotto_num,6))

window=tkinter.Tk()
window.title("lotto")
window.geometry("400x400")
window.resizable(False, False)

button = tkinter.Button(window, overrelief="solid", text="번호 확인", width=15, command=buttonClick, repeatdelay=1000, repeatinterval=100)
button.pack()

# 버튼이 들어갈 부모 창 (window)
# overrelief : 마우스 올렸을 때 버튼 테두리 스타일 (solid = 단단한 선)
# text : 버튼에 표시될 글자
# command : 버튼 눌렀을 때 실행할 함수 이름 (buttonClick)
# repeatdelay : 버튼 누르고 1초(1000ms) 있으면 command 반복 실행 시작
# repeatinterval : command 반복 실행 간격 (100ms마다)

window.mainloop()

# 위 까지 하게되면 생성된 번호가 비주얼스튜디오에만 뜨게 된다. guidp 표출하기 위해서는
import tkinter
import tkinter.font
import random

lotto_num = range(1,46)

def buttonClick() : 
    label = tkinter.Label(window, text=str(random.sample(lotto_num,6)))
    label.pack()

window=tkinter.Tk()
window.title("lotto")
window.geometry("400x400")
window.resizable(False, False)

button = tkinter.Button(window, overrelief="solid", text="번호 확인", width=15, command=buttonClick, repeatdelay=1000, repeatinterval=100)
button.pack()

window.mainloop()