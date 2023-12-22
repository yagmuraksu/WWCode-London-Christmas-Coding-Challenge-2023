def countApplesAndOranges(s, t, a, b, apples, oranges):
    count_apples = 0
    count_oranges = 0
    for i in range(len(apples)):
        apples[i] += a
        if(apples[i]>= s and apples[i]<= t):
            count_apples += 1
    for i in range(len(oranges)):
        oranges[i] += b
        if(oranges[i]>= s and oranges[i]<= t):
            count_oranges += 1

    print(count_apples)
    print(count_oranges)

if __name__ == '__main__':
    s = 7
    t = 11

    a = 5
    b = 15

    apples = [-2,2,1]
    oranges = [5,-6]

    countApplesAndOranges(s, t, a, b, apples, oranges)
