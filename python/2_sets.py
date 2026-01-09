set1 = {550,1400,2100,5500}
set2 = {1550,1010,2200,14500}

print(set1,set2) 
union = set1.union(set2) 
print(union)

intersection = set1.intersection(set2)
print(intersection)

#difference 
difference = set1.difference(set2)
print(difference)