#initial dictionary
dictionary = {'first':[2,1],'second':[2,3],'third':[3,4]}
print 'Initial dictionary:'
print dictionary

print 'Swap the values of the first and third keys'
temp = []
temp=dictionary['first']
dictionary['first']=dictionary['third']
dictionary['third']=temp
print dictionary

print 'Sort the elements of the list with key third'
dictionary['third']=sorted(dictionary['third'])
print dictionary

print 'Add a new key fourth with the value of the key second'
dictionary['fourth']=dictionary['second']
print dictionary

print 'Delete the key/value pair second'
del dictionary['second']

print 'Final Dictionary:'
print dictionary


