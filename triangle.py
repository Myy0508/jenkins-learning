# -*- coding: utf-8 -*-
#!/usr/bin/env python
list2d = [[1,2,3],[4,5,6]]
sum = 0
for i in range(len(list2d)):
    for j in range(len(list2d[0])):
        sum += list2d[i][j]
print(sum)