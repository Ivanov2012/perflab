import sys
import math

def point_position(circle, point):
    cx, cy, r = circle
    px, py = point
    
    # Вычисляем расстояние от точки до центра окружности
    distance = math.sqrt((px - cx) ** 2 + (py - cy) ** 2)
    
    # Устанавливаем порог для учета погрешностей вычислений
    epsilon = 1e-7
    
    # Определяем положение точки
    if abs(distance - r) < epsilon:
        return 0  # Точка лежит на окружности
    elif distance < r:
        return 1  # Точка внутри окружности
    else:
        return 2  # Точка снаружи окружности

def read_circle(file_path):
    with open(file_path) as file:
        cx, cy = map(float, file.readline().split())
        r = float(file.readline().strip())
        return (cx, cy, r)

def read_points(file_path):
    with open(file_path) as file:
        return [tuple(map(float, line.split())) for line in file]

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)
    
    circle_file = sys.argv[1]
    points_file = sys.argv[2]
    
    circle = read_circle(circle_file)
    points = read_points(points_file)
    
    results = [point_position(circle, point) for point in points]
    
    for result in results:
        print(result)