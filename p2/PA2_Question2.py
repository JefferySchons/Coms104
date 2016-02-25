def find_perfect(n):
    divisor_total = 0
    for i in range(1,n):
        if n%i==0:
            divisor_total =divisor_total +i 
    if divisor_total == n:
        return 'is a perfect number'
    else:
        return 'is not a perfect number'
    
input_number = input("Please input a positive number:")
is_purcfit_number=find_perfect(input_number)
print is_purcfit_number
