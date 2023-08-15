def init(data):
    data['first']={}
    data['middle']={}
    data['last']={}

def lookup(data, label, name):
    return data[label].get(name)

def store(data, full_name):
    names = full_name.split()
    if len(names) == 2 : names.insert(1,"")
    labels = 'first', 'middle', 'last'

    for label, name in zip(labels, names):
        people = lookup(data, label, name)
        if people:
            people.append(full_name)
        else:
            data[label][name] = [full_name]

MyNames = {}
init(MyNames)
store(MyNames, 'Magnus Lie Hetland')
store(MyNames, 'Robin Hood')
store(MyNames, 'Robin Locksley')
store(MyNames, 'Mr. Gumby')
store(MyNames, 'Michael M Schumcher')
label = input('输入label:')
name = input('输入想找的名字:')
found = lookup(MyNames, label,name)
print(found)
#for name in MyNames:
#    print("label: "+name)
#    for n in MyNames[name]:
#        if n != "" : print(n)
#    print("\n")
