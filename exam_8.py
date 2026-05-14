

# .დაწერე ფუნქცია find_min_max, რომელიც მიიღებს ნებისმიერი რაოდენობის რიცხვებს (*args) და დააბრუნებს:

# ყველაზე პატარა რიცხვს
# ყველაზე დიდ რიცხვს

def find_max_min(*args):
    min_1 = min(args)
    max_1 = max(args)
    return min_1 , max_1
print(find_max_min(1,2,3,4,5)) 

# 2.დაწერე ფუნქცია calculate, რომელიც:

# იღებს *args
# იღებს keyword არგუმენტს operation

# operation შეიძლება იყოს:

# "sum"  → ჯამი
# "max"  → მაქსიმუმი
# "min"  → მინიმუმი
# "mult" → ნამრავლი

def calculate (*args ,operation):
    if operation == "sum":
        return sum(args)
    elif operation == "max":
        return max(args)
    elif operation == "min":
        return min(args)
    elif operation == "mult":
        result = 1
        for i in args:
            result=result*i
        return result    
print(calculate(1,2,3,4 ,operation="sum"))
print(calculate(1,2,3,4 ,operation="max"))
print(calculate(1,2,3,4 ,operation="min"))
print(calculate(1,2,3,4 ,operation="mult"))

# mult = [1,2,3,4,5,6,7,8,9]
# result = 1
# for i in mult:
#     result=result*i
#     print(i)
# print(result)    

# დაწერე ფუნქცია format_user, რომელიც იღებს:

# first_name
# last_name
# **kwargs

# და აბრუნებს სტრინგს ამ ფორმატში:

# format_user("John", "Doe", age=25, job="Developer")
# John Doe | age: 25, job: Developer
def format_user(first_name, last_name, **kwargs):

    list_1 = []
    
    
    for key, value in kwargs.items():
        list_1.append(f"{key}: {value}")
        
    
    details_string = ", ".join(list_1)
    
    
    return f"{first_name} {last_name} | {details_string}"


print(format_user("John", "Doe", age=25, job="Developer"))

#  დაწერე ფუნქცია safe_divide(a, b), რომელიც:

# თუ b == 0 → აბრუნებს "Cannot divide by zero"
# სხვა შემთხვევაში აბრუნებს:
# მთელ ნაწილს და ნაშთს, ორივეს ერთად

# safe_divide(10, 2)  # (5, 0)
# safe_divide(10, 0)  # Cannot divide by zero


def safe_device(a,b):
    
    if b == 0:
        return ("annot divide by zero")
    
    num = a // b
    num_2 = a % b
    
    
    return num , num_2
print(safe_device(10,0))



