#to create dictionary
n=int(input('enter number of elements in a dictionary'))
dict1={}

for i in range(n):
    name=input('enter name of the student:')
    marks=int(input('enter marks of student'))
    dict1[name]=marks


# now to search names from dictionary

search=input('enter a name')

if(search in dict1):
    print('marks of {} is:'.format(name),marks)

else:
    print('{} not found'.format(search))