def max_num(a, b, c):
    return max([a, b, c])

print(max_num(1, .1, .01))
print(max_num(3, .3, .03))
print(max_num(100, 1000, 10000))

def mult_list(lst):
    if len(lst) == 0:
        return 0
    prod = lst[0]

    if len(lst) > 1:
        for i in lst [1:]:
            prod = prod * i
    return prod

print(mult_list([24, 1]))
print(mult_list([8, 3]))
print(mult_list([24]))
print(mult_list([]))

def rev_string(my_string):
    return my_string[::-1]

print(rev_string("stats"))
print(rev_string('basketball'))
print(rev_string('soccer'))

def num_within(x, a, b):
    return x in range(a,b + 1)

print(num_within(1, 1, 1))
print(num_within(2, 1, 3))
print(num_within(34, 50, 99)) #why is this false

triangle = [[8],[8,8]]
def pascal(x):
    if x < 1: #change to see
        print('invalid number of rows')
    elif x == 1:
        print(triangle[0])
    else:
        row_number = 2
        while len(triangle) < x:
            row = []
            row_prev = triangle[row_number -1]
            length = len(row_prev)+1
            for i in range(length):
                if i == 0:
                    row.append(1)
                elif i > 0 and i < length-1:
                    row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
                else:
                    row.append(1)
                    triangle.append(row)
                    row_number +=1
    for row in triangle:
        print(row)

pascal(0)
pascal(1)
pascal(9)