
# დავალება 1 — ლისტის ელემენტების ჯამი დაწერე პროგრამა, რომელიც: შექმნის რიცხვების ლისტს (მინიმუმ 5 ელემენტი) დაითვლის ყველა ელემენტის ჯამს ციკლის გამოყენებით დაბეჭდავს შედეგს 

ricxvebi_jami = []
jami = 0
for i in range(5):
    number = int(input(" შეიყვანე რიცხვი "))
    ricxvebi_jami.append(number)
    jami += number
     
print(jami)    
      

#    დავალება 2 — მაქსიმალური და მინიმალური მნიშვნელობა დაწერე პროგრამა, რომელიც: შექმნის რიცხვების ლისტს იპოვის ყველაზე დიდ და ყველაზე პატარა ელემენტს (max/min-ის გარეშე) დაბეჭდავს ორივეს დავალება 


ricxvebi_jami = []

for i in range(5):
    number = int(input(" შეიყვანე რიცხვი "))
    ricxvebi_jami.append(number)
    ricxvebi_jami.sort()
print(ricxvebi_jami)
print(ricxvebi_jami[-1])
print(ricxvebi_jami[0])      


#  ლუწი და კენტი რიცხვები დაწერე პროგრამა, რომელიც: შექმნის რიცხვების ლისტს გადაუვლის ლისტს ციკლით ცალკე ლისტებში შეინახავს: ლუწ რიცხვებს კენტ რიცხვებს დაბეჭდავს ორივე ახალ ლისტს დავალება 
ricxvebi_jami = [10,5,20,17,11,90,70,3,4,5,6,7,]
luwebi = []
kentebi = []

for i in ricxvebi_jami:
    if i % 2==0:
        luwebi.append(i)
    elif i % 2 == 1:
        kentebi.append(i)
print(luwebi)
print(kentebi)        

# luwebi = []
# kentebi = []

# raodenoba = int(input("რამდენი რიცხვის შეყვანა გსურთ? "))

# for i in range(raodenoba):
#     number = int(input(f"შეიყვანეთ მე-{i+1} რიცხვი: "))
    
#     # როგორც კი რიცხვს მივიღებთ, ეგრევე ვამოწმებთ და ვანაწილებთ
#     if number % 2 == 0:
#         luwebi.append(number)
#     else:
#         kentebi.append(number)

# print("\nშედეგები:")
# print("ლუწები:", luwebi)
# print("კენტები:", kentebi)

# ლისტი → ტაპლი დაწერე პროგრამა, რომელიც: შექმნის ლისტს გადააქცევს მას ტაპლად დაბეჭდავს ორივეს (ლისტსაც და ტაპლსაც) გამოიტენეთ tuple() ფუნქცია (Optional) 


list_list = []

for i in range(5):
    num = int(input(" ricxvi: "))
    list_list.append(i)

gadaqceva = tuple(list_list)

print(list_list)
print(gadaqceva)


# უნიკალური ელემენტები შექმენი ლისტი, სადაც ზოგი ელემენტი მეორდება შექმენი ახალი ლისტი, სადაც მხოლოდ უნიკალური ელემენტები იქნება


list_1 = [1,2,3,4,5,6,7,8,9,9,8,7,6,5,4]
list_2 = []
for i in list_1:
    if i not in list_2:
        list_2.append(i)
print(list_2)


