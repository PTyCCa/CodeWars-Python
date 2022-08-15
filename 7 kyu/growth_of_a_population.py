def call_counter(func):
    def helper(*args, **kwargs):
        helper.calls += 1
  
        return func(*args, **kwargs)
    helper.calls = 0
    return helper


@call_counter
def nb_year(p0, percent, aug, p):
    # your code
    next_p = p0 + int(p0 * (percent / 100)) + aug
    if next_p >= p:
        return nb_year.calls
    
    return nb_year(next_p, percent, aug, p)


def nb_year_2(p0, percent, aug, p, count = 0):
    if (p0 >= p):
        return count
    else:
        count += 1
        pop = p0 + int(p0 * (percent/100)) + aug
        return nb_year(pop, percent, aug, p, count)