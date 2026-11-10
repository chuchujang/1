import tkinter as tk
import time

# 1. 메인 창 설정
window = tk.Tk()
window.title("움직이는 공 게임")
window.geometry("600x400")
window.resizable(False, False)

# 2. 캔버스 생성 (공이 그려질 공간)
canvas = tk.Canvas(window, width=600, height=400, bg="white")
canvas.pack()

# 3. 공 생성 (좌측상단 x1, y1, 우측하단 x2, y2, 색상)
ball = canvas.create_oval(10, 10, 40, 40, fill="red")

# 4. 공의 이동 속도 (x축, y축)
x_speed = 3
y_speed = 3

# 5. 애니메이션 루프
while True:
    # 공을 x_speed, y_speed 만큼 이동
    canvas.move(ball, x_speed, y_speed)
    
    # 현재 공의 위치 좌표 가져오기
    pos = canvas.coords(ball)
    
    # 벽 충돌 감지 (pos[0]=좌, pos[1]=상, pos[2]=우, pos[3]=하)
    if pos[0] <= 0 or pos[2] >= 600:
        x_speed = -x_speed  # 좌우 벽에 부딪히면 x축 방향 반전
    if pos[1] <= 0 or pos[3] >= 400:
        y_speed = -y_speed  # 상하 벽에 부딪히면 y축 방향 반전
        
    # 화면 업데이트 및 잠시 대기
    window.update()
    time.sleep(0.01)
