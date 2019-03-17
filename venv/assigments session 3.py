# try:
#     a = 1/0:
# except
#     print("Mission Done")
#
#
# 3. Yes
#
# 4.tatement, followed by a block of code which
# handles the kind of the problem which was defined.
#
# 5+6
# We can also provide a generic except clause, which handles any exception (bare except).
# - Except
# or we can focus Python on  particular block of code   which
# handles the kind of the problem which was defined.
# - ExceptIOError
#
#
# 7 . Except IOError - refers to  issues withI/O (input/output) exceptions
# Except ZeroDivisionError - refersto issues with divison by zero

# 8+9+10

adir_file = open("C:/Users/adir.israeli/Documents/words.txt" , 'r+' , encoding='utf-8')
content = adir_file.write("The world is yours -scarface")
adir_file.close()
adir_file = open("C:/Users/adir.israeli/Documents/words.txt" , 'r')
content = adir_file.read()
adir_file.close()
print("content")
adir_file = open("C:/Users/adir.israeli/Documents/words.txt" , 'a' , encoding='utf-8')
content = adir_file.write("מה המצב גבר")
adir_file.close()
print("content")