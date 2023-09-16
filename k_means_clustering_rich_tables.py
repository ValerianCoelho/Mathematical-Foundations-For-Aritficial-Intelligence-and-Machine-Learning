import math
from rich import print
from rich.table import Table

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

for i in range(5):
    new_clusters = []
    distances_to_centroids = []

    for coordinate in coordinates:
        distances = []
        for centroid in centroids:
            d = distance(coordinate, centroid)
            distances.append(d)
        cluster_assignment = distances.index(min(distances))
        new_clusters.append(cluster_assignment)
        distances_to_centroids.append(distances)

    table = Table(title=f"Iteration {i+1}", show_header=True)
    table.add_column("Data Point", style="bold")
    table.add_column("X Value", style="bold")
    table.add_column("Y Value", style="bold")
    table.add_column("Distance to Centroid 1", style="bold")
    table.add_column("Distance to Centroid 2", style="bold")
    table.add_column("Distance to Centroid 3", style="bold")
    table.add_column("Cluster", style="bold")
    table.add_column("New Cluster", style="bold")

    for j, (x, y) in enumerate(coordinates):
        d1, d2, d3 = distances_to_centroids[j]
        cluster = new_clusters[j] + 1
        table.add_row(
            f"Point {j+1}", str(x), str(y), f"{d1:.2f}", f"{d2:.2f}", f"{d3:.2f}", f"{cluster}", f"{new_clusters[j]+1}"
        )

    print(table)

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

print("Final Centroids:")
for i, centroid in enumerate(centroids):
    print(f"Cluster {i+1}: {centroid}")
