limit=int(input("Limit: "))
i=1
my_sum  =0
sum_string = ""
while my_sum <= limit:
      sum_string += f"{i}"
      my_sum += i
      i +=1
if my_sum <= limit:
    sum_string +=" + "
print(f"The consecutive sum: {sum_string}= {my_sum}")
print ("Bye Bye consecutive sum")
print("adding this line to test new git version branch")