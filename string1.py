str1 = input("Enter the sentence:")
print(str1)
str2 = input("Enter the word: ")
count = 0
for i in range(len(str1)): 
  if str1.startswith(str2, i):
    count=count+1
    print(f"The word '{str2}' present in '{str1}' as: {count} --> {i} ")
if count==0:
  print(f"The word '{str2}' is not present in '{str1}'")
