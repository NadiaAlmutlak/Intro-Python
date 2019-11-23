# Fibonacci sequences
#F(n-1)+F(n-2)

def F(n):
    a = 0
    b = 1
    fib_nums=[a,b]
    if n == 0: return fib_nums[:1] # returns zero
    elif n == 1: return fib_nums #returns zero and one as the only fibonnaci numbers
    else:#create a loop which produces all the placeholding numbers of the sequence and adds it to list
        for i in range (0,n-2):
            a, b = b, a + b
            fib_nums.append(b)
    return fib_nums

#Test Cases
r= F(10)
print(r)

#def compute_fib(n):
 #   a = 0
  #  b = 1
   # fib_num2= [0]
    #for i in range (1,n):
     #   a, b = b, a+b
      #  fib_num2.append(b)
       # print (fib_num2)


#v=8
#print(compute_fib(v))

