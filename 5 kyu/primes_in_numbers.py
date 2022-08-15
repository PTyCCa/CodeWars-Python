def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
        primfac.append(n)
    return primfac

def prime_factors(n):
    ls = {
      2: 0, 
      3: 0, 
      5: 0, 
      7: 0, 
      11: 0, 
      13: 0, 
      17: 0, 
      19: 0, 
      23: 0, 
      29: 0, 
      31: 0, 
      37: 0, 
      41: 0, 
      43: 0, 
      47: 0,
      }
    a = primes(n)
    f = []
    for i in a:
        try:
            ls[i] += 1
        except:
            ls[i] = 1
    for i in a:
        if ls[i] == 1:
            f.append('(' + str(i) + ')')
        elif str('(' + str(i) + '**' + str(ls[i]) + ')') not in f:
            f.append('(' + str(i) + '**' + str(ls[i]) + ')')
    return ''.join(f)


def primeFactors_2(n):
    i, j, p = 2, 0, []
    while n > 1:
        while n % i == 0: n, j = n / i, j + 1
        if j > 0: p.append([i,j])
        i, j = i + 1, 0
    return ''.join('(%d' %q[0] + ('**%d' %q[1]) * (q[1] > 1) + ')' for q in p)