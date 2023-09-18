# Import the necessary libraries for mathematical operations and rich text formatting.
import math
from rich import print
from rich.table import Table

# Define a function to calculate the Euclidean distance between two points.
def distance(x, y):
    return math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)

# Define a function to extract coordinates from a string in the format '(x1,y1) (x2,y2) ...'.
def extract_coords(coord):
    # Split the input string into a list of coordinate strings.
    coord = coord.split(' ')
    # Remove parentheses and split each coordinate string into x and y values.
    coord = [x.replace('(', '').replace(')', '').split(',') for x in coord]
    # Convert the x and y values to integers and store them as a list of lists.
    return [list(map(int, x)) for x in coord]

# Extract coordinates from the given input strings and store them in lists.
coordinates = extract_coords('(2,10) (2,5) (8,4) (5,8) (7,5) (6,4) (1,2) (4,9)')
centroids = extract_coords('(2,10) (5,8) (1,2)')

# Initialize a list to keep track of the previous cluster assignments.
old_cluster = [-1] * len(coordinates)

iteration = 1
# Perform the K-means clustering algorithm for a maximum of 10 iterations.
while True:
    # Initialize empty lists to store new cluster assignments and distances to centroids.
    new_clusters = []
    distances_to_centroids = []

    # Calculate distances from each data point to all centroids and assign to the nearest one.
    for coord in coordinates:
        distances = []
        for centroid in centroids:
            d = distance(coord, centroid)
            distances.append(d)
        cluster_assignment = distances.index(min(distances))
        new_clusters.append(cluster_assignment)
        distances_to_centroids.append(distances)

    # Create a Rich Table to display the clustering results for this iteration.
    table = Table(title=f"Iteration {iteration}", show_header=True)
    table.add_column("Data Point", style="bold", justify="center")
    table.add_column("X Value", style="bold", justify="center")
    table.add_column("Y Value", style="bold", justify="center")
    
    # Add columns for centroids with formatted labels and centered text.
    for j in range(len(centroids)):
        table.add_column(f"Centroid {j+1} ({centroids[j][0]:.2f}, {centroids[j][1]:.2f})", style="bold", width=13, justify="center")

    # Add columns for old and new cluster assignments with centered text.
    table.add_column("Old Cluster", style="bold", justify="center")
    table.add_column("New Cluster", style="bold", justify="center")

    # Add rows for each data point, including distances to centroids and cluster assignments.
    for j, (x, y) in enumerate(coordinates):
        distances = distances_to_centroids[j]
        table.add_row(f"{j+1}", str(x), str(y), *[f"{d:.2f}" for d in distances], f"{old_cluster[j]+1}", f"{new_clusters[j]+1}")

    # Print the table to visualize the clustering process for this iteration.
    print(table)

    # Update the centroids by calculating the mean of data points in each cluster.
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

    # Check if cluster assignments have converged, and exit the loop if they have.
    if old_cluster == new_clusters:
        break
    else:
        old_cluster = new_clusters.copy()

# Display the final centroids after clustering.
print("Final Centroids:")
for i, centroid in enumerate(centroids):
    print(f"Centroid {i+1}: ({centroid[0]:.2f}, {centroid[1]:.2f})")
