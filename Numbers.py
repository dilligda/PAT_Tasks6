#Givenlist
Numbers=[10,501,22,37,100,999,87,351]
#list to hold even and odd numbers
even_num=[]
odd_num=[]
#rule to detect the numbers
for num in Numbers:
    if num % 2 == 0:
        even_num.append(num)
    else:
        odd_num.append(num)
#print output
print("Even Numbers:", even_num)
print("Odd Numbers:", odd_num)
