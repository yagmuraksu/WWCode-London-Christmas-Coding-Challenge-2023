'''This function takes the array length and list of queries.
Each query in the list contains the beginning and the end index 
of the array and what value is going to be added to each element
within the range. Index values start from 1. After the manipulation 
of the array with the queries maximum element is returned.
'''

def arrayManipulation(n, queries):
    arr = [0]*(n+1)

    for a, b, k in queries:
        arr[a-1] += k
        arr[b] -= k

    sum_val = 0
    max_val = 0
    for i in range(len(arr)):
        sum_val += arr[i]
        max_val = max(max_val,sum_val)
        
    return max_val


test_n1 = 5
test_query1 = [[1,2,100],[2,5,100],[3,4,100]]
result1 = arrayManipulation(test_n1,test_query1)
print("Expected maximum: 200 Function maximum: ", result1)
test_n2 = 10
test_query2 = [[1,5,3],[4,8,7],[6,9,1]]
result2 = arrayManipulation(test_n2,test_query2)
print("Expected maximum: 10 Function maximum: ", result2)
test_n3 = 10
test_query3 = [[2,6,8],[3,5,7],[1,8,1],[5,9,15]]
result3 = arrayManipulation(test_n3,test_query3)
print("Expected maximum: 31 Function maximum: ", result3)