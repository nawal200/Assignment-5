##Display numbers from a list using loop
a = [12, 75, 150, 180, 145, 525, 50]
b = []
for i in a:
    if i > 150:
        if i > 500:
            break
        continue
    if i % 5 == 0:
        b.append(i)

print(b)
##
for i in range(5):
    print (i)
else:
    print("done!")
##3
num = 76542
reverse_number = 0
print("Given Number ", num)
while num > 0:
    reminder = num % 10
    reverse_number = (reverse_number * 10) + reminder
    num = num // 10
print("Revere Number ", reverse_number)
##
list1 = [10, 20, 30, 40, 50]
new_list = reversed(list1)
for item in new_list:
    print(item)
##convert two list
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

res_dict = dict(zip(keys, values))
print(res_dict)
##
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
keys = ["name", "salary"]

for k in keys:
    sample_dict.pop(k)
print(sample_dict)
##
sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]

sample_set.update(sample_list )
print(sample_set)
##
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print(set1.intersection(set2))
##
tuple1 = (10, 20, 30, 40, 50)
tuple1 = tuple1[::-1]
print(tuple1)
##
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))

print(tuple1[1][1])

tuple1 = (10, 20, 30, 4)
a, b, c, d = tuple1
print(a)
print(b)
print(c)
print(d)