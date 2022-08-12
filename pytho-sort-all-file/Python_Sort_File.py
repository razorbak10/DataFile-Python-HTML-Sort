from ast import keyword
from cgitb import text
from distutils.log import error
from doctest import testsource
import os
import glob
import time
import sys
from sys import argv
from datetime import datetime

#keyword research in file
def Take_Mul_Word(filename, list_of_strings): 
    line_number = 0
    list_of_results = []
    with open(filename, 'r') as read_obj:
        for line in read_obj:
            line_number += 1
            for string_to_search in list_of_strings:
                if string_to_search in line:
                    list_of_results.append((line.rstrip()))
    return list_of_results

def Open_Html_Write(cfile, strdatetime):
    cfile.write(" <html>  <head>  <meta charset='UTF-8' /> <body> \n \
        <link rel='stylesheet' type='text/css' href='css/datatables.css'> \n \
        <script type='text/javascript' src='lib/jquery-3.6.0.js'></script> \n \
        <script type='text/javascript' charset='utf8' src='lib/jquery.dataTables.min.js'></script> \n \
        <script type='text/javascript' src='lib/filter.js'></script> \n\
        <center><h1> Exemple File table </h1> <h2> " + strdatetime + "</h2> \
        </table><center><table id='example' class='display' style='width:100%'>  </td> <thead>  \
        <th> Name </th> \
        <th> position  </th> \
        <th> office   </th> \
        <th> age  </th>\
        <th> Start Day  </th> \
        <th> salary  </th> \
        </tr>  <tfoot> \n <tr> \n <th></th> \n <th></th> \n <th></th> \n <th></th> \n <th></th> \n <th></th>  \n </tr> \n\
        </tfoot> \
        </thead> <tbody>  \n ") #Html management

def Close_Html_Write(cfile):
    cfile.write(" </td> </tr> </tbody> </body> </table> </center> </head> </html> ") 

def Help():
    print("Usage: [python3] [.py]  PATH[to_all_files] and PATH[table.html]")


class ArgumentManager():

    def Check_Args(self, argv) -> int:

        """
        Check for input arguments validity.
        """

        if len(argv) != 3:
            print("ERROR - Wrong number of arguments use -h or --help")
            return 84

    def Need_Help(self, argv) -> bool:

        """
        Check if the user is asking for help.
        """

        if "-h" in argv or "--help" in argv:
            return True
        return False

def Python_Sort_File_To_Html():
    argvpath = sys.argv[1]
    argvpathexit = sys.argv[2]
    now = datetime.now()
    strdatetime = now.strftime("%d/%m/%Y, %H:%M:%S")#date pc
    cfile = open(argvpathexit+'table.html','w+') #file hmtl change name if you need other
    Open_Html_Write(cfile, strdatetime)
    for filename in glob.glob(argvpath+'*.cfg'): #open all file .txt change if you need other change .txt etc ...
        with open(os.path.join(os.getcwd(), filename), 'r') as f: 
            print(filename + " =========100%")
            ti_c = os.path.getctime(filename)
            c_ti = time.ctime(ti_c)#date file
            matcheddot1x = Take_Mul_Word(filename,['P:', 'J:','L:','M:','A:','D','#' ])
                #select the keywords in the file
            elemstr = []
            elemstr.append(matcheddot1x)#list which will group the words selected in the take_mulword function
            #print(matcheddot1x)
        for i in range(len(elemstr[0])):
            if elemstr[0][i] == '#': #allows to locate in the file
                Money = elemstr[0][i-1]
                Money = Money[3:99] #deletion of keywords (p: j: ..Etc) to display the data that we want in database.cfg
                Date = elemstr[0][i-2]#stock Date
                Date = Date[3:99]
                Age = elemstr[0][i-3]#Stock Age
                Age = Age[3:99]
                Location = elemstr[0][i-4]#Stock Location
                Location = Location[3:99]
                Jobs =elemstr[0][i-5]#Stock Jobs
                Jobs = Jobs[3:99]
                Name = elemstr[0][i-6]#Stock Name
                Name = Name[3:99]
                cfile.write(" <td>" + Name + " </td> \n <td>" +Location+ "</td> <td>" + Jobs + "</td>\n <td> "+ Age + " </td> <td> "+ Date +" </td> <td>" +Money+" </td> </tr> \n")
    Close_Html_Write(cfile)

def main():
    argsManager = ArgumentManager()
    if argsManager.Need_Help(argv):
        help()
        exit(84)
    elif argsManager.Check_Args(argv) == 84:
        exit(84)
    
    Python_Sort_File_To_Html()

if __name__ == '__main__':
    main()