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
def getPossiblePaths(graph, start, n, limit, visited, total, vCount):
    visited.append(start)
    if(n == limit):
        if(countVowels(visited) <= 2):
            print(visited) 
            total.append(visited)
        visited.pop()
        return
    for p in graph[start]:
        getPossiblePaths(graph, p, n + 1, limit, visited, total, vCount) 
    visited.pop()
    return

def countVowels(path):
    count = 0
    for letter in path:
        if letter in vowels:
            count+=1
    return count

""" Main Function and Conditional """
def main():
    #edgeList = getEdges(graph)
    emptyList = []
    totalList = []
    n = 10
    for start in nodes:
        getPossiblePaths(graph, start, 1, n, emptyList, totalList, 0)
    print(len(totalList))
    #getPossiblePaths(graph, 'a', 1, n, emptyList, totalList, 0)
    """
    validPaths = []
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
