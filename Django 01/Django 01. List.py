# list
# lst = []
# lst = list()

# print(type(lst))
# lst.append(1)
# lst.append(58)
# print(lst)

# lst = ["Salam", 25, 93.5]
# print(lst)

# shallow copy
# list1 = [25, 36]
# list2 = list1

# print(f'list1 = {list1}')
# print(f'list2 = {list2}')
#
# list2[0] = 698
#
# print()
#
# print(f'list1 = {list1}')
# print(f'list2 = {list2}')

# deep copy - v1
# list2 = []
# for i in list1:
#     list2.append(i)
#
# print(f'list1 = {list1}')
# print(f'list2 = {list2}')
#
# list2[0] = 698
#
# print()
#
# print(f'list1 = {list1}')
# print(f'list2 = {list2}')

# deep copy - v2
# list2 = list1.copy()
#
#
# print(f'list1 = {list1}')
# print(f'list2 = {list2}')
#
# list2[0] = 698
#
# print()
#
# print(f'list1 = {list1}')
# print(f'list2 = {list2}')


# # deep copy - v3
# import copy
# list2 = copy.copy(list1)
#
#
# print(f'list1 = {list1}')
# print(f'list2 = {list2}')
#
# list2[0] = 698
#
# print()
#
# print(f'list1 = {list1}')
# print(f'list2 = {list2}')


# deep copy - v4
# list2 = list1[:]
#
#
# print(f'list1 = {list1}')
# print(f'list2 = {list2}')
#
# list2[0] = 698
#
# print()
#
# print(f'list1 = {list1}')
# print(f'list2 = {list2}')

# slice
# lst1 = [25, 36, 98, 65, 774]
# print(lst1[1:3])
# print(lst1[0:5:2])
# print(lst1[:4])
# print(lst1[1:])
# print(lst1[:])
# print(lst1[::-1])

# print(lst1[-1])

# st = "Salam"
# ind = st.find('t')
# print(st.find('t'))
# print(st[ind])

