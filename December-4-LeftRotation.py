'''This function takes an array and the number of elements to rotate
the array. It returns the new rotated array.
'''
def rotateLeft(d, arr):
    rotated_arr = arr[d:]
    for i in range(len(arr[:d])):
        rotated_arr.append(arr[i])
        
    return rotated_arr

test_array = [1,2,3,4,5]
test_d = 4
rotated_array = rotateLeft(test_d,test_array)
print("Original array: ",test_array)
print("Rotation amount: ",test_d)
print("Rotated array: ",rotated_array)