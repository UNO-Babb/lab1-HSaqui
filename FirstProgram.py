#FirstProgram.py
#Name:
#Date:
#Assignment:

def main():
  #Say hello
  print("hello")
  #Ask for the user's name
  name = input("what is your name")
  #Use the user's name in the program.
  print("Good to meet you",name)
  #Ask the user for their age.
  age = input("how old are you")
  #Tell the user what year they were born in.
  
  age = int(age)
  Birthyear = 2024 - age
  #Assume that they have not had their birthday yet this year.
  print("2024", Birthyear )
#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
