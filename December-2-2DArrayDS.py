'''This function takes 2D Array (6x6) as a parameter, 
finds all (16) hourglasses and their sum,
returns the maximum hourglass sum of all.'''

def hourglassSum(arr):
    upper = []
    middle = []
    lower = []
    sum_all = []
    
    for i in range(0,len(arr)):
        for j in range(0,len(arr[i])-2):
            if(i+1 <= 4):
                upper.append(arr[i][j:j+3])
            if(i+1 >= 3 and i+1 <= 6):
                lower.append(arr[i][j:j+3])
        if(i+1 >=2 and i+1 <= 5):
            middle.append(arr[i][1:5])
            
    for i in range(0, len(middle)):
        middle_of_hg = middle.pop()
        for j in range(0,len(middle_of_hg)):
            middle_value = middle_of_hg.pop()
            lower_hg = lower.pop()
            upper_hg = upper.pop()
            sum_of_hg = sum(upper_hg) + middle_value + sum(lower_hg)
            sum_all.append(sum_of_hg)

    return max(sum_all)

test_case1 = [[1,1,1,0,0,0],
              [0,1,0,0,0,0],
              [1,1,1,0,0,0],
              [0,0,2,4,4,0],
              [0,0,0,2,0,0],
              [0,0,1,2,4,0]]
test_case2 = [[1,1,1,0,0,0],
              [0,1,0,0,0,0],
              [1,1,1,0,0,0],
              [0,9,2,-4,-4,0],
              [0,0,0,-2,0,0],
              [0,0,-1,-2,-4,0]]
test_case3 = [[-9,-9,-9,1,1,1],
              [0,-9,0,4,3,2],
              [-9,-9,-9,1,2,3],
              [0,0,8,6,6,0],
              [0,0,0,-2,0,0],
              [0,0,1,2,4,0]]

print("Test case 1 Expected: 19 Found: ",hourglassSum(test_case1))
print("Test case 2 Expected: 13 Found: ",hourglassSum(test_case2))
print("Test case 3 Expected: 28 Found: ",hourglassSum(test_case3))