#Chapter 2 from the book
#Python Zen
import this

#on the beginning of this chapter there is a good description of how to create virtual enviroments in order to use anaconda
#I will be using vs code, though

#Spacing
for i in [1,2,3,4,5]:
    print(i) #this spacing indicates that this print is inside the 'for' on line 9

    for j in [1,2,3,4,5]:
        print(j)
        print(i+j)
    print(i)

print('done looping')

