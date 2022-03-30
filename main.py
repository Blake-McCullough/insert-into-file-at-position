#Made By Blake McCullough
#Discord - Spoiled_Kitten#4911
#Github - https://github.com/Blake-McCullough/
#Email - privblakemccullough@protonmail.com
#Website - https://blakemccullough.com/
#
#
#For colour text in terminal :)
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
  
#For manually inserting a string at a specific line
def insertintofile(filename,location,input):
  try:
    print(f"{bcolors.OKBLUE}INFO:Inserting value at postition {str(location)}\n{bcolors.ENDC}")
    print()
    with open(filename, 'r') as f:
            lines = f.readlines()
  
    inputed = input+'\n'
    lines.insert(location, inputed)
  
    with open(filename, 'w') as f:
      
            for line in lines:
              
              f.write(line)
  except ValueError:
    print(f"{bcolors.FAIL}Error: Make sure input is an int.{bcolors.ENDC}")



#
#
#Will find the index of the first string that matches the value and then will add after that, puts back into string :)
def insertintofileafterstring(filename,beforestring,input):
  try:
    print(f"{bcolors.OKBLUE}INFO:Inserting value after string {beforestring}\n{bcolors.ENDC}")
    with open(filename, 'r') as f:
            lines = f.readlines()
    beforestringed= beforestring + '\n'
    location = lines.index(beforestringed) +1
    inputed = input+'\n'
    lines.insert(location, inputed)
  
    with open(filename, 'w') as f:
      
            for line in lines:
              
              f.write(line)
  except ValueError:
    print(f"{bcolors.FAIL}Error: The value entered is not in the list,\nmake sure it is spelt correct.\nValue is case sensitive.{bcolors.ENDC}")


#so doesn't instantly run if imported.
if __name__ == "__main__":
  insertintofile('info.txt',2,'I Was inserted from manual index')
  insertintofileafterstring('info.txt','him','I Was inserted two')
