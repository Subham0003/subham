#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Write a Python program to find the multiplication of all elements in a list using loop.
#Input:- [10,20,30,40]
#Output:- 240000

list=[10,20,30,40]
result=1
for i in range(len(list)):
    result*=list[i]
    
print("Multiplication of all number :-", result)


# In[6]:


#Write a Python program to find the largest number from a list using loop.
#Input:- [10,100,2321, 1,200,2]
#Output:- 2321

new=[10,100,2321, 1,200,2]
for i in range(len(new)):
    result=max(new)
    
print("largest no of new:-",result)


# In[9]:


print("argest no ",max(new))


# In[8]:


#Write a Python program to find the smallest number from a list using loop.
#Input:- [10,100,2321, 1,200,2]
#Output:- 1
new=[10,100,2321, 1,200,2]
for i in range(len(new)):
    result=min(new)
print("smallest no is :-",result)


# In[19]:


#Write a Python program to count the number of strings having length more than 2 and are palindrome in a list using loop.
#Input:- ['ab', 'abc', 'aba', 'xyz', '1991']
#Output:- 2

list=['ab', 'abc', 'aba', 'xyz', '1991']
def subham(x):
    count=0
    for x in x :
        if len(x) <1 and x[0:]==x[-1:]:
            count+=1
    return count
            
print(subham(['ab', 'abc', 'aba', 'xyz', '1991']))


# In[26]:


list=['ab', 'abc', 'aba', 'xyz', '1991']
len([x for x in list if (len(x)>=2 and x[-1]==x[0])])


# In[31]:


#Write a Python program to sort a list in ascending order using loop.
#Input:- [100,10,1,298,65,483,49876,2,80,9,9213]
#Output:- [1,2,9,10,65,80,100,298,483,9213,49876]

Input= [100,10,1,298,65,483,49876,2,80,9,9213]
Input.sort()
print(Input)


# In[33]:


#Write a Python program to get a sorted list in increasing order of last element in each tuple in a given list using loop.
#Input:- [(5,4),(9,1),(2,3),(5,9),(7,6),(5,5)]
#output:- [(9,1),(2,3),(5,4),(5,5),(7,6),(5,9)]

Input= [(5,4),(9,1),(2,3),(5,9),(7,6),(5,5)]
Input.sort()
print(Input)


# In[46]:


#Write a Python program to remove fuplicate element from a list using loop.
#Input:- [10,1,11,1,29,876,768,10,11,1,92,29,876]
#Output:- [10,1,11,29,876,768,92]

ass=[10,1,11,1,29,876,768,10,11,1,92,29,876]
new=set(ass)
new
print(new)


# In[49]:


xy=[ass in ass for range(len(ass) if ass.index(ass[i]==i))]


# In[61]:


#Write a Python program which takes a list from the user and prints it after reshuffling the elements of the list.
#Input:- [10,21,22,98,87,45,33,1,2,100]
#Output:- [1,87,21,10,33,2,100,45,98,22] (It may be any randon list but with same elements)

sd=[10,21,22,98,87,45,33,1,2,100]
random.shuffle(sd)
print(sd)


# In[65]:


sd.reverse()
print(sd)


# In[66]:


sd.append(20)


# In[67]:


sd


# In[72]:


sd.pop()


# In[73]:


sd


# In[132]:


#Write a Python program which takes a list of numbers as input and prints a new list after removing even numbers from it.
#Input:- [10,21,22,98,87,45,33,1,2,100]
#Output:- [21,87,45,33,1]

mau=[10,21,22,98,87,45,33,1,2,100]
for i in mau:
    if i%2!=0:
        print(i,end="[] ")


# In[ ]:


#Write a Python program to create a 3X4X6 3D matrix wiith below elements using loop
#Output:- 
# [
#     [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]],
#     [[0,0,0,0,0,0],[1,1,1,1,1,1],[2,2,2,2,2,2],[3,3,3,3,3,3]],
#     [[0,0,0,0,0,0],[2,2,2,2,2,2],[4,4,4,4,4,4],[6,6,6,6,6,6]]
# ]



# In[90]:


mau=[10,21,22,98,87,45,33,1,2,100]
subham=mau.copy()


# In[91]:


subham


# In[92]:


#Write a Python program to copy a list using loop.
#inp_lst = [10,10.20,10+20j, 'Python', [10,20], (10,20)]
#out_lst = [10,10.20,10+20j, 'Python', [10,20], (10,20)]


vd=[10,10.20,10+20j, 'Python', [10,20], (10,20)]
print(vd.copy())


# In[94]:


vd[::-1]


# In[113]:


mau[::-4]


# In[110]:


if mau[:-1]==mau[0:]:
    print("jay shree ram")
else:
    print("jay jay shree ram")


# In[111]:


mau[:-1]


# In[112]:


mau[0:]


# In[114]:


#Input:- 'How much wood would a woodchuck chuck if a woodchuck could chuck wood'
#Write a Python program to find the list of words that are longer than or equal to 4 from a given string.
ram='How much wood would a woodchuck chuck if a woodchuck could chuck wood'
print(ram.split())


# In[123]:


ram='How much wood would a woodchuck chuck if a woodchuck could chuck wood'


# In[130]:


print([ele for ele in set(ram.split())if (ele) >=4])


# In[ ]:





# In[ ]:




