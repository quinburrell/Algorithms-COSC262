def lcs1(s1, s2):
    ''' finds the longest common sub string in 2 strings'''
    known = {}
    def longer(string1, string2):
        if len(string1) > len(string2):
            return string1
        else:
            return string2
    def find_substring(i, j):
        if i == -1 or j == -1:
            return ''
        else:
            if s1[i] == s2[j]:
                return mem(i-1, j-1) + s1[i]
            else:
                return longer(mem(i-1, j), mem(i, j-1))
    def mem(i, j):
        if (i, j) in known:
            return known[(i, j)]
        else:
            known[(i, j)] = find_substring(i, j)
            return known[(i, j)]    
    return mem(len(s1)-1, len(s2)-1)

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

def longest_common_subsequence(list1, list2):
    known = {}
    def longer(string1, string2):
        if len(string1) > len(string2):
            return string1
        else:
            return string2
    def find_substring(i, j):
        if i == -1 or j == -1:
            return []
        else:
            if list1[i] == list2[j]:
                return mem(i-1, j-1) + [list1[i]]
            else:
                return longer(mem(i-1, j), mem(i, j-1))
    def mem(i, j):
        if (i, j) in known:
            return known[(i, j)]
        else:
            known[(i, j)] = find_substring(i, j)
            return known[(i, j)]    
    return mem(len(list1)-1, len(list2)-1)    

list1 = [19, 5, 5, 0, 13, 5, 0, 1, 14, 7, 21, 1]
list2 = [19, 5, 5, 0, 20, 8, 5, 0, 7, 21, 19]
print(longest_common_subsequence(list1, list2))
                