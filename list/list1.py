list =  [1, 3, 5, 6, 3, 5, 6, 1]
unique_list=set(list)

print(len(unique_list))
print(unique_list)
a=1
for x in unique_list:
    a*=x
print("product of unique list",a)

            
        