mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]


#Count the total number of missions
total_missions = (len(mission_names)) #So here we will count the total number of values/items within mission_names
print("Total Number of Missions: ", + total_missions) #Then as requested, we are outputting the number of missions.

#Count the total Number of Successful missions
successful_missions = sum(mission_success) #Honestly, courtesy of my girlfriend the beginning indie game dev, I got some help with using "sum" to count the True values. 
print("Number of Successful Missions: ", + successful_missions) #Here we are outputting the number of successful missions. Doing this by counting every True value in mission_success

#Calulate the mission success rate
success_rate = (successful_missions / total_missions) * 100 #Formula here for calculating how many missions were successful over how many missions total.
print(f"Success Rate: {success_rate: .2f}%") #This will print the success rate evaluated above limitied to two decimal points. I picked up the .2f from my CS 110 class, pretty handy, also, I dont want to talk about how long it took me to put the % key in. 

#Count number of missions before 2000
print("Missions launched before the year 2000: ")
for i in range(len(mission_years)): #here we are looking at a range, the range is the number of values in mission_years. Only for loop in the code thank goodness. 
    if mission_years[i] < 2000: #If the mission year is less than 2000, it is counted, if not, then it will not be a factor. 
        print(mission_names[i]) #Finally, we will output the number of missions launched before the year 2000