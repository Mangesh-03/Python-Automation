###############################################################
# Project        : Process Automation Tool
# Description    : It used to periodically log details of running process
# Author         : Mangesh Ashok Bedre
# Date           : 15 June 2025
###############################################################

import psutil
import os
import time
import schedule
import sys
import smtplib
from email.message import EmailMessage

###############################################################
# Function Name  : CreateLog
# Description    : Creates a log file and writes all running 
#                  process details into it
# Parameters     : FolderName (str) - Name of folder to store logs
# Returns        : None
###############################################################

def CreateLog(FolderName):
    
    if not os.path.exists(FolderName):
        os.mkdir(FolderName)

    timestamp = time.ctime()

    timestamp = timestamp.replace(" ","_")
    timestamp = timestamp.replace(":","_") 
    timestamp = timestamp.replace("/","_")     

    FileName = os.path.join(FolderName,"Marvellous%s.log" %(timestamp)) 

    fobj = open(FileName,"w")
    Border = "="*80
    
    fobj.write(Border+"\n")
    fobj.write("\tMarvellous InfoSystem Process log"+"\n")
    fobj.write("\tLog File is Created at : "+timestamp+"\n")  
    fobj.write(Border+"\n")  

    fobj.write("\n")  
    fobj.write("\n")

    Data = ProcessScan()
    
    for value in Data:
        # fobj.write(str(value)+"\n")
        fobj.write("%s \n\n" %(value))
          

    fobj.write(Border+"\n")
    fobj.close() 

    logPath = FileName
    logPath = logPath.replace("\\","/")
    SendMail(logPath)

###############################################################
# Function Name  : ProcessScan
# Description    : Scans all currently running processes and 
#                  records their PID, name, username and memory usage
# Parameters     : None
# Returns        : list (List of process information dictionaries)
###############################################################

def ProcessScan():
    listProcess = []

    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs=['pid','name','username'])
            info['vms'] = proc.memory_info().vms/(1024 *1024)
            listProcess.append(info)

        except (psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess) :
            pass

    return listProcess

###############################################################
# Function Name  : SendMail
# Description    : Sends the generated log file as an email attachment
#                  using SMTP. Works with Gmail App Password.
# Parameters     : logFile (str) – Absolute path of log file to send
# Returns        : None
###############################################################


def SendMail(logFile):

    SenderMail = "logfile29@gmail.com"
    SenderPass = "ykpr wumw tgtz vtpm"
    reciverMail = "mangeshbedre7@gmail.com"
    MailServer = "smtp.gmail.com"
    port = 587
    logFilePath = logFile
    print(logFilePath)  

    try:
        msg = EmailMessage()

        msg["From"] = SenderMail
        msg["To"] = reciverMail
        msg["Subject"] = "Log File report"

        fobj = open(logFilePath,"rb")
        
        FileData = fobj.read()
        print("size: ",len(FileData))
        FileName = logFile.split("/")[-1]

        msg.add_attachment( 
            FileData,
            maintype = "application",
            subtype = "octet-stream",
            filename = FileName
        )

        Server = smtplib.SMTP(MailServer,port)

        Server.starttls()
        Server.login(SenderMail,SenderPass)
        Server.send_message(msg)
        Server.quit()
        fobj.close()

    except Exception as e:
        print("Exception : ",e)

###############################################################
# Function Name  : main
# Description    : Entry point of the script. Handles command-line 
#                  arguments and triggers the scheduler.
# Parameters     : None
# Returns        : None
###############################################################

def main():

    Border = "-"*54
    print(Border)
    print("-------------Process Automation--------------------")
    print(Border)

    if(len(sys.argv)==2):
        if((sys.argv[1] == "--h") or (sys.argv[1]=="--H")):
            print("This application is periodically log details of running process")
            print("This is the process automation script")
        
        elif((sys.argv[1] == "--u") or (sys.argv[1]=="--U")):
            print("Use the given script as")
            print("ScriptName.py folderName")
            print("Plz provide valid Absolute path")
        
        else:
            schedule.every(1).minutes.do(CreateLog,(sys.argv[1]))

            while True:
                schedule.run_pending()
                time.sleep(1)

    else:
        print("Invalid Number of commandline Arguments")
        print("Use the given flag as")
        print("--h used to display help")
        print("--u used to display usage")

    print(Border)
    print("------------Thank you for using our script------------")
    print(Border)

    
if(__name__=="__main__"):
    main()