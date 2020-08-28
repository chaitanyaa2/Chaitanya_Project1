from matplotlib import pyplot as plt
from matplotlib import style
#PART 1
#taking a string input
line=input('Enter a line :')
# a list of words in the string
words=line.split()
l1=list()
l2=list()
counts=dict()
# a dictionary with word count
for word in words:
    counts[word]=counts.get(word,0)+1
#list of tuples including each word and it's length
for k,v in counts.items():
    a=len(k)
    l2.append((k,a))
print('Length of each word : ',l2)
#word count in decreasing order
l1=sorted([(v,k) for k,v in counts.items()],reverse=True)
#displaying the list of tuples
print('Word count in decreasing order : ',l1)
# PART 2
#taking email id as Input
email=input('Enter your college mail id : ')
x=email.find('@')
#extracting student number
stno=email[x-7:x]
#extracting student name
name=email[:x-7]
print('Student Name :',name)
print('Student Number :',stno)
# PART 3
# menu driven program
s=input('Enter\n1 for Line Graph\n2 for Bar Graph\n3 for Histogram\n4 for Scatter Plot\n5 for Stack Plot\n6 for Pie Plot\n')
x=int(s)
#to display a line graph
if x==1:
    style.use('ggplot')
    plt.plot([0,3,6,9],[0,3,2,5],'c',label='line one',linewidth=5)
    plt.title('Line Graph')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.legend()
    plt.grid(True,color='k')
    plt.show()
#to display a bar graph
elif x==2:
    style.use('dark_background')
    plt.bar([2,4,6,8,10],[5,7,2,9,4],label='Ex One',color='pink')
    plt.bar([1,3,5,7,9],[8,3,6,10,3],label='Ex Two',color='c')
    plt.legend()
    plt.xlabel('bar number')
    plt.ylabel('bar height')
    plt.title('Bar Graph')
    plt.show()
#to display a histogram
elif x==3:
    style.use('dark_background')
    age=[1,3,4,8,9,4,3,5,7,5,3,2,8,7,5,7,9,3,2,8,9,3,8]
    bins=[0,2,4,6,8,10]
    plt.hist(age,bins,histtype='bar',rwidth=0.5,color='pink')
    plt.title('Histogram')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.show()
#to display a scatter plot
elif x==4:
    style.use('ggplot')
    x=[1,2,3,4,5,6,7,8]
    y=[3,5,2,9,7,5,9,6]
    plt.scatter(x,y,label='python',color='k')
    plt.title('Scatter Plot')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.legend()
    plt.show()
#to display a stack plot
elif x==5:
    x=[1,2,3,4,5]
    a=[7,8,6,7,11]
    b=[2,3,4,2,7]
    c=[7,2,9,6,4]
    d=[8,7,4,9,1]
    plt.plot([],[],color='m',label='a',linewidth=5)
    plt.plot([],[],color='c',label='b',linewidth=5)
    plt.plot([],[],color='r',label='c',linewidth=5)
    plt.plot([],[],color='k',label='d',linewidth=5)
    plt.stackplot(x,a,b,c,d,colors=['m','c','r','k'])
    plt.title('Stack Plot')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.legend()
    plt.show()
#to display a pie plot
elif x==6:
    slices=[7,2,2,13]
    work=['a','b','c','d']
    col=['c','m','r','b']
    plt.pie(slices,labels=work,colors=col,startangle=90,shadow=True,explode=(0,0.3,0,0.06),autopct='%1.1f%%')
    plt.title('Pie Plot')
    plt.show()
#in case of wrong input
else:
    print('Invalid Input')
