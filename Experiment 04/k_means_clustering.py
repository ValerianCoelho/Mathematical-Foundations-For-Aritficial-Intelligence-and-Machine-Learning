import math

def distance(x, y):
    return math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)

coordinates_str = '(2,10) (2,5) (8,4) (5,8) (7,5) (6,4) (1,2) (4,9)'
coordinates_str = coordinates_str.split(' ')
coordinates = [x.replace('(', '').replace(')', '').split(',') for x in coordinates_str]
coordinates = [list(map(int, x)) for x in coordinates]

centroids_str = '(2,10) (5,8) (1,2)'
centroids_str = centroids_str.split(' ')
centroids = [x.replace('(', '').replace(')', '').split(',') for x in centroids_str]
centroids = [list(map(int, x)) for x in centroids]

clusters = []

for i in range(5):
    new_clusters = []
    for coordinate in coordinates:
        distances = []
        for centroid in centroids:
            distances.append(distance(coordinate, centroid))
        new_clusters.append(distances.index(min(distances)))
    
    for i in range(len(centroids)):
        sum_x = 0
        sum_y = 0
        count = 0
        for j in range(len(new_clusters)):
            if new_clusters[j] == i:
                sum_x += coordinates[j][0]
                sum_y += coordinates[j][1]
                count += 1
        if count > 0:
            centroids[i][0] = sum_x / count
            centroids[i][1] = sum_y / count

print(new_clusters)