def kangaroo(x1, v1, x2, v2):
    result ="NO"
    location1 = x1 + v1
    location2 = x2 + v2
    counter = 10000
    while(counter > 0):
        if(location1 == location2):
            result = "YES"
            break
        location1 += v1
        location2 += v2
        counter -= 1
        
    return result

if __name__ == '__main__':
    tests = [[0,3,4,2],[0,2,5,3]]

    for i in range(len(tests)):
        x1 = tests[i][0]
        v1 = tests[i][1]
        x2 = tests[i][2]
        v2 = tests[i][3]

        print(f"Test Case{i+1}:")
        print(tests[i])
        result = kangaroo(x1, v1, x2, v2)
        print(result)
