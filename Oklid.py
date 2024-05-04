import math

def euclidean_distance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

def main():
    points = []
    n = int(input("Kaç nokta gireceksiniz? "))
    
    for _ in range(n):
        x = float(input("X koordinatını giriniz: "))
        y = float(input("Y koordinatını giriniz: "))
        points.append((x, y))
    
    distances = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = euclidean_distance(points[i], points[j])
            distances.append(dist)
    
    print("Hesaplanan mesafeler:", distances)
    if distances:  
        print("En kısa mesafe:", min(distances))

if __name__ == "__main__":
    main()
