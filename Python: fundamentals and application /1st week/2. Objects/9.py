n = len(objects)
ans = n
for i in range(n):
    for j in range(i):
        if id(objects[i]) == id(objects[j]):
            ans -= 1
            break

print(ans)


# 2nd solution

"""
print(len({id(x) for x in objects}))
"""