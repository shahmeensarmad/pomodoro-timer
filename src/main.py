#main.py
# ENDG 233 F24
# STUDENT NAME(S): Jasleen Ghotra and Shahmeen Sarmad
# GROUP NUMBER: 23
# A terminal-based data analysis and visualization program in Python.
import user_csv #import user_csv module
import numpy as np #import numpy 
import design_analysis #import design analysis module
import matplotlib.pyplot as plt #import mathplotlib.pyplot 

#make a 2d numpy array of our data and have it be read using our read_csv function under user_csv
country_array = np.array(user_csv.read_csv("Country_Data.csv"))
threatened_species_array = np.array(user_csv.read_csv("Threatened_Species.csv"))
population_array = np.array(user_csv.read_csv("Population_Data.csv"))

#while true loop that runs program until user wants to quit
while True:
    #get subregion from user by calling get_sub_region function from design analysis module
    subregion = design_analysis.get_subregion(country_array)
    #if user inputs "0" as subregion, break out of loop
    if subregion == "0":
        break
    #ask user to pick a country in sub_region using the get_sub_region_country function from design analysis module
    user_country = design_analysis.get_user_country(country_array, subregion)
    
    #display menu options to users using the print_options functions drom design analysis module
    user_option = design_analysis.print_options()
    #if user option equals 1, display the maximum population of country user picked
    if user_option == 1:
        design_analysis.maximum_population(user_country, population_array)

    #else if user option equals 2, display the minimum population of country user picked
    elif user_option == 2:
        design_analysis.minimum_population(user_country, population_array)

    #else if user option equals 3, display the average population of country user picked
    elif user_option == 3:
        design_analysis.average_population(user_country, population_array)

    #else if user option equals 0, skip the rest of the code below and take user back to main menu
    elif user_option == 0:
        continue

    #find all the countries in users specified subregion using the get_subregion_countries function from design analysis module
    countries_in_subregion = design_analysis.get_subregion_countries(subregion, country_array)
    #find UN region for which the user subregion falls under using find_UN_region function from design analysis
    un_region = design_analysis.find_UN_region(subregion, country_array)
    #get the average threatened species in all the countries in user subregion 
    countries_avg_threatened_species = design_analysis.avg_threatened_species(countries_in_subregion, threatened_species_array)
    #get the total amount of threatened species in all the countries in user subregion
    countries_total_threatened_species = design_analysis.total_threatened_species(countries_in_subregion, threatened_species_array)
    #get the threatened species per sq km in all countries in user subregion
    countries_threatened_species_per_sq_km = design_analysis.threatened_species_per_sq_km(countries_in_subregion, threatened_species_array, country_array)

    #Display UN region that subregion falls under to user
    print(f"\nUN Region: {un_region}")
    #Display user subregion to user
    print(f"\nUN subregion: {subregion}")
    
    print("\nThe average number of threatened species in each country of the subregion is:")

    #loop through countries_in_subregion to find each position corresponding to each country 
    for index, country in enumerate(countries_in_subregion):
        #display the country at that index with its average threatened species (rounded to one decimal place)
        print(f"{country}; {countries_avg_threatened_species[index]:.1f}")
    
    
    print("\nThe total number of threatened species in each country of the subregion is:")

    #loop through countries_in_subregion to find each position corresponding to each country
    for index, country in enumerate(countries_in_subregion):
        #display the country at that index with its total threatened species as integer value
        print(f"{country}; {int(countries_total_threatened_species[index])}")

    print("\nThe calculated number of threatened species per sq km area in each country of the subregion is:")

    #loop through countries_in_subregion to find each position corresponding to each country
    for index, country in enumerate(countries_in_subregion):
        #if we get a negative value (meaning the square km was the -1 flag value), then no data is found for country
        if countries_threatened_species_per_sq_km[index] < 0:
            print(f"{country}; no sq km data available")
        else:
            #display the country at that index with its threatened species per sq km
            print(f"{country}; {countries_threatened_species_per_sq_km[index]:.5f}")
    
    #set output data to equal headers
    output_data = [["Country","Avg Threathened Species", "Total Threatened Species", "Threatened Species per sq km"]]
    
    #loop through countries in subregion to each position corresponding with each country
    for index, country in enumerate(countries_in_subregion):
        #append the country, the average threatened species, the total threatened species and the threatened species per sq km for that country to output data
        output_data.append([country,
        f"{countries_avg_threatened_species[index]:.1f}",
        f"{int(countries_total_threatened_species[index])}",
        f"{countries_threatened_species_per_sq_km[index]:.5f}"
        ])
    #use write_csv function to write a new file with the subregion and its threatened species results
    user_csv.write_csv(f"{subregion}_Threatened_Species_Results.csv", output_data, overwrite=True)

# Matplotlib - Creates the plots that show the Total and Average Number of Threatened Species in each country within the user inputed subregion
    
    # Dictates the figure size. The width is 5 times the number of countries in the subregion (as this could vary), and the height is 5
    plt.figure(figsize=(5*len(countries_in_subregion), 5))

    # Dictates which subplot to graph. 
    # plt.subplot(a, b, c)
    # a = number of rows
    # b = number of columns
    # c = the index of the subplot
    plt.subplot(2,1,1)
    # Title of the subplot
    plt.title("Total Number of Threatened Species")
    # Labels the y axis of the subplot 
    plt.ylabel("Number of Species")
    # Labels the x axis of the subplot
    plt.xlabel("Country")

    #loop through countries_in_subregion to find each position corresponding to each country
    for index, country in enumerate(countries_in_subregion):
        #creates a bar graph for total threatened species with the country names associated with each bar
        plt.bar(country, countries_total_threatened_species[index])

    # 2 rows, 1 column, subplot at index 2 
    plt.subplot(2,1,2)
    # Title of Subplot
    plt.title("Average Number of Threatened Species")
    # Y axis label of Suplot
    plt.ylabel("Average Number of Species")
    # X axis label of subplot 
    plt.xlabel("Country")

    #loop through countries_in_subregion to find each position corresponding to each country
    for index, country in enumerate(countries_in_subregion):
        #creates a bar graph for average threatened species with the country names associated with each bar
        plt.bar(country, countries_avg_threatened_species[index])


    # Automatically adjusts spacing between subplots to prevent overlapping
    plt.tight_layout()
    # Ensures that the program continues, and that the plots do not block the program until the user closes them 
    plt.show(block = False)