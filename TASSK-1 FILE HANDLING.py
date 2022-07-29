x=open("task-1.txt","w")
my_output=["ENTER YOUR EMAIL ID : abcde@gmail.com\n","VALID EMAIL ID\n","ENTER YOUR PASSWORD: AbcdE@@1234\n","VALID PASSWORD"]
x.writelines(my_output)

x=open("task-1.txt","r")
print(x.read())
x.close()
