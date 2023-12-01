'''This function takes an array as a parameter and returns reversed version of it.'''

def reverseArray(a):
    reversed_a = []
    for i in range(len(a)-1, -1, -1):
        reversed_a.append(a[i])
    
    return reversed_a

test_array = [1,4,3,2]
print("Test Array: ",test_array)
print("Reversed Array: ",reverseArray(test_array))