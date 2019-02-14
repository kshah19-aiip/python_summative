import csv
import random
import datetime

#Creates timestamp for data and empty list to contain generated data
today = datetime.datetime.now()
timestamp = [today.strftime("%d/%m/%Y, %X")]
dataset = []

#Ask user to input number of clusters and no of sensors/cluster for data generation
no_of_clusters = int(input("Please input number of clusters for which readings are to be generated: "))
no_of_sensors = int(input("Please input number of sensors per cluster: "))

'''
Generate randomised sensor readings for user-defined no of sensors and store in list called "sensor_readings"
Then add this list of readings into the 'dataset' list such as to contain a 16-reading list for each cluster
'''
for i in range(0,no_of_clusters):
    sensor_readings = [random.random() for j in range(0,no_of_sensors)]
    dataset.append(["cluster_" + str(i+1)] + sensor_readings)

#Write sensor readings to csv file named "sensor_data.csv" and create file if it does not exist
#The mode 'a' ensures no data is overwritten when a new set is generated
with open("sensor_data.csv", "a") as f:
    writer = csv.writer(f)
    writer.writerow(timestamp)
    writer.writerows(dataset)

#Assign error number if the data set has 'err' recorded in it for a failed sensor
#Also initialise an empty list to record all entries of failed sensors
error = 101
error_list = []

#Function to perform diagnosis on recorded data to locate failed sensors
def diagnosis_function(inputvalue):

    #Check all recorded data in file to give the location of failed sensors and add this along with error
    #code to the empty list 'error_list' initialised above
    with open("sensor_data.csv", 'r') as f:
        reader = csv.reader(f, delimiter = ',')
        for row in reader:
            if "err" in row:
                error_list.append("Error" + str(error) + " Sensor no." + str(row.index("err"))
                      + " " + str(row[0]) + " failure")

    '''
    Create (if not already existing) and write all the entries in the error list to a text file called 
    error_log.txt along with date and time stamp of the diagnosis. 
    Mode 'a' ensures no data is overwritten in the text file
    '''
    #print(error_list)
    with open("error_log.txt", "a") as logfile:
        logfile.write(str(timestamp) + " " + str(error_list) + '\n')

    #Ouput of textfile to display contents of the log file
    with open("error_log.txt", "r") as logfile:
        for line in logfile:
            print(line)

#Ask user if they want to perform a diagnosis for failed sensors on recorded data or not
diag_decision = (input("Would you like to check all recorded data for sensor failures? Enter Y for Yes "
                   "or any other letter for No: "))

#If user inputs 'Y' then call the diagnosis function to check for all failed sensors in dataset
if diag_decision.lower() in ["y"]:
    diagnosis_function(diag_decision)

else:
    exit()
