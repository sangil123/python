def calcArea(b,h):
    area = b * h 
    return area

radius = int(input("원의 반지름 : "))
print("반지름이", radius, "인 원의 면적은", area, "입니다.")
recArea = calcArea(base, height)
print("밑변과 높이가", base, height,"인 사각형의 면적은", recArea,"입니다.")
