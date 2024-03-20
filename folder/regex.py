import re
str1='KDeoALOklOOHserfLoAJSIskdsf'
str2="this,is!an,example\nof:the&split"

print(re.sub("[a-z]",'',str1))
print(re.split(":|,|\n|!|&",str2))
print(re.findall("is",str2))
x=re.search(r"\Bis",str2)
print(x.span())