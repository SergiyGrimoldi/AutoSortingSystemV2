from itertools import count
from locale import RADIXCHAR
import os
import shutil
from tkinter import E
from colorama import Fore, init, Back, Style
import time
init(autoreset=True)

title  =(Style.BRIGHT + Back.WHITE + Fore.RED + "Automatic Sorting System - By Sergiy Grimoldi ")

def clear():
    try:
        os.system('clear') 
    except:
        os.system('cls') 
    finally:
        None

def main():
    
    directory_to_scan = "/Users/s.grimoldi/Downloads"
    
    files = [] 
    
    try:
        for file in os.scandir(directory_to_scan): 
            
            if file.is_file(): 
                file=(file.name) 
                 
                files.append(file)

    except: 
        None
    
    count_done = 0 

    for file in files: 

        if (file == ".DS_Store"):
            continue
       
        file_extension = file.split(".")[-1] 
        
        if file_extension == "crdownload":
            continue
        
        full_dir_file = f"{directory_to_scan}/{file}" 

        check_if_exsist = f"{directory_to_scan}/{file_extension}" 
        to_check = os.path.isdir(check_if_exsist) 

        if not to_check:
            os.makedirs(check_if_exsist) 

            try:
                shutil.move(full_dir_file, check_if_exsist) 
                count_done+=1
            
            except Exception as e:
                print(e)

        else: 
            try:
                shutil.move(full_dir_file, check_if_exsist) 
                count_done+=1 
               
                with open ("/Users/s.grimoldi/log_sorting_download_folder.csv", "a+") as l:
                    file_name = str(full_dir_file.split("/")[-1])
                    log = f"File < {Fore.RED + file_name +Fore.RESET} > moved to < {Fore.GREEN + check_if_exsist + Fore.RESET} >\n"
                    l.write(log)
                    print(log)
                l.close()


            except Exception as e:
                print(e) 
                
         
    if count_done==0:
        status = "Nothing to do, all files are sorted."
        print(f"{Fore.RED + status +Fore.RESET}")
        time.sleep(5)
        clear()
        exit()

def config():
    clear()
    print(title)
    
    print ("1. Scan dir and Create folders")
    print( "2. ...")
    print ("3. ...")
    print ("4. ...")
    print ("5. Exit")

    print (67 * "-")


    choice = input("Enter your choice [1-5]: ")

    if choice=="1":   
        clear()  
        print(title)
        main()

    elif choice=="5":
        clear()
        print(title)
        print("Goodye!")
        time.sleep(5)
        clear()
        exit()
    else:
        # Any integer inputs other than values 1-5 we print an error message
        print("Wrong option selection. Enter any key to try again..")
        time.sleep(2)
        config()


config()