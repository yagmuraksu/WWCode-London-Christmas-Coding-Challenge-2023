def birthday(s, d, m):
    counter = 0
    for i in range(len(s)):
        subarray = s[i:i+m]
        sum = 0
        for j in range(len(subarray)):
            sum += subarray[j]
        if(sum == d):
            counter += 1
    
    return counter
    
if __name__ == '__main__':
    tests = [[[1,2,1,3,2],3,2],
             [[1,1,1,1,1,1],3,2],
             [[4],4,1]]
    for i in range(len(tests)):
        s = tests[i][0]
        d = tests[i][1]
        m = tests[i][2]

        result = birthday(s, d, m)
        print(f"Test case {i+1}:")
        print("Number of squares in the chocolate: ",s)
        print("Birthday: ",d)
        print("Birth month: ",m)
        print("Number of possible divisions: ",result)
