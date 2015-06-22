""" Data Structures """
# graph theory approach
graph = {'a':['h', 'l'],
         'b':['k', 'm', 'i'],
         'c':['f','j','l','n'],
         'd':['g','m','o'],
         'e':['h','n'],
         'f':['c','m','1'],
         'g':['d','n','2'],
         'h':['a','e','k','o','1','3'],
         'i':['b','l','2'],
         'j':['c','m','3'],
         'k':['b','h','2'],
         'l':['a','c','i','3'],
         'm':['b','d','f','j'],
         'n':['c','e','g','1'],
         'o':['d','h','2'],
         '1':['f','h','n'],
         '2':['g','i','k','o'],
         '3':['h','j','l']}

graphSet = {'a':set(['h', 'l']),
         'b':set(['k', 'm', 'i']),
         'c':set(['f','j','l','n']),
         'd':set(['g','m','o']),
         'e':set(['h','n']),
         'f':set(['c','m','1']),
         'g':set(['d','n','2']),
         'h':set(['a','e','k','o','1','3']),
         'i':set(['b','l','2']),
         'j':set(['c','m','3']),
         'k':set(['b','h','2']),
         'l':set(['a','c','i','3']),
         'm':set(['b','d','f','j']),
         'n':set(['c','e','g','1']),
         'o':set(['d','h','2']),
         '1':set(['f','h','n']),
         '2':set(['g','i','k','o']),
         '3':set(['h','j','l'])}
# vowel list
vowels = ['a','e','i','o']
nodes = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','1','2','3']

""" Functions """
# edge list (not used)
def getEdges(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))
    return edges

# currently no vowel constraints
def getPossiblePaths(graph, start, n, limit, visited, total):
    visited.append(start)
    if(n == limit):
        #print(visited)
        total.append(visited)
        visited.pop()
        return
    for p in graph[start]:
        getPossiblePaths(graph, p, n + 1, limit, visited, total)
    visited.pop()
    return
        
""" Main Function and Conditional """
def main():
    #edgeList = getEdges(graph)
    emptyList = []
    totalList = []
    n = 3
    for start in nodes:
        getPossiblePaths(graph, start, 1, n, emptyList, totalList)
    print(len(totalList))
    validPaths = []
    """
    for path in totalList:
        #print(path)
        vowelCount = 0
        for letter in path:
            if letter in vowels:
                vowelCount += 1
        if vowelCount <= 2:
            validPaths.append(path)
    print(len(validPaths))
    """
if __name__ == "__main__":
    main()
