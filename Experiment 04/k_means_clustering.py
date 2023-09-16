import math

def distance(x, y):
    return math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)

coordinates = '(2,3) (4,5) (6,7)'.split(' ')
coordinates = [x.replace('(', '').replace(')', '').split(',') for x in coordinates]
coordinates = [list(map(int, x)) for x in coordinates]


centroids = '(2,3) (1,5) (7,8)'.split(' ')
centroids = [x.replace('(', '').replace(')', '').split(',') for x in centroids]
centroids = [list(map(int, x)) for x in centroids]

cluster = []

for i in range(2):
    new_cluster = []
    for coordinate in coordinates:
        distances = []
        for centroid in centroids:
            distances.append(distance(coordinate, centroid))
        new_cluster.append(distances.index(min(distances)))
        # print(distance)
    print(new_cluster)
