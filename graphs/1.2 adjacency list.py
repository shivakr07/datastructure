# method-1 [ using list of the list]

'''#In adjacency list representation of graph we can use list in which list size will be equal to the number of vertex present in the graph.

#Index value is considered as vertex and at each index we store a list in which we add all the connected vertices with the current vertex(current index value).

#Method- 2 [ using dictionary ]
#We can also implement adjaceny list by using dictionary and it is easier to understand.
#In a dictionary we assign key values upto number of vertex present in the graph and each key will intially have an empty list as a value.
#Now we will iterate through given set of edges and then assign source and destination in two different variables.
#In graph at source key( graph[source] ) we will add destination and at destination key( graph[destination] ) we will add source.
#
'''

# creating adjacency list for graph

def build_graph(edges, n):
    graph = {}
    
    for i in range(n):
        graph[i] = []
        
    for edge in edges:
        src =  edge[0]
        dest = edge[1]
        
        graph[src].append(dest)
        graph[dest].append(src)
    print(graph)
    return graph

def display_graph(graph):
    for vertex in graph:
        print(str(vertex)+ " -- >", end = " ")
        print(*graph[vertex])

if __name__ == '__main__':
    n = 5
    edges = [[0,1], [0,2], [0,4], [1,2], [1,3], [2,3], [3,4]]
    graph = build_graph(edges, n)
    display_graph(graph)
    

# ---------------------------------------

# creating directed graph 
# it is similar to the undirected graph but you need to remove dest to src edge


# def build_graph(edges, n):
#     graph = {}
    
#     for i in range(n):
#         graph[i] = []
    
#     for edge in edges:
#         source = edge[0]
#         destination = edge[1]
        
#         graph[source].append(destination)
        
#     return graph
            
# def display_graph(graph):
#     for vertex in graph:
#         print(str(vertex)+" -->", end = " ")
#         print(*graph[vertex])

# n = 5
# edges = [[0, 1], [0, 2], [0, 4], [1, 2], [1, 3], [2, 3], [3, 4]]
# graph = build_graph(edges, n)
# display_graph(graph)