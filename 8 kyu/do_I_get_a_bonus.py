def bonus_time(salary, bonus):
    #your code here
    if bonus:
        return "$" + str(salary * 10)
    return f"${salary}"