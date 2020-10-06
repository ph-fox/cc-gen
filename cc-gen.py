import time, random, colorama, os, sys
from colorama import Fore

version = "1.3"
os.system("clear")
char = "1234567890"
char_lst = list(char)
ch = ["01","02","03","04","05","06","07","08","09","10","11","12",]
ch_lst = list(ch)
yyyy = ["2021","2022","2023","2024","2025","2026","2027","2028",]
cvv ='123'
cc = '12345'

print("""\033[1;31;40m

 ██████╗
██╔════╝
██║     
██║     
╚██████╗
 ╚═════╝ 
                                                     
""")

time.sleep(.3)
os.system("clear")

print("""\033[1;31;40m

 ██████╗ ██████╗           
██╔════╝██╔════╝          
██║     ██║         █████╗
██║     ██║         ╚════╝
╚██████╗╚██████╗          
 ╚═════╝ ╚═════╝          
                                                     
""")

time.sleep(.3)
os.system("clear")

print("""\033[1;31;40m

 ██████╗ ██████╗           ██████╗
██╔════╝██╔════╝          ██╔════╝ 
██║     ██║         █████╗██║  ███╗
██║     ██║         ╚════╝██║   ██║
╚██████╗╚██████╗          ╚██████╔╝
 ╚═════╝ ╚═════╝           ╚═════╝ 
                                                     
""")

time.sleep(.3)
os.system("clear")

print("""\033[1;31;40m

 ██████╗ ██████╗           ██████╗ ███████╗
██╔════╝██╔════╝          ██╔════╝ ██╔════╝
██║     ██║         █████╗██║  ███╗█████╗  
██║     ██║         ╚════╝██║   ██║██╔══╝  
╚██████╗╚██████╗          ╚██████╔╝███████╗
 ╚═════╝ ╚═════╝           ╚═════╝ ╚══════╝
                                                     
""")

time.sleep(.3)
os.system("clear")

print("""\033[1;31;40m

 ██████╗ ██████╗           ██████╗ ███████╗███╗   ██╗
██╔════╝██╔════╝          ██╔════╝ ██╔════╝████╗  ██║
██║     ██║         █████╗██║  ███╗█████╗  ██╔██╗ ██║
██║     ██║         ╚════╝██║   ██║██╔══╝  ██║╚██╗██║
╚██████╗╚██████╗          ╚██████╔╝███████╗██║ ╚████║
 ╚═════╝ ╚═════╝           ╚═════╝ ╚══════╝╚═╝  ╚═══╝
                                                     
""")

print(Fore.GREEN+"coded by: Anikin Luke")

while True:
    
    print("type 'help' to show commands")
    ui = input(Fore.YELLOW+">").lower()

    if(ui =="start"):
        amount = int(input("Enter amount of cc to generate:"))
    
        for i in range(amount):
            ran = random.choices(char_lst, k=len(cc))
            ran_mm = random.choices(ch_lst)
            ran_y = random.choices(list(yyyy))
            ran_cvv = random.choices(char_lst, k=len(cvv))
        
            print("45101560210"+"".join(ran)+"|"+''.join(ran_mm)+"|"+''.join(ran_y)+"|"+''.join(ran_cvv))
            time.sleep(.1)
            
        print("generated successfully!")
        
    elif(ui =="help"):
        print("""
=============================================
+|   CC Generator coded by Anikin Luke     |+
=============================================
+|     COMMANDS            Decription      |+
+|-----------------------------------------|+
+|     start   --  To Start generating cc  |+
+|     About   --  To show dev info.       |+
+|     Exit    --  To quit the program.    |+
+|     Help    -- To show commands         |+
+|    update   --   Comming soon! no       |+
+|     update command not working yet      |+
 ===========================================

        """)
        
    elif(ui=="exit"):
        print("goodbye!.. :(")
        break
    
    elif(ui=="about"):
        print(f"""
    =============================================
    +|             About this tool             |+
    =============================================
    +|              This Tool Is               |+
    +|               Is Created                |+
    +|                   By                    |+
    +|            Anikin Luke Abales           |+
    +|  for SudoCentercorp team CyberHackers   |+
    +|-----------------------------------------|+
    +| Tool name: CC generator                 |+
    +| Use To Generate Credit card info's      |+
    +| Tool version: {version}                      |+
    +|-----------------------------------------|+
    +|                Contact                  |+
    +|        Facebook-Group                   |+
    +|  facebook.com/groups/sudocyberhackers   |+
    +|--------------^--------^-----------------|+
    +|   Email: Anonnewshacker@gmail.com       |+
    +|   Github: abalesluke                    |+
    +|                                         |+
    +|                 Note!                   |+
    +|   This tool is now available on github  |+
    +|   so please dont republish it on github |+
    +|   i do not autorized you to edit this   |+
    +|   tool or republish it on github.       |+
    +|                                         |+
    +|         Editing or changing the         |+
    +|       name of the coder or developer    |+
    +|        wont make you a programmer.      |+
    +|                                         |+
    +|        [+]Respect the coder's[+]        |+
     ===========================================  
        """)
        
    else:
        print("Command not found!")
        print("Try typing 'help'")
    
    
