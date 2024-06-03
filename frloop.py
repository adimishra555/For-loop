''' s='fifhteen augest is very import day for india bcs that day is fully independent and aajadi '
for i in s:
    print(i,end=' ')
print() '''


''' b=[1,2,3,4,5]
for i in b:
    print(i,end=' ') '''


# for i in range(0,11,1):
    # print(i,end=' ')
    
   
# s='javatpoint is best website to learn coding'
# x=s.split()
# for i in range(0,len(x),1):
#     print(i,x[i], end='  ')
# print()
    
    
# d={"a":51,"n":89,"r":78}
# for i in d:
#     # print(d[i],end='')
#     # print(i,end=' ')
#     print({i:d[i]}, end=' ')
# # print()
# # print()
# print()


''' d={"a":"apple","b":24,"c":6+2j,"d":True}
dict={}
for i in d:
    if isinstance(d[i],(int,float,bool,complex)):
        dict[d[i]]=i
    
print(dict) '''

''' 
l=["hello",1,23.4,"guys",[2,3,4],True,78+4j,{8,9},(89,66),{"hi":"hello"}]
indi_dtype=[]
for i in l:
    if isinstance(i,(int,float,complex,bool)):
        indi_dtype.append(i)
    
print(indi_dtype) '''



''' l=["hello",1,23.4,"guys",[2,3,4],True,78+4j,{8,9},(89,66),{"hi":"hello"}]
sum=0
for i in l:
    if isinstance(i,(int,bool,complex,float)):
        sum=sum+i
print(sum) '''


''' a="in a day we have 24 hours"
calpha=0
cnum=0
cspace=0
for i in a:
    if i.isalpha():
        calpha+=1
    elif i.isdigit():
        cnum+=1
    else:
        cspace+=1
    
print(f'Number of alphabat: {calpha}')
print(f'Number of digit: {cnum}')
print(f'Number of space: {cspace}') '''


# l=["apple","google","yahoo","microsoft","gmail","walmart"]
# d={}
# for i in l:
#     d[l.index(i)]=i
    
# print(d)

# for i in range(len(l)):
#     d[i]=l[i]
# print(d)




''' dic=["apple","google","yahoo","samsung","oracle","flipcart"]
d={}
for i in dic:
    if len(i)%2==0:
        d[i]=i
    else:
        d[i]=i[::-1]
print(d) '''



''' l=["red","blue","violet","pink","orange","black","red","orange","pink"]
d={}
for i in l:
    d[i]=l.count(i)
print(d) '''


''' l='aajrajakabajabaje'
d={}
for i in l:
    d[i]=l.count(i)
    
print(d) '''

# l=["red","blue","violet","pink","orange","black","red","orange","pink"]
# l='aajrajakabajabaje'
# d={}
# for i in l:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# print(' '+str(d))

''' from collections import Counter
l='aajrajakabajabaje'
x=Counter(l)
print(' '+str(x)) '''


''' def find_pairs_with_sum(arr, target):
    num_dict = {}  # Dictionary to store numbers and their indices

    for num in arr:
        complement = target - num
        if complement in num_dict:
            print(f"({num},{complement})")
        num_dict[num] = True

# Given array and target value
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_sum = 10 '''

''' a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
d={}
sum=10
for i in a:
    com=sum-i
    if com in d:
        print(f"{i},{com}")
    d[i]=i '''





''' s="hello world hello python and python program"
x=s.split()
count=0
# print(len(x))
for i in x:
    count+=1
print(count) '''


''' s="Today is friday and attending python session"
x=s.split()
i=0
for i in range(len(x)):
    if x[i][0] in 'aeiouAEIOU':
        print(f'{x[i]} is start with vowel') '''
    


    
''' s="Today is friday and attending python sesion"
x=s.split()
i=0
for i in range(len(x)):
    if len(x[i])%2==0:
        print(f"{str(x[i])} is even length str")
    i+=1 '''
    
    
''' s="Today is friday and attending python sesion"
x=s.split()
d={}
# for i in x:
for i in range(len(x)):
    d[i]=x[i]
    # d[x.index(i)]=i
print(d) '''
    
    

''' s="Today is frida and attending pytho sesion"
x=s.split()
# d={}
for i in range(len(x)-1):
    if x[i][-1] in 'aeiouAEIOU':
        print(f'{x[i]} end with vowel')
        print()
    i+=1
    # d[i]=x[i]
# print(d) '''

#wap to create a dictionary with words and its pair length pair and ends
#with vowel
# s="Today is friday and attending python sesion"
# x=s.split()
# var={i:{i,len(i)} for i in range(len(x)) if i[-1] in 'aeiouAEIOU'}
# print(var)





# s="hii hello good morning welcome to python session"
# x=s.split()
# d={}
# for i in x:
#     if i[0] in d:
#         d[i[0]].append(i)
#     else:
#         d[i[0]]=[i]
# print(d)

# var={i[0]:[] for i in x}
# for i in x:
#     var[i[0]].append(i)
# print(var)


''' 
from collections import OrderedDict
d=OrderedDict()
d={'a':1,'b':2,'c':3,'d':4}
for i,j in d.items():
    print(i,j) '''



''' from collections import ChainMap
d1={'a':1,'b':2}
d2={'c':3,'d':4}
c=ChainMap(d1,d2)
print(c.keys())
print(c.values())

print(type(c)) '''

''' 
def WrapperExample(A): 
      
    class Wrapper: 
          
        def __init__(self, y): 
              
            self.wrap = A(y) 
              
        def get_number(self): 
              
 
            return self.wrap.name 
          
    return Wrapper 
  
@WrapperExample
class code: 
    def __init__(self, z): 
        self.name = z 
 
y = code("Wrapper class") 
print(y.get_name()) 
'''


# s='101010'
# str=''
# for i in s:
#     if i in str=='1':
#         str+=1
#     else:
#         if i in  str=='0':
#             str+=1
# print(str)
        
        
        
# s='101010'
# str=list(s)
# for i in range(len(str)-1):
#     for j in range(i+1,len(str)):
#         if str[i]>str[j]:
#             str[i],str[j]=str[j],str[i]
# print(''.join(str))



        
        
# n=int(input("Enter the number:"))
# for i in range(n+1):
#     print("*    *")
#     print("*    *")

#     if (i<n):
#         print("******")




''' 
def search(arr,target):
    left,right=0,len(arr)-1

    while left<=right:
        mid=left+right//2

        if arr[mid]==target:
            return mid
        
        if arr[left]<=arr[mid]:
            if arr[left]<=target<=arr[mid]:
                right=mid-1
            else:
                left=mid+1
        else:
            if arr[mid]<=target<=arr[right]:

                left=mid+1
            else:
                right=mid-1
    return -1
arr=[10,20,30,50,49,60,70,80]
target=50
result=search(arr,target)


if result !=-1:
    print(f"element {target} is found the index {result}")
else:
    print(f"element {target} is not found the index {result}") 

'''
    
    
        



       
        




        

