import tkinter # tkinter 모듈 가져오기

# 창 생성 + window 라는 이름 붙이기
window = tkinter.Tk()

# 창에 대한 크기와 제목 정하기
window.title("원하는 제목")
window.geometry("400x400") # 곱하기는 x로 표현함
window.resizable(False, False) # 창 크기를 커서로 바꿀 때의 크기를 말함. false의 경우, 사이즈 고정을 뜻함

# 텍스트 라벨 만들기
label = tkinter.Label(window, text="HELLO TK!") # 라벨 설정하기
label.pack() # 실제 창 안에 표출하기

# 창이 계속 열려있길 원해!이 코드를 실행해야 창이 열림
window.mainloop()

