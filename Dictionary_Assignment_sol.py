#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Create a dictionary out of below inputs
# lst1 = ['emp1', 'emp2', 'emp3']
# emp_key = ['e_name', 'e_id', 'e_sal']
# emp1_val = ['John', 'SG101', '$10,000']
# emp2_val = ['Smith', 'SG102', '$9,000']
# emp3_val = ['Peter', 'SG103', '$9,500']

# Expected Output:- {'emp1':{'e_name':'John', 'e_id':'SG101', 'e_sal':$10,000}, 
#                    'emp2':{'e_name':'Smith', 'e_id':'SG102', 'e_sal':$9,000}, 
#                    'emp3':{'e_name':'Peter', 'e_id':'SG103', 'e_sal':$9,500}}

lst1 = ['emp1', 'emp2', 'emp3']
emp_key = ['e_name', 'e_id', 'e_sal']
emp1_val = ['John', 'SG101', '$10,000']
emp2_val = ['Smith', 'SG102', '$9,000']
emp3_val = ['Peter', 'SG103', '$9,500']
# new_dic  = dict(zip(emp_key, emp1_val)), dict(zip(emp_key, emp2_val)), dict(zip(emp_key, emp3_val))
# dict(zip(lst1, new_dic))

out_lst = []
for i in [emp1_val, emp2_val, emp3_val]:
  in_d = {}
  in_d[emp_key[0]] = i[0]
  in_d[emp_key[1]] = i[1]
  in_d[emp_key[2]] = i[2]
  out_lst.append(in_d)
out_d = {}
for i in range(len(out_lst)):
  out_d[lst1[i]] = out_lst[i]
out_d





# In[ ]:


# Acess the value of key 'history'

# sampleDict = { 
#    "class":{ 
#       "student":{ 
#          "name":"Mike",
#          "marks":{ 
#             "physics":70,
#             "history":80
#          }
#       }
#    }
# }




# In[ ]:


# Initialize dictionary with default values. Inputs are:-
# employees = ['Kelly', 'Emma', 'John']
# defaults = {"designation": 'Application Developer', "salary": 8000}

#Expected output:- {'Kelly': {'designation': 'Application Developer', 'salary': 8000}, 
#                   'Emma': {'designation': 'Application Developer', 'salary': 8000}, 
#                   'John': {'designation': 'Application Developer', 'salary': 8000}}


# In[ ]:


# Write a function reverseLookup(dictionary, value) that takes in a dictionary 
# and a value as arguments and returns a sorted list of all keys that contains the value. 
# The function will return an empty list if no match is found.

# In - reverseLookup({'a':1, 'b':2, 'c':2}, 1)
# Out - ['a']
# In - reverseLookup({'a':1, 'b':2, 'c':2}, 2)
# Out - ['b', 'c']
# In - reverseLookup({'a':1, 'b':2, 'c':2}, 3)
# Out - []

def reverseLookup(dictionary, value):
    key_lst = list(dictionary.keys())
    values_lst = list(dictionary.values())
    out_lst = []
    pos = -1
    for val in values_lst:
        try:
            pos = values_lst.index(value, pos+1)
        except ValueError:
            break
        out_lst.append(key_lst[pos])
    out_lst.sort()

    return out_lst
print(reverseLookup({'a':1, 'b':2, 'c':2}, 1))


# In[ ]:


# Write a function invertDictionary(d) that takes in a dictionary as argument and return a dictionary that inverts the keys and the values of the original dictionary.
# In - invertDictionary({'a':1, 'b':2, 'c':3, 'd':2})
# Out - {1: ['a'], 2: ['b', 'd'], 3: ['c']}
# In - invertDictionary({'a':3, 'b':3, 'c':3})
# Out - {3: ['a', 'c', 'b']}
# In - invertDictionary({'a':2, 'b':1, 'c':2, 'd':1})
# Out - {1: ['b', 'd'], 2: ['a', 'c']}


def invertDictionary(d):
    key_lst = list(d.keys())
    val_lst = list(d.values())
    out_dict = {}
    for i in val_lst:
        if i in out_dict:
            out_dict[i].append(key_lst[val_lst.index(i)])
            val_lst[val_lst.index(i)] = None
        elif i == None:
            continue
        else:
            out_dict[i] = [key_lst[val_lst.index(i)]]
            val_lst[val_lst.index(i)] = None
    return out_dict

invertDictionary({'a':2, 'b':1, 'c':2, 'd':1})


# In[ ]:


# Write a function that converts a sparse vector into a dictionary as described above.
# In - convertVector([1, 0, 0, 2, 0, 0, 0, 3, 0, 0, 0, 0, 4])
# Out - {0: 1, 3: 2, 7: 3, 12: 4}
# In - convertVector([1, 0, 1 , 0, 2, 0, 1, 0, 0, 1, 0])
# Out - {0: 1, 2: 1, 4: 2, 6: 1, 9: 1}
# In - convertVector([0, 0, 0, 0, 0])
# Out - {}

# def convertVector(numbers):
#     pos = -1
#     out_dict = {}
#     for num in numbers:
#         if num != 0:
#             try:
#                 pos = numbers.index(num, pos+1)
#             except:
#                 break
#             out_dict[pos] = num
#     return out_dict

# convertVector([1, 0, 0, 2, 0, 0, 0, 3, 0, 0, 0, 0, 4])

dict([i for i in enumerate([1, 0, 1 , 0, 2, 0, 1, 0, 0, 1, 0]) if i[-1] != 0])


# In[ ]:


# Write a function that converts a dictionary back to its sparse vector representation.
# In - convertDictionary({0: 1, 3: 2, 7: 3, 12: 4})
# Out - [1, 0, 0, 2, 0, 0, 0, 3, 0, 0, 0, 0, 4]
# In - convertDictionary({0: 1, 2: 1, 4: 2, 6: 1, 9: 1})
# Out - [1, 0, 1, 0, 2, 0, 1, 0, 0, 1]
# In - convertDictionary({})
# Out - []

def convertDictionary(dictionary): 
    key_lst = list(dictionary.keys())
    val_lst = list(dictionary.values())
    max_key = max(key_lst)
    out_lst = [0] * (max_key+1)
    pos = -1
    for ind in key_lst:
        try:
            pos = key_lst.index(ind, pos+1)
        except ValueError:
            break
        out_lst[ind] = val_lst[pos]
    return out_lst

convertDictionary({0: 1, 3: 2, 7: 3, 12: 4})


# In[ ]:





# In[ ]:


import math
fl = math.pi
# print(dir(f))
print(f'{fl:.2f}')
# help(f)

