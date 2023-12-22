"""
For solving advent of code 2023 problem 8 part 1
"""

data_dict = {}

with open('data.txt', 'r', encoding='utf-8') as file:
    path = file.readline()
    blank = file.readline() # Dealing with line 2.
    for line in file:
        key, value = line.strip().split('=')
        key = key.strip()
        value = value.strip()
        value = value.replace(' ','')
        value = tuple(value[1:-1].split(','))
        data_dict[key] = value
path = path[:-1]


# In[6]:


COUNT = 0
NEW_KEY = 'AAA'
while NEW_KEY != 'ZZZ':
    NEW_KEY = data_dict[NEW_KEY][0] if path[COUNT % len(path)] == 'L' else data_dict[NEW_KEY][1]
    COUNT += 1
print(COUNT)
