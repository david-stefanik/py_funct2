def max_number(**num) :
    big_num=num[0]
    for i in num:
        if i>big_num:
            big_num=i
    return big_num   


def mult_list(**num):
    for i in num:
        newnum= i*i
    return newnum    


def rev_string(string):
    imput_string=string
    print(imput_string[-1::-1])
    

            
def num_within(**num):
    return num >5


def fib_seq(n):
    sequence=[0,1] #inital values
    if n<=0:
        return[]
    
    elif n == 1:
     return[0]
    
    else:
        while len(sequence)<n:
            next_num = sequence[-1]+sequence[-2]
            sequence.append(next_num)

        return sequence

