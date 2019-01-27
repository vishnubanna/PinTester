raised = raw_input("numbers and a letter")
test = raised.split(',')
for i in range(0, len(test)):
  try:
    test[i] = int(test[i])
  except:
    test[i] = test[i]


print(test)

for i in range(0, len(test)):
  if type(test[i]) == int:
    print (test[i])
