


# # . Countdown
# # დაწერე პროგრამა, რომელიც:
# # მომხმარებლისგან ითხოვს დადებით მთელ რიცხვს n.
# # while ციკლის გამოყენებით ბეჭდავს რიცხვებს n-დან 1-მდე (უკუღმა).
# # ციკლის დასრულების შემდეგ ბეჭდავს ტექსტს:

number  = int(input("Sheiyvane ricxvi "))

while number >= 1:

    print(number)

    number = number -1
    
print("good")

# # ჯამის გამოთვლა
# # დაწერე პროგრამა, რომელიც:
# # უსასრულო ციკლში სთხოვს მომხმარებელს მთელ რიცხვებს.
# # თუ მომხმარებელი შეიყვანს 0-ს, პროგრამა უნდა შეჩერდეს.
# # საბოლოოდ დაბეჭდოს ყველა შეყვანილი (არანულოვანი) რიცხვის ჯამი.

total = 0
while True:
    number  = int(input("Sheiyvane ricxvi "))
    if number == 0:
        break
    else:
        total = number + total
print( total)        



# # . გამოცნობის თამაში
# # დაწერე პროგრამა:
# # კოდში განსაზღვრე საიდუმლო რიცხვი (მაგ. 7).
# # მომხმარებელი ციკლში ცდილობს მის გამოცნობას.
# # ყოველი არასწორი მცდელობისას:
# # თუ რიცხვი მეტია → "Too high"
# # თუ რიცხვი ნაკლებია → "Too low"
# # სწორ გამოცნობაზე:
# # დაბეჭდე "Correct!"
# # გამოიყენე break ციკლის შესაჩერებლად.

number = 10
while True:

    num = int(input("sheiyvane ricxvi: "))
    if num == number:
        print("ricxia: ", number)
        break
    elif num >= number:
        print("Too high")
    elif num <= number:
        print("Correct!")    
    
# სტრიქონის ფილტრაცია (continue)
# დაწერე პროგრამა, რომელიც:
# მომხმარებლისგან იღებს ტექსტს.
# continue-ის გამოყენებით გამოტოვებს ხმოვნებს (a, e, i, o, u).
# ბეჭდავს მხოლოდ თანხმოვნებს.


# text_1 = input("sheiyvane sityva: " )

for i in text_1:
    if i in ['a','e','i','o','u']:
        continue
    print(i)

# range() პრაქტიკა
# დაწერე პროგრამა, რომელიც for ციკლისა და range() ფუნქციის გამოყენებით ბეჭდავს:
# 0-დან 9-მდე
# 5-დან 15-მდე
# 0-დან 20-მდე მხოლოდ ლუწ რიცხვებს
# 10-დან 1-მდე (უკუღმა)

for i in range(0,9):
    if i % 2 == 0:
        print("luwia" ,i)

for i in range(5,15):
    if i % 2 == 0:
        print("luwia" ,i)

for i in range(10,1, -1):
    if i % 2 == 0:
        print("luwia" ,i)