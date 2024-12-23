def count_bit_strings(n):
    #base case
    if n==1:
        return 2
    elif n==2:
        return 3
    #intilization first two variable
    a_n_minus_2=2
    a_n_minus_1=3
    
    for i in range(3,n+1):
        a_n = a_n_minus_1 + a_n_minus_2
        a_n_minus_2 = a_n_minus_1
        a_n_minus_1 = a_n
    return a_n_minus_1

result = count_bit_strings(18)
print(f"The number of bit strings of length 18 with no consecutive ones is: {result}")