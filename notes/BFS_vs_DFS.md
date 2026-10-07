## Sources
- [geeksforgeeks: Difference between BFS and DFS](https://www.geeksforgeeks.org/dsa/difference-between-bfs-and-dfs/)
  
# BFS vs DFS

## BFS: Breadth-First Search

**Idea:** Explore nodes **level by level**.

```text
        A
      /   \
     B     C
    / \   / \
   D   E F   G

BFS: A → B → C → D → E → F → G
```

* Uses a **Queue (FIFO)**
* Explores closest nodes first
* Finds the **shortest path in an unweighted graph**
* Good for:

  * Shortest path
  * Minimum number of moves
  * Level-order tree traversal
  * Finding nodes at a certain distance

**Remember:**

> BFS = Queue = Levels = Shortest unweighted path

---

## DFS: Depth-First Search

**Idea:** Go as **deep as possible**, then backtrack.

```text
        A
      /   \
     B     C
    / \
   D   E

DFS: A → B → D → E → C
```

* Uses a **Stack (LIFO)** or recursion
* Goes deep before exploring another branch
* Good for:

  * Cycle detection
  * Topological sorting
  * Connected components
  * Backtracking
  * Maze/puzzle problems
  * Tree traversals: preorder, inorder, postorder

**Remember:**

> DFS = Stack = Deep = Backtracking

---

## Main Difference

|                          | BFS         | DFS        |
| ------------------------ | ----------- | ---------- |
| Strategy                 | Wide first  | Deep first |
| Data structure           | Queue       | Stack      |
| Shortest unweighted path | Yes         | No         |
| Backtracking             | No          | Yes        |
| Tree levels              | Yes         | No         |
| Topological sort         | Less common | Common     |
| Time                     | O(V + E)    | O(V + E)   |

### Quick decision

**Shortest path / minimum steps?** → BFS

**Explore deeply / backtrack / dependencies?** → DFS

**Connected components?** → Either
