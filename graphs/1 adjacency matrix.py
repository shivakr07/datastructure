# graph representation
#  n is the number of the nodes
# m is the number of the edges
if __name__ == '__main__':
    # n, m = map(int, input.split())
    n = 5
    edges = [[0,1], [0,4], [1,2], [1,3], [3,4], [1,4]]
    adjmat = [[0 for i in range(n)] for j in range(n)]
    # print(adjmat)
    for i in range(len(edges)):
        u, v = edges[i][0], edges[i][1]
        print(u, v)
        adjmat[u][v] = 1
        adjmat[v][u] = 1
    for i in adjmat:
        print(i)
        
#--------------------------------------------------------------------
    '''
    // for the one based numbering of the nodes
    n = 5
    edges = [[1,2], [1,5], [2,3], [2,4], [4,5], [2,5]]
    adjmat = [[0 for i in range(n)] for j in range(n)]
    # print(adjmat)
    for i in range(len(edges)):
        u, v = edges[i][0], edges[i][1]
        print(u, v)
        adjmat[u-1][v-1] = 1
        adjmat[v-1][u-1] = 1
    for i in adjmat:
        print(i)
    '''
# Note :
#-----------------------------------------------------------------------
'''
pt1>> 
in case of the one based numbering you crete a matrix of the n+1 size or n size but
then you assign the values accoridng to the adjmat[u-1][v-1] and adjmat[v-1][u-1] both
pt2>>
in case of directed graph you make only adjmat[u][v] = 1 only
'''

    