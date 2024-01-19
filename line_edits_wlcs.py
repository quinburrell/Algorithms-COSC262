def lcs(s1, s2):
    '''a faster iterative version'''
    len_table = {}
    for i1 in range(len(s1)+1):
        for i2 in range(len(s2)+1):
            if i1 == 0 or i2 == 0:
                len_table[(i1, i2)] = 0
            else:
                len_table[(i1, i2)] = max(
                    len_table[(i1, i2-1)], len_table[(i1-1, i2)])
                if s1[i1-1] == s2[i2-1] and len_table[(i1, i2-1)] == len_table[(i1-1, i2)]:
                    len_table[(i1, i2)] += 1
    n, m = len(s1), len(s2)
    result = ''
    while m > 0 and n > 0:
        if len_table[(n, m)] != len_table[(n, m-1)]:
            if len_table[(n, m)] != len_table[(n-1, m)]:
                m -= 1
                result = s2[m] + result
            n -= 1
        else:    
            m -= 1
    return result

def lcs_strings(s1, s2):
    '''makes two strings to show what is common between them'''
    temp_lcs = lcs(s1, s2)
    s1_lcs, s2_lcs, index = '', '', 0
    for c in s1:
        if index < len(temp_lcs) and temp_lcs[index] == c:
            index += 1
        else:
            c = '[[{}]]'.format(c)
        s1_lcs += c
    index = 0
    for c in s2:
        if index < len(temp_lcs) and temp_lcs[index] == c:
            index += 1
        else:
            c = '[[{}]]'.format(c)    
        s2_lcs += c
    return s1_lcs, s2_lcs

def trace_back(i1, i2, known, s1lines, s2lines):
    '''it iterates backwards through the table to find the edit path'''
    result = []
    while i1 != 0 or i2 != 0:
        if i1 == 0:
            result = [('I', '', s2lines[i2-1])] + result
            i2 -= 1             
        elif i2 == 0:
            result = [('D', s1lines[i1-1], '')] + result
            i1 -= 1             
        else:
            if s1lines[i1-1] == s2lines[i2-1]:
                result = [('C', s1lines[i1-1], s2lines[i2-1])] + result
                i1 -= 1
                i2 -= 1  
            else:
                temp = min(known[(i1-1, i2-1)], known[(i1-1, i2)], known[(i1, i2-1)])
                if temp == known[(i1-1, i2-1)]:
                    s1_lcs, s2_lcs = lcs_strings(s1lines[i1-1], s2lines[i2-1])                   
                    result = [('S', s1_lcs, s2_lcs)] + result
                    i1 -= 1
                    i2 -= 1 
                elif temp == known[(i1-1, i2)]:
                    result = [('D', s1lines[i1-1], '')] + result
                    i1 -= 1    
                elif temp == known[(i1, i2-1)]:
                    result = [('I', '', s2lines[i2-1])] + result
                    i2 -= 1    
    return result 

def line_edits(s1, s2):
    '''edit distance function line by line using memoise'''
    #makes two lists of the lines of each argumant string
    s1lines = s1.splitlines()
    s2lines = s2.splitlines()
    known = {}
    def edit_dist(s1lines, s2lines, i1, i2):
        '''determines the edit cost of a s1 to s2'''
        if i1 == 0:
            if i2 == 0:
                return 0
            return mem(i1, i2-1) + 1
        if i2 == 0:
            return mem(i1-1, i2) + 1
        elif s1lines[i1-1] == s2lines[i2-1]:
            return mem(i1-1, i2-1)
        else:
            delete = mem(i1-1, i2) + 1
            insert = mem(i1, i2-1) + 1
            substitute = mem(i1-1, i2-1) + 1
            return min(delete, insert, substitute)
    def mem(i1, i2):
        '''wrapping memoise function'''
        if (i1, i2) in known:
            return known[(i1, i2)]
        else:
            known[(i1, i2)] = edit_dist(s1lines, s2lines, i1, i2)
            return known[(i1, i2)]
    #the program builds the table from the bottem up
    for i1 in range(len(s1lines)+1):
        for i2 in range(len(s2lines)+1):
            mem(i1, i2)
    return trace_back(i1, i2, known, s1lines, s2lines)