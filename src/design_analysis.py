# design_analysis.py
# ENDG 233 F25
# STUDENT NAME(S): Jasleen Ghotra and Shahmeen Sarmad
# GROUP NAME: 23
# A terminal-based data analysis and visualization program in Python.
# You must follow the specifications provided in the project description.
# Remember to include docstrings and comments throughout your code.

import numpy as np

def get_subregion(country_data):
    """Prints the prompt to select the subregion

    Parameters:
        country_data (array): an array of data obtained from the read_csv function using the Country_Data.csv file

    Returns: 
        subregion (str): a valid subregion provided by the user 
    """
    # Loops until user wants to exist program
    while True:
        # Get subregion from user by asking for user input
        subregion = input("\nPlease enter a sub-region or type '0' to quit: ")
        #if user enters in 0, exist the while loop and end program
        if subregion == "0":
            print("\nThank you for using our program.") # Display thank you message to user
            return "0" # Break out of while loop and returns "0"
        #Check if subregion exists:
        for row in country_data:
            #if in our nested list, index 2 equals user subregion return user subregion and break out of while loop
            if row[2] == subregion:
                return subregion
        #else print error, invalid input which will continue displaying until user enters valid input      
        print("\nError! Invalid input. Please try again.")

def get_user_country(country_data, subregion):
    """Prints the prompt to select the country within the subregion

    Parameters:
        country_data (array): an array of data obtained from the read_csv function using the Country_Data.csv file
        subregion (str): a valid subregion

    Returns: 
        country_subregion (str): a valid country within the subregion provided by the user
    """
    #loop that runs until user provides correct input
    while True:
        #ask user to enter a country in subregion
        user_country = input("\nPlease enter a country within the specified sub-region: ")

        #check if country user entered corresponds with entered subregion
        for row in country_data:
            if row[2] == subregion: #if in our nested list we find subregion at index 2
                if row[0] == user_country: #check to see if in that same nested list at inex 0 coutnry user inputted is found
                    return user_country # if so return user country and break out of while loop
        #else print error, invalid input which will continue displaying until user enters valid input      
        print("\nError! Invalid input. Please try again.") 

def print_options():
    """Prints the inner menu thats prompts the user to select a data analysis option and returns a valid option number

    Returns:
        int: a valid input provided by the user
    
    """

    while True:
        #display menu option
        print("\nThe program will display data related to the threatened species in every country for your selected subregion.")
        print("\nSelect any additional data you would like to display for your selected country.")
        print("\nEnter the number of the option you want to select: ")
        print("\t1)The maximum population from 2000 to 2020")
        print("\t2)The minimum population from 2000 to 2020")
        print("\t3)The average population from 2000 to 2020")
        print("\t0)Return to main menu\n>> ", end = "")

        user_option = int(input()) #user option taken as int value
        if (user_option in [0,1,2,3]): #if user option in list
            return user_option #return user_option and breaks out of while loop

        #else print error, invalid input which will continue displaying until user enters valid input
        
        print("\nError! Invalid input. Please try again.")

def maximum_population(user_country, population_data):
    """ Takes the population data and returns the maximum population in selected country

    Parameters:
        country_subregion (str): a valid country within the subregion
        population_data (array):  an array of data obtained from the read_csv function using the Population_Data.csv file
        
    """
    #iterate through each row in population data
    for row in population_data:
        #if the value at index 0 equals user country
        if row[0] == user_country:
            #make a array of all the population values from index 1 onward (this gets rid of country name)
            values = np.array(row[1:], float) #type cast values as floats
            pop_max = np.max(values) #find the maximum population from the array above
     #display max population (type cast max population to int)
    print(f"\nThe maximum population for {user_country} from 2000 to 2020 is: {int(pop_max)} people ")

def minimum_population(user_country, population_data):
    """ Takes the population data and returns the minimum population in selected country

    Parameters:
        country_subregion (str): a valid country within the subregion
        population_data (array):  an array of data obtained from the read_csv function using the Population_Data.csv file
        
    """
    #iterate through each row in population data
    for row in population_data:
        #if the value at index 0 equals user country
        if row[0] == user_country:
            #make a array of all the population values from index 1 onward (this gets rid of country name)
            values = np.array(row[1:], float)
            #find the minimum population from the array above
            pop_min = np.min(values)\
    #display min population (type cast minimum population to integer)
    print(f"\nThe minimum population for {user_country} is from 2000 to 2020 is: {int(pop_min)} people ") 


def average_population(user_country, population_data):
    """ Takes the population data and returns the average population in selected country

    Parameters:
        country_subregion (str): a valid country within the subregion
        population_data (array):  an array of data obtained from the read_csv function using the Population_Data.csv file
        
    """
    #iterate through each row in population data
    for row in population_data:
        #if the value at index 0 equals user country
        if row[0] == user_country:
            #make a array of all the population values from index 1 onward (this gets rid of country name)
            values = np.array(row[1:], float)
            #find the average population from the array above
            population_avg = np.mean(values) 
    #display average population (type cast average population as int)
    print(f"\nThe average population from 2000 to 2020 in {user_country} is: {int(population_avg)} people")

def get_subregion_countries(subregion, country_data):
    """ Takes the valid subregion and returns a list of all countries in that subregion

    Parameters:
        subregion (str): a valid subregion
        country_data (array):  an array of data obtained from the read_csv function using the Country_Data.csv file

    Returns:
        countries_in_subregion (list): all countries within the user inputed subregion

    """
    # Create an empty list to store all the countries in the valid subregion
    countries_in_subregion = []
    # for each row (sublist) in country_data
    for row in country_data:
        # if the row at index 2 (where the subregion is held) is the same as the user inputed subregion
        if row[2] == subregion:
            # Add the country (held at index 0 in each row) to the countries_in_subregion_list
            countries_in_subregion.append(row[0])
    return countries_in_subregion


def avg_threatened_species(countries_in_subregion, threatened_species_data):
    """ Takes threatened_species_data and returns the average threatened species in all countries in the subregion

    Parameters:
        countries_in_subregion (list): all countries within the user inputed subregion
        threatened_species_data (array):  an array of data obtained from the read_csv function using the Threatened_Species.csv file
    
    Returns:
        countries_avg_threatened_species (list): the average number of threatened species corresponding to each country within the subregion, ordered as countries_in_subregion
    """
    # Create an empty list to store the average threatened species corresponding to each country in the valid subregion
    countries_avg_threatened_species = []
    # for each country (the value) in countries_in_subregion
    for country in countries_in_subregion:
        # for each row (sublist) in threatened_species
        for sublist in threatened_species_data:
            # if index 0 for each sublist (where country name is held) is the same as valid country
            if sublist[0] == country:
                # Takes the number of threatened species (everything but the country name), makes it a numpy array as floats
                # [1:] from (including) index 1 to end (including last index)
                values = np.array(sublist[1:], float)
                # Appends (adds on to the end) the mean of the row to countries_avg_threatened_species (list)
                countries_avg_threatened_species.append(np.mean(values))
    return countries_avg_threatened_species    # returns the list

def total_threatened_species(countries_in_subregion, threatened_species_data):
    """ Takes threatened_species_data and returns the total number of threatened species in all countries in the subregion

    Parameters:
        countries_in_subregion (list): all countries within the user inputed subregion
        threatened_species_data (array):  an array of data obtained from the read_csv function using the Threatened_Species.csv file

    Returns:
        countries_total_threatened_species (list): the total number of threatened species corresponding to each country within the subregion, ordered as countries_in_subregion
    """
    # Creates an empty list to hold the total number of threatened species corresponding to each country
    countries_total_threatened_species = []
    # for each country (value) in countries_in_subregion
    for country in countries_in_subregion: 
        # for each row (sublist) in threatened_species
        for sublist in threatened_species_data:
            # if index 0 for each sublist (where country name is held) is the same as valid country
            if sublist[0] == country:
                # Takes the number of threatened species (everything but the country name), makes it a numpy array as floats
                # [1:] from (including) index 1 to end (including last index)
                values = np.array(sublist[1:], float)
                # Appends (adds on to the end) the sum of the row to countries_total_threatened_species (list)
                countries_total_threatened_species.append(np.sum(values))
    return countries_total_threatened_species   # returns the list

def threatened_species_per_sq_km(countries_in_subregion, threatened_species_data, country_data):
    """ Takes threatened_species_data and returns the number of threatened species per square kilometer in all countries in the subregion

    Parameters:
        countries_in_subregion (list): all countries within the user inputed subregion
        threatened_species_data (array):  an array of data obtained from the read_csv function using the Threatened_Species.csv file
        country_data (array):  an array of data obtained from the read_csv function using the Country_Data.csv file

    Returns:
        countries_threatened_species_per_sq_km (list): the number of threatened species per square kilometer corresponding to each country within the subregion, ordered as countries_in_subregion
    """
    # Creates an empty list to hold the total number of threatened species corresponding to each country
    countries_total_threatened_species = []
    # for each country (value) in countries_in_subregion
    for country in countries_in_subregion: 
        # for each row (sublist) in threatened_species
        for sublist in threatened_species_data:
            # if index 0 for each sublist (where country name is held) is the same as valid country
            if sublist[0] == country:
                # Takes the number of threatened species (everything but the country name), makes it a numpy array as floats
                # [1:] from (including) index 1 to end (including last index)
                values = np.array(sublist[1:], float)
                # Appends (adds on to the end) the sum of the row to countries_total_threatened_species (list)
                countries_total_threatened_species.append(np.sum(values))
    
    # Creates an empty list to hold the corresponding number of square km for each country
    countries_sq_km = []
    # for each country (value) in countries_in_subregion
    for country in countries_in_subregion: 
        # for each row (sublist) in country_data
        for sublist in country_data:
            # if index 0 for each sublist (where country name is held) is the same as valid country
            if sublist[0] == country:
                raw_value = sublist[3].strip()
                if raw_value == '':
                    #sets a flag value of negative one to indicate no sq km value
                    sq_km_value = -1
                else:
                    sq_km_value = float(raw_value)
                # Appends (adds on to the end) the float value of the row at index 3 (where the number of square km is held) to countries_sq_km
                countries_sq_km.append(sq_km_value)
    
    # Creates an empty list to hold the corresponding number of threatened species per sq km for each country
    countries_threatened_species_per_sq_km = []
    # for each value in countries_total_threatened_species
    for value in countries_total_threatened_species:
        # find the index at that value
        index = countries_total_threatened_species.index(value)
        # Append the countrie _total_threatened species at that index divided by the countries_square_km at the same index (as they are corresponding values)
        countries_threatened_species_per_sq_km.append(countries_total_threatened_species[index] / countries_sq_km[index])

    return countries_threatened_species_per_sq_km   # return the list

def find_UN_region(subregion, country_data):
    """ Takes the subregion and returns the corresponding UN Region

    Parameters:
        subregion (str): a valid subregion
        country_data (array):  an array of data obtained from the read_csv function using the Country_Data.csv file 

    Returns:
        row[1] (str): the corresponding UN region to the user inputed subregion


    """
    # for each row (sublist) in country_data
    for row in country_data:
        # if at index 2 of the row (where the subregion name is held) is the same as the subregion
        if row[2] == subregion:
            # return the UN region (held at index 1) corresponding to the UN Subregion
            return row[1]