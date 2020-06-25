# Modelling with Graphs

## Part A

### Question A.1

Create a file `greedy_col_basic.py` such that, when run:

- it visits the vertices of the input graph sequentially in the order 1, 2, 3, 4, …

  - (i.e. regardless of whether the next visited node is adjacent or not to any of the previously visited nodes),

- at every step it assigns (in a greedy fashion) to the currently visited node the smallest possible color such that no two adjacent nodes receive the same color, and

- it outputs the constructed coloring and the number `kmax` of the different colors in this coloring.

### Question A.2

Create a file `greedy_col_variation.py` such that, when run:

- it visits the vertices of the input graph in such an order that always the next visited node is adjacent to at least one previously visited node,

- among all such vertices, the algorithm visits at every step the
vertex that is labeled with the smallest integer,

- at every step it assigns (in a greedy fashion) to the currently visited vertex the smallest possible color such that no two adjacent nodes receive the same color, and

- it outputs the constructed coloring and the number `kmax` of the distinct colors in this coloring.

## Part B

### Question B.1

Create a file `breadth_first.py` with a function `bfs(G, a, b)` such that, when run:

- it performs a Breadth-First Search (BFS), starting from node `a` and ending when it reaches node `b`, and

- it outputs the `distance` (i.e. the length of a shortest path) between the given pairs of nodes for `graph6.py` &ndash; `graph10.py`.

### Question B.2

Create a file `depth_first_pair_nodes.py` with a function `dfs(G, a, b, u)` such that, when run:

- it performs a Depth-First Search (DFS), starting from node `a` and ending when it reaches node `b`,

- at every step, among the neighbors of the currently visited vertex, the algorithm chooses the smallest one (i.e. the vertex that is labeled with the smallest integer) to continue the exploration from it, and

- it adds a label to each of the visited nodes, such that if a vertex `v` receives the label `i`, then this Depth-First Search has reached vertex `v` with a path of length `i` (starting form `a`);

  - note that the label of vertex `a` is 0.

### Question B.3

Create a file `diameter.py` such that, when run:

- it outputs the greatest distance between any pair of vertices in the input graph

  - (i.e. the `diameter` of the input graph).
