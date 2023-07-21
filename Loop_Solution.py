#!/usr/bin/env python
# coding: utf-8

# # If - elif - else statement

# In[ ]:


#W. A P. which takes one number from 0 to 9 from the user and prints it in the word. And if the word is not from 0 to 9 then
#it should print that number is outside of the range and program should exit.
# For exapmple:- 
# input = 1
# output = one

num = int(input('Enter a number: '))
if num == 0:
  print('Zero')
elif num ==1:
  print('One')
elif num ==2:
  print('Two')
elif num ==4:
  print('Four')
elif num ==5:
  print('Five')
elif num ==6:
  print('Six')
elif num ==7:
  print('Seven')
elif num ==8:
  print('Eight')
elif num ==9:
  print('Nine')
else:
  print('Number is outside the range!!!')


# In[ ]:


#W. A P. to implement calculator but the operation to be done and two numbers will be taken as input from user:-
#Operation console should show below:-
#     Please select any one operation from below:-
#         * To add enter 1
#         * to subtract enter 2
#         * To multiply enter 3
#         * To divide enter 4
#         * To divide and find quotient enter 5
#         * To divide and find remainder enter 6
#         * To divide and find num1 to the power of num2 enter 7
#         * To Come out of the program enter 8
import sys
num1 = int(input('Enter 1st number: '))
num2 = int(input('Enter 2nd number: '))
while True:
  op = int(input('''Please select any one operation from below:-\n
  \tTo add enter 1\n
  \tTo subtract enter 2\n
  \tTo multiply enter 3\n
  \tTo divide enter 4\n
  \tTo divide and find quotient enter 5\n
  \tTo divide and find remainder enter 6\n
  \tTo divide and find num1 to the power of num2 enter 7\n
  \tTo exit Enter 8\n
  '''))
  if op == 1:
    print(num1+num2)
  elif op == 3:
    if num1>num2:
      print(num1-num2)
    else:
      print(num2-num1)
  elif op == 4:
    print(num1*num2)
  elif op == 5:
    print(num1/num2)
  elif op == 6:
    print(num1//num2)
  elif op == 7:
    print(num1**num2)
  elif op == 8:
    sys.exit(0)
  else:
    print('wrong input\nTry Again\n\n')


# In[ ]:


#W A P to check whether a year entered by user is an leap year or not?
#Check with below input:-
    #leap year:- 2012, 1968, 2004, 1200, 1600,2400
    #Non-lear year:- 1971, 2006, 1700,1800,1900
    


# In[ ]:


#W A P which takes one number from the user and checks whether it is an even or odd number?, If it even then prints number is 
#even number else prints that number is odd number.



# In[ ]:


#W A P which takes two numbers from the user and prints below output:-
#     1. num1 is greater than num2 if num1 is greater than num2
#     2. num1 is smaller than num2 if num1 is smaller than num2
#     3. num1 is equal to num2 if num1 and num2 are equal

#Note:- 1. Do this problem using if - else 
#       2. Do this using ternary operator



# In[ ]:


#W A P which takes three numbers from the user and prints below output:-
#     1. num1 is greater than num2 and num3 if num1 is greater than num2 and num3
#     2. num2 is greater than num1 and num3 if num2 is greater than num1 and num3
#     3. num3 is greater than num1 and num2 if num3 is greater than num1 and num2

#Note:- 1. Do this problem using if - elif - else 
#       2. Do this using ternary operator

# a = a if a>b else b
expr if cond1 else expr2 if cond2 else expr3


# # Loops - for loop, while loop

# In[ ]:


#Write a Python program to find the length of the my_str using loop:-

#Input:- 'Write a Python program to find the length of the my_str'
#Output:- 55


# In[9]:


#Write a Python program to find the total number of times letter 'p' is appeared in the below string using loop:-
    
#Input:- 'peter piper picked a peck of pickled peppers.\n'
#Output:- 9

jack='peter piper picked a peck of pickled peppers.\n'
jack.count("p")


# In[19]:


#Write a Python Program, to print all the indexes of all occurences of letter 'p' appeared in the string using loop:-
    
#Input:- 'peter piper picked a peck of pickled peppers.'
y='peter piper picked a peck of pickled peppers.'
for i in range(y.index("p")):
    print(y)
y

#Output:- 
# 0
# 6
# 8
# 12
# 21
# 29
# 37
# 39
# 40


# In[1]:


#Write a python program to find below output using loop:-

#Input:- 'peter piper picked a peck of pickled peppers.'
#Output:- ['peter', 'piper', 'picked', 'a', 'peck', 'of', 'pickled', 'peppers']

dimah='peter piper picked a peck of pickled peppers.'
dimah.split()


# In[7]:


#Write a python program to find below output using loop:-

#Input:- 'peter piper picked a peck of pickled peppers.'
#Output:- 'peppers pickled of peck a picked piper peter'

aram='peter piper picked a peck of pickled peppers.'
aram[::]


# In[ ]:


#Write a python program to find below output using loop:-

#Input:- 'peter piper picked a peck of pickled peppers.'
#Output:- '.sreppep delkcip fo kcep a dekcip repip retep'



# In[ ]:


#Write a python program to find below output using loop:-

#Input:- 'peter piper picked a peck of pickled peppers.'
#Output:- 'retep repip dekcip a kcep fo delkcip sreppep'


# In[ ]:


#Write a python program to find below output using loop:-

#Input:- 'peter piper picked a peck of pickled peppers.'
#Output:- 'Peter Piper Picked A Peck Of Pickled Peppers'


# In[ ]:


#Write a python program to find below output using loop:-

#Input:- 'Peter Piper Picked A Peck Of Pickled Peppers.'
#Output:- 'Peter piper picked a peck of pickled peppers'


# In[ ]:


#Write a python program to implement index method using loop. If sub_str is found in my_str then it will print the index
# of first occurrence of first character of matching string in my_str:-

#Input:- my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.', sub_str = 'Pickl'
#Output:- 29



# In[ ]:


#Write a python program to implement replace method using loop. If sub_str is found in my_str then it will replace the first 
#occurrence of sub_str with new_str else it will will print sub_str not found:-

#Input:- my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.', sub_str = 'Peck', new_str = 'Pack'
#Output:- 'Peter Piper Picked A Pack Of Pickled Peppers.'

my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.'
sub_str = 'Peck'
new_str1 = 'Pack'
out_str = ''
j = 0
new_str = ''
for i in range(len(my_str)):
    if my_str[i] == sub_str[j]:
        new_str += my_str[i]
        j += 1
        if len(new_str) == len(sub_str) and new_str == sub_str:
            ind = i-(len(sub_str)-1)
            print(ind)
            out_str = my_str[:ind] + new_str1 + my_str[ind+(len(sub_str)):]
            print(out_str)
            break
        elif len(new_str) == len(sub_str) and new_str != sub_str:
            new_str = ''
    elif i == (len(my_str)-1):
        print('string not found!')
    else:
        new_str = ''
        j = 0


# In[ ]:


#Write a python program to find below output (implements rjust and ljust) using loop:-

#Input:- 'Peter Piper Picked A Peck Of Pickled Peppers.', sub_str = 'Peck', 
#Output:- '*********************Peck********************'

# my_str='Peter Piper Picked A Peck Of Pickled Peppers.'
# sub_str='Peck'
# out_str=''
# i=0
# while i in range(0,len(my_str),1):
#     if my_str[i:(i+len(sub_str)):1]==sub_str:
#         out_str=out_str+sub_str
#         i = i+(len(sub_str)-1)
#     else:
#         out_str=out_str+'*'
#     i=i+1
# print(out_str)



# In[ ]:


#Write a python program to find below output using loop:-

#Input:- 'This is Python class', sep = 'is', 
#Output:- ['This', 'is', 'Python class']


inp_str='This is Python class'
sep='is'
out_str=''
l_str=''
r_str=''
length=0
out_lst=[]
for letter in inp_str:
    length+=1
    out_str += letter
    if sep in out_str:
        l_str=inp_str[:length-len(sep):]
        r_str=inp_str[length::]
        out_str=''
out_lst.append(l_str)
out_lst.append(sep)
out_lst.append(r_str)
print(out_lst) 

# my_str='This is Python Class '
# my_str1 =''
# my_str2 =''
# my_lst =[]
# sep = 'is'
# x=0
# for i in my_str:
    
#     if i !=' ':
#         my_str1 += i    
#     else:
#         if sep not in my_lst:
#             my_lst += [my_str1]
#             my_str1 = ''
#         else:
#             my_str1=my_str1 + ' '
# my_lst += [my_str1.strip()]
# print(my_lst)




# my_str='This is Python class'
# sep_str=' is'
# out_str=''
# out_lst=[]
# i=0
# x=True
# # print(my_str.partition(' is '))
# while i in range(0,(len(my_str)),1):
#     if my_str[i]==' ' and x==True and i<=(len(my_str)):
#         out_lst.append(out_str)
#         out_str=''
#     if my_str[i:(i+len(sep_str)):1]==sep_str:  
#             out_lst.append(sep_str)
#             out_str=''  
#             i = i+(len(sep_str))
#             x=False
#     if i ==(len(my_str)):
#         out_lst.append(out_str)
#     else: 
#         out_str=out_str+my_str[i]    
#     i=i+1
# out_lst.append(out_str)
# print(out_lst) 


# In[ ]:


#Write a python program which takes one input string from user and encode it in below format:-
#     1. #Input:- 'Python'
       #Output:- 'R{vjqp'

#Using loop
# inp_str = 'Python'
# out_str = ''
# for i in inp_str:
#   out_str = out_str + chr(ord(i)+2)
# print(out_str)
        
# Using built-in function and list comprehension
# ''.join([chr(ord(ele)+2) for ele in list('Python')])

    # 2. #Input:- 'Python'
    #    #Output:- 'Rwvfql'
        
# inp_str = 'Python'
# out_str = ''
# for ele in range(len(inp_str)):
#   if ele%2 == 0:
#     out_str += chr(ord(inp_str[ele])+2)
#   else:
#     out_str += chr(ord(inp_str[ele])-2)
# print(out_str)
        
        
        
    # 3. #Input:- 'Python'
    #    #Output:- 'R{vkfml'

# inp = input("Enter a string")
# out = ''
# for i in range(0, len(inp)):
#   if i < len(inp)/2:
#     out += chr(ord(inp[i]) + 2)
#   else:
#     out += chr(ord(inp[i]) - 2)
# print(out)       
        
        
        

