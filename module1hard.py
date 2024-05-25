grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
a = grades[0]
b = grades[1]
c = grades[2]
d = grades[3]
f = grades[4]
sumofelement1= (sum(a)/len(a))
sumofelement2= (sum(b)/len(b))
sumofelement3= (sum(c)/len(c))
sumofelement4= (sum(d)/len(d))
sumofelement5= (sum(f)/len(f))
dict_=dict()
dict_['Aaron']= sumofelement1
dict_['Bilbo']= sumofelement2
dict_['Johnny']= sumofelement3
dict_['Khendrik']= sumofelement4
dict_['Steve']= sumofelement5
print(dict_)

