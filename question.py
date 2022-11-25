'''
Sieve of Eratosthenes
'''


def sieve(limit):
    prime = []
    prime = [True for i in range(limit)]
    p = 2
    if limit > 2:
        while (p < limit):
            if prime[p] == True and limit > 2:
                for j in range(2*p, limit, p):
                    prime[j] = False
            p = p + 1
        prime_list = []
        for i in range(2, limit):
            if(prime[i] == True):
                prime_list.append(i)
        return prime_list
    else:
      raise ValueError("Invalid input.")



