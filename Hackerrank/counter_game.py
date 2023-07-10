# n = 132
#  basic logic problem with two auxiliaries
# ---------------------------------------------------

def counterGame(n):
    # Write 
    if n == 1:
        return 'Louise'
    def ispoweroftwo(number):
        return (number & (number - 1)) == 0 and number != 0
    def find_next_power_of_two(number):
        if number <= 0:
            return 0
        power = 0
        while number > 1:
            number >>= 1
            power += 1
        next_power = 1 << power
        return next_power
    # ----------------------------
    count = 0
    while n > 1:
        if ispoweroftwo(n):
            n = n//2 
        else:
            val = find_next_power_of_two(n)
            n = n-val
            
        count += 1
        if n == 1:
            break
    if count % 2 == 0:
        return 'Richard'
    return 'Louise'

# ---------------------

# NOTE 
# if count = 0 means no one has did anything okay so if count -> 1 means Louise done
# means next (Richard so count = 2) means Richard will never give count -> odd 
# so if count is even return Richard else return Louise


# ---------------------------------------------------
# Aux functions
# ----------------------------------------------------
# def find_next_power_of_two(number):
#     if number <= 0:
#         return 0
#     power = 0
#     while number > 1:
#         number >>= 1
#         power += 1
#     next_power = 1 << power
#     return next_power

# ans = find_next_power_of_two(20)
# print(ans)

# def ispoweroftwo(number):
#         return (number & (number - 1)) == 0 and number != 0
    
# ans = ispoweroftwo(16)
# print(ans)