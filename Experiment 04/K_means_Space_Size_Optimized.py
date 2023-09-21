import math

def distance(x, y):return math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)
def extract_coords(coord):return [list(map(int, c.split(','))) for c in coord.replace('(', '').replace(')', '').split(' ')]
coordinates, centroids, old_cluster, iteration = extract_coords('(2,10) (2,5) (8,4) (5,8) (7,5) (6,4) (1,2) (4,9)'), extract_coords('(2,10) (5,8) (1,2)'), [-1] * 8, 1

while True:
    new_clusters, distances_to_centroids = [], []

    for c in coordinates:
        distances = [distance(c, cent) for cent in centroids]
        new_clusters.append(distances.index(min(distances)))
        distances_to_centroids.append(distances)

    for i in range(len(centroids)):
        cluster_coords = [coordinates[j] for j in range(len(new_clusters)) if new_clusters[j] == i]
        if cluster_coords:
            centroids[i] = [sum(x[0] for x in cluster_coords) / len(cluster_coords),
                            sum(x[1] for x in cluster_coords) / len(cluster_coords)]

    if old_cluster == new_clusters: break
    old_cluster, iteration = new_clusters.copy(), iteration + 1

print("Final Centroids:")
for i, c in enumerate(centroids):
    print(f"Centroid {i+1}: ({c[0]:.2f}, {c[1]:.2f})")