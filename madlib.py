# mad lib generator
# my family

q1=input("how many family member you have (in number not alphabet)? ")

q2=input("list down who is your family member: ")

q3=input("do you love your family (Yes/No)? ")
plural=""


if int(q1)>1:
    plural="s"
else:
    plural=""

if q3=="yes":
    q3="i love my family"
elif q3.lower()=="no":
    reason=input("why you don't love your family? ")
    q3=f" i don't love my family because {reason}"


print(f" i have {q1.lower()} family member{plural.lower()}, they are {q2.lower()}. {q3.lower()} ")

