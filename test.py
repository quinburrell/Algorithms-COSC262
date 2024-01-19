
# Fibonacci Series using  
# Optimized Method 
  
# function that returns nth  
# Fibonacci number  
def fib(n): 
      
    F = [[1, 1], 
         [1, 0]] 
    if (n == 0): 
        return 0
    power(F, n - 1) 
          
    return F[0][0] 
      
def multiply(F, M): 
      
    x = (F[0][0] * M[0][0] + 
         F[0][1] * M[1][0]) 
    y = (F[0][0] * M[0][1] + 
         F[0][1] * M[1][1]) 
    z = (F[1][0] * M[0][0] + 
         F[1][1] * M[1][0]) 
    w = (F[1][0] * M[0][1] + 
         F[1][1] * M[1][1]) 
      
    F[0][0] = x 
    F[0][1] = y 
    F[1][0] = z 
    F[1][1] = w 
          
# Optimized version of 
# power() in method 4  
def power(F, n): 
  
    if( n == 0 or n == 1): 
        return; 
    M = [[1, 1], 
         [1, 0]]; 
          
    power(F, n // 2) 
    multiply(F, F) 
          
    if (n % 2 != 0): 
        multiply(F, M) 
      

def combinations(items, r):
    end_index = r
    start_index = 0
    resultlist = []
    while 1:
        templist = [items[start_index:end_index]]
        resultlist.append(tuple(templist))
        end_index += 1
        if end_index == len(items):
            start_index += 1
            end_index = start_index + r
    
        
def find_pit(seq, index1=0, index2=1):
    if index1 != index2:
        index1 = len(seq) // 2
        if seq[index1] >= seq[index1-1]:
            find_pit(seq, )
        else:
            find_pit(seq[mid:])

def print_shows(show_list):
    current = 0
    result = []
    shows = {}
    for show in show_list:
        shows[show[1] + show[2]] = [show[0], show[1]]
    for i in sorted(shows.keys()):
        temp = shows.get(i)
        if temp[1] >= current:
            current = i
            print("{0}, {1}, {2}".format(temp[0], temp[1], i))

def fractional_knapsack(capacity, items):
    value_dict = {}
    