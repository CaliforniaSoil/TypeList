my_list =["magical unicorns",19,"hello",98.98,"world"]
sum = 0
if all(isinstance(i, int) for i in my_list) == True:
  print "The list you entered is of mixed type"
  for i in my_list:
    sum += i
  print "sum: {}".format(sum)

elif all(isinstance(i, str) for i in my_list) == True:
  "".join(my_list)
  print "The list you entered is of string type"
  print "String: " + " ".join(my_list)    


elif all(isinstance(i, int) for i in my_list) == False:
  print "The list you entered is of mixed type"
  newlist = []
  for x in my_list:
    if isinstance(x, str) == True:
      newlist.append(x)
  print "String: " + " ".join(newlist)

  for i in my_list:
    if isinstance(i, str) == True:
      my_list.remove(i)
  for k in my_list:
     sum += k
  print "sum: {}".format(sum)

