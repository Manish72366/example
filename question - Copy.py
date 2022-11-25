def triplets_with_sum(number):
    list = []
    for i in range (1 , number - 4):
        if (3*i + 3 > number ): # so i < j < k therefore minimum condition is k = j + 1 and i = j + 1 so if number > i + j + k = 3i + 3 so stop 
            break
        else :
            for j in range ( i + 1 , number - 3):
                k = number - j - i
                if ( (i**2 + j**2 == k**2 ) ):
                    list.append([i,j,k]) 
                else :
                    continue
    return list

print(triplets_with_sum(30000))

