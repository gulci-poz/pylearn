print(ord('s'))
print(chr(ord('s')))

# manually
res = []
for x in 'spam':
    res.append(ord(x))

print(res)

# apply a function to sequence or other iterable
res = list(map(ord, 'spam'))
print(res)

# apply an arbitrary expression to sequence or other iterable
res = [ord(x) for x in 'spam']
print(res)

# without square brackets we get a generator object
res = [x ** 2 for x in range(10)]
print(res)

# with map, using lambda for inline function
res = list(map((lambda x: x ** 2), range(10)))
print(res)

res = []
for x in range(5):
    if x % 2 == 0:
        res.append(x)

print(res)

res = list(filter((lambda x: x % 2 == 0), range(5)))
print(res)

res = [x for x in range(5) if x % 2 == 0]
print(res)

# map + filter using list comprehension
res = [x ** 2 for x in range(10) if x % 2 == 0]
print(res)

# the same using map and filter
res = list(map((lambda x: x ** 2), filter((lambda x: x % 2 == 0), range(10))))
print(res)

# additional for-s and if-s
res = [x + y + z for x in [100, 200, 300, 400, 500]
    for y in [10, 20, 30, 40, 50]
    for z in range(10) if z % 2 == 0]
print(res)

res = [(x, y) for x in range(10)
    for y in range(10) if x == y]
print(res)

# helpdesk example
row1 = {"id": "0", "company": "hp", "device": "laser printer"}
row2 = {"id": "1", "company": "hpe", "device": "router"}
row3 = {"id": "2", "company": "intel", "device": "processor"}
row4 = {"id": "3", "company": "hp", "device": "printer"}
row_lst = [row1, row2, row3, row4]

# query_str = "hp printer las"
# query_str = "int proc"
query_str = "hp t"
query_lst = query_str.split(" ")

# ver. 1
# single word per column version
res = [row for row in row_lst if set(query_lst).issubset(row.values())]
# print(res)

# ver. 2
# a few words per column version
# data in a single column may contain a few words, we have to split each column
# as the level of complication of a single comprehension grows,
# we split it in a few comprehensions
row_refined = []
for row in row_lst:
    row_refined.append([v for val in row.values() for v in val.split(' ')])

res_indexes = [row_refined.index(row) for row in row_refined if set(query_lst).issubset(row)]
res_rows = [row_lst[i] for i in res_indexes]
# print(res_rows)

# ver. 3
# going further, we should search substrings (words from query_lst) in each word
row_refined = []
for row in row_lst:
    row_refined.append([v for val in row.values() for v in val.split(' ')])

rows = []
for row in row_refined:
    word_count = 0
    for val in row:
        for word in query_lst:
            if val.find(word) >= 0:
                word_count += 1
    if word_count >= len(query_lst):
        # we return original dictionaries,
        # we match indexes of the original list and the refined one
        rows.append(row_lst[row_refined.index(row)])

print(rows)

M = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

N = [[2, 2, 2],
    [3, 3, 3],
    [4, 4, 4]]

res = [row[1] for row in M]
print(res)

res = [M[row][1] for row in (0, 1, 2)]
print(res)

# diagonal
# we generate a list of offsets (numbered rows)
res = [M[i][i] for i in range(len(M))]
print(res)

# 2nd diagonal
res = [M[i][len(M) - 1 - i] for i in range(len(M))]
print(res)
