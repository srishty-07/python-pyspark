#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=10
print(type(a))


# In[2]:


b="Srishty"


# In[9]:


c='srishty'
d="'srishty'"
#for multiline - triple quotes
print(type(b))
print(type(c))
print(type(d))
print(b+' '+c+' '+d)


# In[11]:


a = True
b = False
print(type(a))


# In[12]:


print(type(b))


# In[13]:


print(True+True)


# In[14]:


print(True-False)


# In[15]:


c=10+20j


# In[16]:


print(c)


# In[17]:


print(type(c))


# In[19]:


a=10
# it will show location id where the value 10 will be stored
#we have a single object having value 10 and any other variable that has value 10 then it will point automatically to that object
b=10
print(id(a))
print(id(b))


# In[21]:


s=7
print(s)
print(id(s))
#after that a new object will be created and the old one can not be retrieved so for new s a new object will be created therefore we can see difft id's for both s
s=13
print(s)
print(id(s))


# In[22]:


# s{start:end-1:skip}
s="abcdefghijklmnopqrstuvwxyz"


# In[24]:


s[12:-11]


# In[26]:


s[-3:]


# In[27]:


s[:-12]


# In[28]:


#operators
#depending upon the variable the output for floordivision will change (//)
a=2
b=4
c=6.0
print(a/b)
print(a//b)
print(a//c)


# In[29]:


a=True
b=False
print(a or a)
print(a and a)
print(a or b)
print(b or b)
print(a and b)


# In[30]:


is_geological_survey_complete = True
is_environmental_clearance_received = True
is_market_demand_high = False
should_start_drilling = is_geological_survey_complete and is_environmental_clearance_received and is_market_demand_high


# In[31]:


print(should_start_drilling)


# In[32]:


# Boolean Variables
HasExplorationPermit = True
HasDrillingRights = True
HasEnvironmentalApproval = False
HasOilDiscovery = True

# Logical Operations
IsExplorationAllowed = HasExplorationPermit and HasDrillingRights and not HasEnvironmentalApproval
IsDiscoveryProfitable = HasOilDiscovery and (HasExplorationPermit or HasDrillingRights)


# In[33]:


print(IsExplorationAllowed)


# In[34]:


print(IsDiscoveryProfitable)


# In[35]:


"seven"*7


# In[37]:


#LIST
# slicing and indexing can be performed
# order is maintained
# Duplictaes are allowed
# list is mutable(we can edit something inside that object)- same object is created and that weill only be edited
a=[10,"srishty",7,9.8,True]
print(a)
print(type(a))


# In[38]:


print(id(a))
a.append(26)
print(id(a))


# In[40]:


#tuple
#same as list but it is immutable
#syntax: in paranthesis : ()
a=("srishty",True,"2002-02-07",67,8)
# a.append(1) #we cannnot edit list


# In[41]:


#tuple is faster bcoz it is immutable


# In[43]:


#formatted string
name = "srishty"
dept = "IDA"
print("I am {} working as {}".format(name,dept))
print("I am %s working as %s" %(name,dept))


# In[44]:


#latest way of formatted string 
print(f"I am {name} working as {dept}")


# In[46]:


# Employee Information:
name = "John Doe"
job_title = "Senior Geologist"
department = "Geology"
email = "johndoe@email.com"
phone = "123-456-7890"


# In[53]:


print(f" name : {name} \n job_title : {job_title} \n department : {department} \n email : {email} \n phone : {phone} ")


# In[54]:


#set
#heterogenous object
#duplivctaes are not allowed
#order is not preserved
#slicinh and indexing are not possible


# In[55]:


c={10,10.5,"shelll",True,True,10,10,10,"Python"}


# In[56]:


print(c)


# In[57]:


c.add(55)


# In[59]:


#dictionary
# {}
# key value piar
#allows heterogenous object
#order is maintinaed
#no duplicates(no duplicate key but value can be duplivcate)
d={"location":"delhi","name":"srishty","age":21}
print(d)


# In[60]:


d['location']="bangalore"


# In[61]:


print(d)


# In[62]:


#membership operator : (in) and (not in)


# In[63]:


#to chcek whether a value is present in list/string etc
# List of Equipment
refineryEquipment = ["Crude Distillation Unit", "Catalytic Cracking Unit", "Hydrotreating Unit", "FCC Unit"]

 

# Membership Operator
IsUnitInstalled = "Hydrotreating Unit" in refineryEquipment
IsUnitObsolete = "Thermal Cracking Unit" not in refineryEquipment

 

print("Is Hydrotreating Unit installed?", IsUnitInstalled)
print("Is Thermal Cracking Unit obsolete?", IsUnitObsolete)


# In[64]:


employees = [
    "John Doe, Senior Geologist, Geology, johndoe@email.com, 123-456-7890",
    "Jane Smith, Drilling Engineer, Drilling, janesmith@email.com, 987-654-3210",
    "Bob Johnson, Reservoir Engineer, Reservoir Engineering, bobjohnson@email.com, 456-789-0123",
    "Alice Brown, Petrophysicist, Petrophysics, alicebrown@email.com, 789-012-3456"
]
employees[0]


# In[65]:


new_employee = "Eva Green, Drilling Technician, Drilling, evagreen@email.com, 111-222-3333"
employees.append(new_employee)


# In[66]:


print(employees)


# In[68]:


age=20
if(age>18):
    print("can vote")
else:
    print("can't soorrryy")


# In[72]:


low_fuel_threshold = 1000
crtical_fuel_threshold = 500
current_fuel_level = int(input("enter current_fuel_level"))


# In[73]:


type(current_fuel_level)


# In[74]:


if(current_fuel_level < crtical_fuel_threshold):
    print("Critical fuel level reached. Take immediate action")
    more_fuel = int(input("Add fuel"))
    current_fuel_level = more_fuel+current_fuel_level
elif(current_fuel_level<low_fuel_threshold):
    print("Low Fuel alert!!!")
else: 
    print("continue fueling")


# In[75]:


range(9)


# In[76]:


for i in range(0,10):
    print(i)


# In[77]:


range(10)
range(5,10)
range(2,22,2)


# In[78]:


#table of 2
for i in range(2,21,2):
    print(i)


# In[79]:


l1=['a','b','c']
l2=['sales','it','finance']
l=zip(l1,l2)
print(l)


# In[80]:


l=list(zip(l1,l2))
print(l)


# In[83]:


oil_gas_data = [
    ("Field A", "Texas", 500000),
    ("Field B", "Alaska", 800000),
    ("Field C", "North Sea", 300000),
    ("Field D", "Gulf of Mexico", 600000),
]
# use zip() to group the information of each oil and gas field together:
field_name,location,reserves = zip(*oil_gas_data)


# In[85]:


print(field_name)
print(location)
print(reserves)


# In[87]:


#to add index in field suppose we will use an enumerate function
e = list(enumerate(location))
f = list(enumerate(field_name))
print(e)
print(f)


# In[88]:


for index, field_data in enumerate(oil_gas_data):
    field_name, location, reserve = field_data
    print(f"Field {index+1}: {field_name} is located in {location} with reserves of {reserve} barrels.")


# In[ ]:




