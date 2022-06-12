# Graphs
A graph is a pictorial representation of a set of objects where some pairs of objects are connected by links. The interconnected objects are represented by points termed as vertices, and the links that connect the vertices are called edges

## Challenge
Implement a Graph that takes multiple methods, add nodes, add edges, get nodes, get nodes, size
### Add Node
Time Complexity: O(1)

Space Complexity: O(n)
### Add Edge
Time Complexity: O(1)

Space Complexity: O(n)
### Get Nodes
Time Complexity: O(n)

Space Complexity: O(n)
### Get Neighbors
Time Complexity: O(n)

Space Complexity: O(n)
### Size
Time Complexity: O(1)

Space Complexity: O(1)
## API
### Add Node
A method that adds a node to the graph
    Arguments: value
    Returns: The added node

### Add Edge
A method that adds a new edge between two nodes in the graph
If specified, assign a weight to the edge
Both nodes should already be in the Graph
    Arguments: 2 nodes to be connected by the edge, weight (optional)
    Returns: nothing

### Get Nodes
    Arguments: none
    Returns all of the nodes in the graph as a collection (set, list, or similar)

### Get Neighbors
    Arguments: node
    Returns a collection of edges connected to the given node
    Include the weight of the connection in the returned collection

### Size
    Arguments: none
    Returns the total number of nodes in the graph