"""mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]"""

#use x to print out the entire list when using for
ghost_list = ["Samara", "Casper", "Slimer", "Beetlejuice"]
for x in ghost_list:
    print(x)

for x in "Beetlejuice": #You can use x to print out every character in a string
    print(x)

for x in ghost_list:
    print(x)
    if x == "Casper":
        break #break will stop a loop in for loops. Stop the condition. 
    print(x)

for x in ghost_list:
    if x == "Slimer":
        continue  #Continue will skip the current condition. it will continue to the next line. So, it will skip "slimer"
    print(x)


for x in range(7): #You can print out ranges, this will print out 0-6 totalling 7 digits. 
    print(x)
else:
    print("Finished Program")  #This else statement will make it so the print statement happens after we arrive at the specified digit.
#If you put a break before your else, the else will not print. 


movie_list = ["Ring", "Casper", "Ghostbusters", "Beetlejuice"]

for x in ghost_list:
    for y in movie_list:  #X will have the same value until it runs out of elements (Partners). So Samara, until is is paired with all movie names here. 
        print(x, y)

#Write a program
##############
#Fizzbuzz program - basic interview program (oldschool)
for fizzbuzz in range(100):
#if numeber is divisable by 3 print out fizz
#if number is divisbale by 5 print out buzz
#if number is divisable by both 3 and 5, print out fizzbuzz.
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0: #Using % key means divisable by
        print("Fizzbuzz") 

    elif fizzbuzz % 5 == 0: 
        print("buzz")

    elif fizzbuzz % 3 == 0:   #If a number is divisbale by another there is nothing left, so the result check would be 0
        print("Fizz")

    else:
        print(str(fizzbuzz)) 


#If statement for earlier tham 2000. Use less than. Not less than or equal to.
#use a lot of len?
#You can do this without continue.
#No breaks either. 
#Output needs to match. 
#Algorithm. 