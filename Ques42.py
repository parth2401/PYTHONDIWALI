test_str = "ParthVyas"
  
# printing original string 
print("The original string is : " + str(test_str))
  
# Using lower() + string slicing
# Lowercase first character of String
res = test_str[0].lower() + test_str[1:]
  
# printing result 
print("The string after lowercasing initial character : " + str(res))
