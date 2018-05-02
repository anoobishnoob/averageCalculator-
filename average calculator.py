total = 0
newTotal = "you do not have any values " # this is still bugged 0/0 error
b = 0
i = 0
while b != -1:
  #print("Please type a non-negative int")
  num = int(input())
  total = num + total
  #print ("current datum is = to", num, "current total is = to ", total)
  if num == -1:
    b = -1
  i +=1 
  #print("counter is ", i )
total +=1 # -1 is counted so this is just to counteract that fact
i -= 1 # -1 is counted in my model here, so this just gets rid of an extra count
if not(i == 1 and num == -1):
# if i != 1 or num != -1:
  newTotal = total/i
  print ('n=', total,"counter =", i )
  print ("average =", newTotal)
print("end")

