# Create a list

sample_list = ["Ansible", "Terraform", "Jenkins", "Docker", "K8s"] # list()

# Indexing, slicing
sample_ele = sample_list[1]
print(sample_ele)

# sample_ele = sample_list[5]
# print(sample_ele)

"""
Traceback (most recent call last):
  File "/home/cloudshell-user/python-devops/04_list.py", line 9, in <module>
    sample_ele = sample_list[5]
IndexError: list index out of range
"""

sample_ele = sample_list[len(sample_list) - 1] # sample_list[-1]
print(sample_ele)

# Slicing
sliced_list = sample_list[1:3] # ("Terraform", "Jenkins")
print(sliced_list)

sliced_list_len = len(sliced_list)
print(sliced_list_len)

# List is a mutable data type
# Once defined, it can be altered
sample_list[1] = "Shell"
print(sample_list)

# Append element to the list
sample_list = ["Ansible", "Terraform", "Jenkins", "Docker", "K8s"]
sample_list.append("Shell") # inplace operation
print(sample_list)

# Append list to list
sample_list.append(sample_list)
print(len(sample_list))
print(sample_list[-1])