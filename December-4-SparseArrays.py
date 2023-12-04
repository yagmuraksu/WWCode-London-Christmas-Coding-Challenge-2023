'''This function takes an array of strings and an array of queries,
counts how many of each query string exists in array and returns
the list of count of each query.
'''
def matchingStrings(stringList, queries):
    results = [0]*len(queries)
    
    for i in range(len(queries)):
        for j in range(len(stringList)):
            if(stringList[j] == queries[i]):
                results[i] += 1
                
    return results

test_array1 = ['aba', 'baba', 'aba', 'xzxb']
test_query1 = ['aba', 'xzxb','ab']
results1 = matchingStrings(test_array1,test_query1)
print("Test array 1 :",test_array1)
print("Test query 1 :",test_query1)
print("Results 1 :",results1)
test_array2 = ['def', 'de', 'fgh']
test_query2 = ['de', 'lmn','fgh']
results2 = matchingStrings(test_array2,test_query2)
print("Test array 2 :",test_array2)
print("Test query 2 :",test_query2)
print("Results 2 :",results2)
test_array3 = ['abcde', 'sdaklfj', 'asdjf', 'na','basdn','sdaklfj',
               'asdjf','na','asdjf','na','basdn','sdaklfj','asdjf']
test_query3 = ['abcde', 'sdaklfj','asdjf','na','basdn']
results3 = matchingStrings(test_array3,test_query3)
print("Test array 3 :",test_array3)
print("Test query 3 :",test_query3)
print("Results 3 :",results3)