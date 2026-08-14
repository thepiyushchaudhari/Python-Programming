import psutil, sys, os, time, schedule

def PlatformSurvillance(FolderName):
    Border = "--"*50

    Ret = False

    Ret = os.path.exists(FolderName)

    if(Ret == True):
        Ret = os.path.isdir(FolderName)

        if(Ret == False):
            print("Unable to proceed as directory name is existing but it is not a directory")
            return

    else:
        os.mkdir(FolderName)  
        print("Directory for the log file created successfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    FileName = os.path.join(FolderName,"Marvellous_%s.log" %timestamp)

    fobj= open(FileName,"w")

    print(f"Log file created successfully with name {FileName}")

    fobj.write(Border+"\n")
    fobj.write("-----Marvellous Platform Survillence System-----\n")
    fobj.write("Log file created at : "+ timestamp+"\n")
    fobj.write(Border+"\n\n")

    fobj.write("-------------------- System Report --------------------\n")

    fobj.write("Number of active CPU Cores : %s\n" %psutil.cpu_count())
    fobj.write("CPU Usage : %s %%\n"%psutil.cpu_percent())
    fobj.write(Border+"\n")

    fobj.write("\n\n\n\n\n\n\n\n\n\n")

    fobj.write(Border+"\n")
    fobj.write("-------------------- End of Log File --------------------\n")
    fobj.write(Border+"\n")

    fobj.close()

def main():
    Border = "--"*50

    print(Border)
    print("----- Marvellous Platform Survillence System -----")
    print(Border)

    # -- h and --u handeling
    if(len(sys.argv) == 2):
        if((sys.argv[1]) == "--h" or (sys.argv[1]) == "--H"):
            print("This automation script is used to perform ")
            print("1: It fetches the information of running process")
            print("2: It fetches the information about the primary storage as RAM")
            print("3: It fetches the information about the secondary stoarge as HDD")
            print("4: It fetches the information about the microprocessor")
            print("5: It gets auto scheduled periodically")
            print("6: It maintains all records into a log file")
            print("7: It sends the log files through mail periodically")

        elif((sys.argv[1]) == "--u" or (sys.argv[1]) == "--U"):
            print("Use the automation script as : ")
            print(f"python {sys.argv[0]} Time_Interval Folder_Name")
            print("Time_Interval : Time in minutes for periodic execution")
            print("Filder_Name : To store the log files that will be created")
            

        else:
            print("Invalid Number of Arguments")


    #Actual project code
    elif(len(sys.argv) == 3):

        #print("CPU Usage : ",psutil.cpu_percent())
        print("Scheduler Started Successfully")
        print("Press ctrl + C to abort the automation script")

        schedule.every(int(sys.argv[1])).minutes.do(PlatformSurvillance, sys.argv[2])

        while(True):
            schedule.run_pending()
            time.sleep(1)
            

    else:
        print("Unable to proceed as Arguments are not matching")
        print("Please use --h or --u flags to get more details")


    print(Border)
    print("-----Thank You for using our Automation System-----")
    print(Border)

if __name__ == "__main__":
    main()