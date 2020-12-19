# See question details at projecteuler.net problem #27
import time
start = time.time()

primes = []
n_list = []
list_length = []
a_b_tuple = []

def sieve_eratosthenes(n):
    sieve = [True] * n
    for p in range(2, n):
        if sieve[p]:
            primes.append(p)
            for i in range(p*p, n, p):
                sieve[i] = False

sieve_eratosthenes(10000)

def quad_function(n,a,b):
    output = n*n + a*n + b
    return output

for a in range(-999,1000):
    for b in range(-1000,1001):
        valid_n = []
        for n in range(0, 100):
            if quad_function(n,a,b) in primes:
                valid_n.append(n)
            else:
                if len(valid_n) > 50:
                    n_list.append(valid_n)
                    a_b_tuple.append([a,b])
                else:
                    break
                break

for list in n_list:
    list_length.append(len(list))

a_b_answer = a_b_tuple[list_length.index(max(list_length))]

answer = a_b_answer[0] * a_b_answer[1]

print(answer)

stop = time.time()
print('Time: ', stop - start)