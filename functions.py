import statics
def print_name(name):
    print(statics.home_welcome_heading, name)

my_name=input("What is your name: ")
print_name(my_name)

my_info=open("info.txt","w+")
my_info.write(my_name)
my_info.close()

