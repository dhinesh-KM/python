from collections import namedtuple
employee=namedtuple("employee",['name','age','sal'])
e=employee("sam",45,50000)
l=employee("Madonna",25,30000)
print(e.name)
print(employee._make(l))
print(e._fields)
print(e._replace(age=50))
print(l.__getnewargs__())