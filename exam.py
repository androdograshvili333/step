
num_1 = 100
print(type(num_1),num_1)

# float

num_2 = 100.1
num_3 = 200.4
add_number = num_2 + num_3
print(type(add_number), add_number)

# string

contry = "georgia"
print(type(contry),contry)

# boolean

x_1 = 100
y_1 = 200
print(x_1 < y_1)
print(x_1 > y_1)


# exam 2 --------------------
year_birth = input("ჩაწერე დაბადების წელი : ")
year_1 = 2025  - int(year_birth)
print("დაახლოებითი ასაკი იქნება: ",year_1)


# exam 3 -------------
number_1 = int (input("ჩაწერე რიცხი"))

print(number_1 > 0, "დადებითია")
print(number_1 < 0, "უარყოფითია")
print(number_1 == 0, "ტოლია")
print(number_1 % 2, " თუ ნაშთი ნულია, ლუწია" )
print(number_1 % 2, " თუ ნაშთი 1, კენტია" )