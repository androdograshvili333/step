
# # 1. მომხმარებელს შემოატანინე ასაკი (input() გამოყენებით) და if / elif / else გამოყენებით დაადგინე, რომელი კატეგორიას ეკუთვნის:
# # ბავშვი (0–12)
# # თინეიჯერი (13–19)
# # ზრდასრული (20–64)
# # უფროსი (65+)
# # ბოლოს დაბეჭდე შედეგი, მაგალითად:
# # "თქვენ ხართ: თინეიჯერი"

name = int(input("How old are you>>> "))

if name <= 12:
    print("child")
elif name >= 12 and name <= 19:    
    print("tinager")
elif  name >= 20 and name <= 64:
    print("Adult") 
else :
    print ("old man")     

# #  მომხმარებელს შემოატანინე:
# # ქულა (score)
# # დასწრება პროცენტებში (attendance)
# # სტუდენტი ჩაითვლება ჩაბარებულად მხოლოდ იმ შემთხვევაში, თუ ქულა მეტია 60-ზე და დასწრება მეტია 75-ზე.

# # გამოიყენე and ოპერატორი.
# # დაბეჭდე:
# # "ჩააბარა"
# # ან
# # "ვერ ჩააბარა"    

score  = int(input(" Qula: "))
attedance =  int(input("procenti "))
if score >= 60 and attedance >= 75:
    print("Chaabara")
else:
    print("ver Chabaraa")    




# #   მომხმარებელს ჰკითხე:
# # არის თუ არა სტუდენტი (yes/no)
# # არის თუ არა წევრი (yes/no)

# # ლოგიკა:
# # თუ სტუდენტია ან წევრია → აქვს ფასდაკლება
# # თუ ორივეა (სტუდენტიც და წევრიც) → დამატებითი (უფრო დიდი) ფასდაკლება

# # დაბეჭდე შესაბამისი შეტყობინება, მაგალითად:
# # "გაქვს ფასდაკლება"
# # "გაქვს დამატებითი ფასდაკლება"
# # "ფასდაკლება არ გაქვს"
student = str(input("are you a student  yes/ no"))
member = str(input("are you a member  yes/no"))

if student == "yes" or member == "yes":
    print("gaqvs fasdakleba")
elif student == "yes" and member == "yes":
    print("gaqvs didi fasdakleba")
else:
    print('ar gaqvs fasdakelba')    


# # მომხმარებელს შემოატანინე username და შეამოწმე:

# # სიგრძე არის მინიმუმ 3 და მაქსიმუმ 20 სიმბოლო, შემოკლებით(and-ის გამოყენების გარეშე) შეგიძლიათ დაწეროთ num1 < x < num2
# # შეიცავს მხოლოდ ასოებს და ციფრებს (არანაირი space ან სიმბოლოები)

# # ამისთვის შეგიძლია გამოიყენო:

# # len() → ტექსტის სიგრძის გასაგებად
# # .isalnum() → ამოწმებს შეიცავს თუ არა მხოლოდ ასოებს და ციფრებს

# # მაგალითი:
# # len(username)
# # username.isalnum()


# # თუ ორივე პირობა დაკმაყოფილდა:
# # "username სწორია"

# # წინააღმდეგ შემთხვევაში:
# # "username არასწორია"    
name = str(input("Sheiyvane username>>> "))
sigrdze = len(name)
simbolo = name.isalnum()

if 3 <= sigrdze <=20 and simbolo == True:
    print(" Username Sworia")
else:
    print(" Username arasworia")    
    





