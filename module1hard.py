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
list_= list(students)
list_.sort()
a2 = list_[0]
b2 = list_[1]
c2 = list_[2]
d2 = list_[3]
f2 = list_[4]
dict_=dict()
dict_[a2]= sumofelement1
dict_[b2]= sumofelement2
dict_[c2]= sumofelement3
dict_[d2]= sumofelement4
dict_[f2]= sumofelement5
print(a2)
print(list_)
print(dict_)


