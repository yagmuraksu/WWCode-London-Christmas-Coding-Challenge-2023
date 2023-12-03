'''This function takes the number of empty arrays and queries as parameters.
If the query format is 1 x y, it adds the value to the index of array using
idx = (x xor lastAnswer) % n equation.
If the query format is 2 x y, it assigns the value of the array element to 
lastAnswer using
idx = (x xor lastAnswer) % n
idy = y % size(arr[idx]) equations.
The function returns an array answers.
'''
def dynamicArray(n, queries):
    lastAnswer = 0
    arr = [[] for _ in range(n)]
    answers = []

    for i in range(len(queries)):
        if(queries[i][0] == 1):
            idx = (queries[i][1] ^ lastAnswer) % n
            arr[idx].append(queries[i][2])
        elif(queries[i][0] == 2):
            idx = (queries[i][1] ^ lastAnswer) % n
            idy = queries[i][2] % len(arr[idx])
            lastAnswer = arr[idx][idy]
            answers.append(lastAnswer)
            print(lastAnswer)
    return answers

test_n = 2
test_queries = [[1,0,5],
                 [1,1,7],
                 [1,0,3],
                 [2,1,0],
                 [2,1,1]]
print("Test case 1 \nn: {:}\nqueries: {:}".format(test_n,test_queries))
print("Expected return:\n7\n3")
print("Function return:")
answer = dynamicArray(test_n,test_queries)

