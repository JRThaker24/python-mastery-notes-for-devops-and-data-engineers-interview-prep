import math

def circle_stats(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

a, c = circle_stats(3)
print(f"Area: {a:.2f}, Circumference: {c:.2f}")
print(f"Area: {round(a, 2)}, Circumference: {round(c, 2)}")