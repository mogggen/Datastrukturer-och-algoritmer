WARNING: The instructions and steps found in the content may be, intentionally or not, bias.

1. Find all concepts and key-words that shows up in the exams.
2. Understand the questions, and describe them in details step-by-step.
3. Update the category for better mangement and organization.

----------------------------------------
---------- Sorting algoritm ------------
----------------------------------------

Ω(Omega notation) = best case
Θ(Theta notation) = average case
O(big-O notation) = worst case (this is ordo, O(n), n -> inf in Computer Science)

------------------------------------------------------------------------------------------------------------------------

BubbleSort

Description: The sorting-algortihm start at the beginning traversing the list swapping adjacent elements of the
list that is in incorrect order, it traverses the list until the algortims has made an entire traversal without
finding any out of order pairs.

https://www.youtube.com/watch?v=nmhjrI-aW5o
Ω(n)
Θ(n^2)
O(n^2)

------------------------------------------------------------------------------------------------------------------------

bucketSort
https://www.youtube.com/watch?v=VuXbEb5ywrU
Ω(n)
Θ(n)
O(n)

Description: BucketSort starts by creating the same number of buckets as there are elements in the
array we want sorted. The algorithm checks the value of the  first decimal smaller than zero, and
places it in the corresponding bucket. If a bucket already has a value a linked list will form from
that bucket. When all the values from the array is put into each bucket, the buckets are sorted, and
then emptied back into the array from first bucket to last. BucketSort is used (primarly) to sort
floating-point numbers.

------------------------------------------------------------------------------------------------------------------------

countingSort
https://www.youtube.com/watch?v=7zuGmKfUt7s
https://www.youtube.com/watch?v=1mh2vilbZMg




O(n+k) k = range of input.


Insertion Sort
https://www.youtube.com/watch?v=OGzPmgsI-pQ
Ω(n)
Θ(?)
O(n^2)

Selection Sort
https://www.youtube.com/watch?v=xWBP4lzkoyM
Ω(n)
Θ(?)
O(n^2)

Radix Sort
https://www.youtube.com/watch?v=nu4gDuFabIM
Ω(n)
Θ(?)
O(n + e) e = the base to sort in

heapSort
https://www.youtube.com/watch?v=MtQL_ll5KhQ
data structure: transform and conquer
Θ(theta): 

merge Sort
data structure: divide and concuquer
Θ(theta): 

----------------------------------------
--------------- Searches ---------------
----------------------------------------

binary search - O(log n)

linear search - O(n)


----------------------------------------
------------ Data structures -----------
----------------------------------------
bineary search tree
Lists (array[], vector<>)
Stacks (List, linked)
Queues (List, linked)
Linked Lists (singly, doubly)
Trees (2-3, balanced(Red-black, 2-3), binary)
Graph (adjacency list, adjacency matrix) https://www.youtube.com/watch?v=DBRW8nwZV-g
Heap (min/max)
Hash map/tables

singelton element
----------------------------------------
--------------- Graphs -----------------
----------------------------------------
Directed Acyclic Graphs (DAG) - a graph with one-way-edges and no cycles. Meaning you can't end up at a previous node in a given number of traversal.

------------------------------------------------------------------------------------------------------------------------

Dijkstra's algorithm - https://www.youtube.com/watch?v=pVfj6mxhdMw

Description:
Start with all the lengths at infinite length. And starting Node at zero.

Move to neigbouring nodes, with shortest path, and compute the new distances from the new node, starting with the shortest, and sort shortest through longest.
Continue until with the node that has the shortest distance the end vertices is reached.
storing the vertices that the algrithm arrived from. In doing so gives the entire path.
(see video)

Calulating the shortest path to the end node, also gives the shortest path to all the nodes contained in the graph.

------------------------------------------------------------------------------------------------------------------------

adjacency matrix - The edges will go from the vertically listed nodes, on the left, to the horizontally listed, at the top.
adjacency list - an array with all the nodes of the graph, were every element has in the list has a linked list with it's neighbours.
neighbour - a Node that can be directly visted from currently visited node via an edge.

------------------------------------------------------------------------------------------------------------------------
terminology

current working node - the node that the algorithm is working with at the moment.
discovery time - the first time the node is visited.
finishing time - the last time the node is visited.
every node will be visited exactly 2 times during a search.

topilogical sorting - A topilogical order/sorting can't contain cycles, so it has to be directed. https://en.wikipedia.org/wiki/Topological_sorting

----------------------------------------
--------------- Trees ------------------
----------------------------------------
tree traversals (inorder, pre-order, post-order) - https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/

inorder - left, parent, right
pre-order - parent, left, right
post-order - left, right, root

as a recursive function-call:
order(Node* first, Node* second, Node* third)
if(first->getFirst()) return first->getFirst();
else if(second->getSecond()) return second->getSecond();
else if(third->getThird()) return third->getThird();
return;

binary search tree - a technique that splits the array into smaller halves of itself to find a certain element


BFS & DFS https://www.youtube.com/watch?v=pcKY4hjDrxk

----------------------------------------
--------------- Hashes -----------------
----------------------------------------

Hashing technices: https://m.youtube.com/watch?v=mFY0J5W8Udk

Open hashing/ chaning h(x), add a node on collision
Closed hashing / linear probing: h(x, i)
------------------------------------------------------------------------------------------------------------------------

DFS: When a neighbouring node is visited it is added to the top of a stack to remember the order that the search
traversed. When the newest addition the the stack has no unvisited neighbouring nodes it is poped from the stack
and this is repeated until the stack is empty or a previous node with unvisted neighbours is found.

trick: walking the left-most branch (in-order traversal), counting leafs double, and backtracking will give the correct discovery and finishing time, for DFS

Discovery time = stack.push(Node*)
Finishing time = stack.pop()

------------------------------------------------------------------------------------------------------------------------

BFS: When the neigbouring node is visited it is added to the end of the queue to remember what set of nodes are visited.

discovery time - the first time the node is visited. queue.EnQueue(node*)
finishing time - the last time the node is visited. queue.DeQueue()

------------------------------------------------------------------------------------------------------------------------
