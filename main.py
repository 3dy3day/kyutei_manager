# -*- coding: utf8 -*-
import datetime
import os
import json
import sys

file_path_h = "./Log/History.json"
file_path_o = "./Log/Ongoing.json"


shokai = False
# def resource_path(relative_path):
#     if hasattr(sys, '_MEIPASS'):
#         return os.path.join(sys._MEIPASS, relative_path)
#     return os.path.join(os.path.abspath("."), relative_path)

# file_path_h = resource_path("History.json")
# file_path_o = resource_path("Ongoing.json")

if os.path.getsize(file_path_o) > 0 and os.path.getsize(file_path_h) > 0:
    print("Current Ongoing Tasks:")
    with open(file_path_o, "r") as amat:
        with open(file_path_h, 'r') as smat:
            tmat = json.load(smat)
            cmat = json.load(amat)
            for k in range(len(cmat['Tasks'])):
                print(cmat['Tasks'][k]) 

    dmat = str(input("Is Anything Done?(y/n): "))
    if dmat == 'y':
        emat = str(input("What is the Task Name?: "))
        fmat = 0            
        for x in range(len(cmat['Tasks'])):           
            if cmat['Tasks'][x]["Task_Name"] == emat:
                with open(file_path_o, 'w+') as chk:
                    with open(file_path_h, 'w+') as air:
                        cmat['Tasks'][x]["Done"] = "True"
                        for y in range(len(tmat['Tasks'])):           
                            if tmat['Tasks'][y]["Task_Name"] == emat:
                                tmat['Tasks'][y]["Done"] = "True"

                        json.dump(cmat, air, indent=4)
                        json.dump(cmat, chk, indent=4)
                        fmat += 1
                        print("You Have Completed a Task")
                        air.close()
                        chk.close()
        if fmat != 1:
            print("No Such Task ")             

    elif dmat == 'n':
        print("\n Proceeding Next Step \n")
    else:
        print("Invalid Input")
    smat.close()
    amat.close()

elif os.path.getsize(file_path_o) == 0 or os.path.getsize(file_path_h) == 0:
    shokai = True
    seq2 = input("Do You Want to Add Task?(y/n): ")
    if seq2 == 'y':
        task_name = input("Name the Task: ")
        priority = input("What is the Priority Level?(1~5): ")
        date = str(datetime.date.today())
        done = str(False)
        primer = {}
        primer['Tasks'] = []
        primer['Tasks'].append({
                "Task_Name": task_name,
                "Priority": priority,
                "Date": date,
                "Done": done
            })
        with open(file_path_o, 'w') as outfile_a:
            json.dump(primer, outfile_a, indent=4)
            with open(file_path_h, 'w') as outfile_b:
                json.dump(primer, outfile_b, indent=4)

    elif seq2 == 'n':
        print("\n Proceeding Next Step \n")
    else:
        print("Invalid Input")



if shokai == False:
    tasu2 = input("Do You Want to Add Task?(y/n): ")
    if tasu2 == 'y':
        poly = {}
        with open(file_path_o, "r") as azmat:
            poly = json.load(azmat)

        task_name = input("Name the Task: ")
        priority = input("What is the Priority Level?(1~5): ")
        date = str(datetime.date.today())
        done = str(False)

        poly["Tasks"].append({
                "Task_Name": task_name,
                "Priority": priority,
                "Date": date,
                "Done": done
        })
        with open(file_path_o,'w+') as bmat:          
            json.dump(poly, bmat, indent=4)
        with open(file_path_h, 'w+') as bamat:
            json.dump(poly, bamat, indent=4)
        bamat.close()
        bmat.close()
        azmat.close()

    elif tasu2 == 'n':
        print("\n Proceeding Next Step \n")
    else:
        print("Invalid Input")

if os.path.getsize(file_path_h) != 0:
    tasu3 = input("Do You Want to View History?(y/n): ")
    if tasu3 == 'y':
        with open(file_path_h, "r") as hismat:
            history = json.load(hismat)
        for p in range(len(history['Tasks'])):
            print(history['Tasks'][p])
        hismat.close()

    elif tasu3 == 'n':
        print("\n Proceeding Next Step \n")
    else:
        print("Invalid Input")

if os.path.getsize(file_path_o) != 0:
    with open(file_path_o, "r") as bbmat:
        ccmat = json.load(bbmat)
    for z in range(len(ccmat['Tasks']) - 1):
        if ccmat['Tasks'][z]["Done"] == "True":
            with open(file_path_o, 'w+') as las:
                del ccmat['Tasks'][z]
                json.dump(ccmat, las, indent=4)
                las.close()
    bbmat.close()

input("Press Enter to Exit :")