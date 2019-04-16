#i/o


#
# my_file = open("C:/Users/adir.israeli/Documents/text file-Adir.txt")
# content = my_file.read()   #in this line we create variable and call the read function in order to view the content
# print(content)

#
# # #reading ability
# my_file = open("C:/Users/adir.israeli/Documents/text file-Adir.txt" , 'r')
# moshe = my_file.read()
# print(moshe)   #that will show the ontent of the text file


#adding write ability and print the new content + reading +close

# my_file = open("C:/Users/adir.israeli/Documents/text file-Adir.txt" , 'r+')
# moshe = my_file.write("moshe the dog")
# my_file.close()     #after every row we should put close command
# my_file = open("C:/Users/adir.israeli/Documents/text file-Adir.txt" , 'r')
# moshe = my_file.read()
# my_file.close()
# print(moshe)


#IO + adding encoding

# my_file = open("C:/Users/adir.israeli/Documents/text file-Adir.txt" , 'r' , encoding='utf-8')
# content = my_file.read()
# print(content)




#Error handing - exceptions (file name incorrect\events that occured\no permission to file..)

# my_file = open("C:/Users/adir.israeli/Documents/text file-Adire.txt" , 'r' , encoding='utf-8')
# content = my_file.read()
# print(content)



#Error handling + try & except (PAY ATTENTION FOR IDENTATION)

# try:
#     my_file = open("C:/Users/adir.israeli/Documents/text file-Adire.txt" , 'r' , encoding='utf-8')
#     content = my_file.read()
# except IOError:
#     print("eRROR:FILE DOWS NOT EXIST")




#Error handling + throwing the error exception into variable called e

# try:
#     my_file = open("C:/Users/adir.israeli/Documents/text file-Adire.txt" , 'r' , encoding='utf-8')
#     content = my_file.read()
# except IOError as e:
#     print(e)
#     print("eRROR:FILE DOWS NOT EXIST")

# print(123)  #printing some integers in order to make sure the code continue running after error exception



# #Error handling = Adding Finally
# try:
#     my_file = open("C:/Users/adir.israeli/Documents/text file-Adire.txt", 'r', encoding='utf-8')
# except IOError:
#     print("fatal error")
# finally:
#     print("this will run anyway")


#
# #Error handling- try + finally without except  (note: finally notification will presented before the error)
#
# try:
#     my_file = open("C:/Users/adir.israeli/Documents/text file-Adire.txt", 'r', encoding='utf-8')
# finally:
#     print("this will run anyway")


#Debugger+breakpoint

# try:
#     my_file = open("C:/Users/adir.israeli/Documents/text file-Adire.txt", 'r', encoding='utf-8')
# except IOError:
#     print("fatal error")
# finally:
#     print("this will run anyway")


# #another example for debuger and breakpoint(
# X = 5
# X = 8
# X = 80
# print(x)
#






