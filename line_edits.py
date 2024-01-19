def line_edits(s1, s2):
    '''edit distance function line by line using memoise'''
    s1lines = s1.splitlines()
    s2lines = s2.splitlines()
    known = {}
    def edit_dist(s1lines, s2lines, i1, i2):
        if i1 == -1:
            if i2 == -1:
                return []
            return mem(i1, i2-1) + [('I', '', s2lines[i2])]
        if i2 == -1:
            return mem(i1-1, i2) + [('D', s1lines[i1], '')]
        elif s1lines[i1] == s2lines[i2]:
            temp = ('C', s1lines[i1], s2lines[i2])
            return mem(i1-1, i2-1) + [temp]
        else:
            delete = mem(i1-1, i2) + [('D', s1lines[i1], '')]
            insert = mem(i1, i2-1) + [('I', '', s2lines[i2])]
            substitute = mem(i1-1, i2-1) + [('S', s1lines[i1], s2lines[i2])]
            print(delete)
            if len(substitute) <= len(insert):
                if len(substitute) <= len(delete):
                    return substitute
                else:
                    return delete
            elif len(delete) <= len(insert):
                return delete
            else:
                return insert
    def mem(i1, i2):
        if (i1, i2) in known:
            return known[(i1, i2)]
        else:
            known[(i1, i2)] = edit_dist(s1lines, s2lines, i1, i2)
            return known[(i1, i2)]
    return mem(len(s1lines)-1, len(s2lines)-1)

s1 = "Line2\nLine1\n"
s2 = "Line2\n"
table = line_edits(s1, s2)
for row in table:
    print(row)