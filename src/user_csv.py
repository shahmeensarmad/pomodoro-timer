# user_csv.py
# ENDG 233 F24
# STUDENT NAME(S): Jasleen Ghotra and Shahmeen Sarmad
# GROUP NUMBER: 23
# A terminal-based data analysis and visualization program in Python.
# You must follow the specifications provided in the project description.
# Remember to include docstrings and comments throughout your code.


def read_csv(filename, include_header = True):
    """ 
    Takes the filename and returns the data as a nested list

    Parameters:
    filename (str): The name of the file being read
    include_header (bool): indicates whether to include the header in returned data

    Returns:
    data (2D list): contains the data from the file in a 2D list, with each sublist being a row

    """
    f = open("data_files/" + filename, "r")    
    data = [] #empty list of our data

    for line in f: #for each line in our lines list
        row = [] #2D list being created, empty row list
        for index in line.split(","): #split each index with a comma (making a new list)
            if index.isdigit(): #chacking to see if index is an integer
                row.append(float(index)) #convert to float
            else: #else add to row as usual
                row.append(index)
        data.append(row) #append our row list to data list making it 2D
    #if we do not want to include headers when reading csv file
    if not include_header:
        # return without headers (row 1 at index 0)
        data = data[1:]
    #close file
    f.close()
    return data #return data as a nested list



def write_csv(filename, data, overwrite):
    """
    Takes the filename and chosen data, Returns a new file which writes and stores the data, to either overwrite or append

    Parameters:
    filename (str): The name of the file being read
    data (list): contains the data selected to write into a new file
    overwrite (bool):
    if True: indicates data is being overwritten into the file
    if False: indicates data is being appended into the file

    Returns:
    "{filename}" (file): data appended or overwritten into a new file

    """
    # if overwrite parameter is true, we know we are overwriting data
    if overwrite == True:
        option = "w" #overwrite

    #else append data to exisiting file
    else:
        option = "a" #append

    #open the file and whether we are appending or overwriting
    f = open(filename, option)

    #iterate through data
    for row in data:
        #go through each index of row
        for index in range(len(row)):
            #writing the string value corresponding to each index in row
            f.write(str(row[index]))
            #as long as we are not at our last index, seperate string with commas
            if index < len(row) - 1:
                f.write(",")
        #adds a new line after every row is iterated through    
        f.write("\n")
    #close file after writing
    f.close()