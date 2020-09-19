"""
s = input()
a = s.find('h')
b = s.rfind('h')
print(s[:a+1] + s[b-1:a-1:-1] + s[b+1:])
"""

list_to_sort = [24, 45, 2, 3, 2]
print(len(set(list_to_sort)))
