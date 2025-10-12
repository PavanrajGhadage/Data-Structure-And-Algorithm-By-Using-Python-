def dfs(matrix, locations, start_index):
    visited = set()
    stack = [start_index]  # Use a list as a stack for DFS
    order = []

    while stack:
        node = stack.pop()  # Pop from the end (top of stack)
        if node not in visited:
            visited.add(node)
            order.append(locations[node])
            # Add neighbors (reverse order for consistent exploration)
            for neighbor in reversed(range(len(matrix))):
                if matrix[node][neighbor] == 1 and neighbor not in visited:
                    stack.append(neighbor)
    return order


if _name_ == "_main_":
    # Input number of locations
    n = int(input("Enter number of locations: "))
    print("Enter location names (e.g., A B C D):")
    locations = input().split()

    # Initialize adjacency matrix with zeros
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    # Input number of routes
    m = int(input("Enter number of routes: "))
    print("Enter routes as pairs (e.g., A B means route between A and B):")

    for _ in range(m):
        u, v = input().split()
        i = locations.index(u)
        j = locations.index(v)
        matrix[i][j] = 1
        matrix[j][i] = 1  # Undirected graph

    # Print adjacency matrix
    print("\nAdjacency Matrix:")
    print("   " + "  ".join(locations))
    for i in range(n):
        print(locations[i], matrix[i])

    # Input starting location
    start = input("\nEnter the starting location: ")
    start_index = locations.index(start)

    # Perform DFS
    dfs_order = dfs(matrix, locations, start_index)

    # Print visiting sequence
    print("\nDFS visiting sequence:", " --> ".join(dfs_order))
