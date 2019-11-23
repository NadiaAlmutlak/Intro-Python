import math

def estimate_pi(n):
    result= 0
    for k in range(0,n+1): #formulates the Newton-Euler equation
        numerator = math.pow(2, k)* (math.factorial(k)**2)
        denominator= math.factorial((2*k+1))
        result=result+ numerator/denominator

    result= result*2 # We multiply because pi/2 is equal to the Newton-Euler eq
    return result

def converge_to_pi(t):
    i= 1
    previous_error= None
    done= False

    while not done:
        test= estimate_pi(i)
        error= math.fabs(math.pi-test)
        if error <= t:
            done= True
        else:
            i=i+1

    return i,test


target_error = 0.0000000001
print("Target error = ", target_error)
print("Approximating pi.")
n,v = converge_to_pi(target_error)
print("n = ", n, "v = ", v)
print("difference = ", v - math.pi)