def divisibleSumPairs(n, k, ar):
    pairs = []
    for i in range(n):
        for j in range(i,n):
            sub_array = []
            if(i!=j):
                if((ar[i]+ar[j]) % k == 0):
                    sub_array.append(ar[i])
                    sub_array.append(ar[j])
            if(len(sub_array) > 0):
                pairs.append(sub_array)
    return len(pairs)

if __name__ == '__main__':
    n = 6
    k = 3
    ar = [1, 3, 2, 6, 1, 2]

    print("Test Case:")
    print("Array: ",ar)
    result = divisibleSumPairs(n, k, ar)
    print(f"Number of subarray pairs with their sum divisible by {k}: ", result)


