# taking the sum of numbers demo
import time
def sum_num(start, end, return_val):
    if(start<=end):
        return_val += start
        start+=1
        return(sum_num(start,end,return_val))
    else:
        return return_val

time_start = time.time_ns()
print(sum_num(1,100,0))
time_end = time.time_ns()
'''
print(time_end - time_start)
Sum = 0
 
for i in range(1,100):
    Sum += i+1

print(time_end - time_start)
'''
