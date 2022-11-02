from ast import arg
import os
import sys
import datetime
import argparse
from pathlib import Path
import logging
from os.path import getsize
from hex import CheckFile
import time
import PySimpleGUI as sg 

# Constant Variables
APP_NAME = "File Recovery"
GEN_DATE = datetime.datetime.now().strftime("%d/%m/%Y")
GEN_TIME = datetime.datetime.now().strftime("%H:%M")
APP_LINK = "https://github.com/Jollysquire/3900-4900-TeraDrive"

# global variables
DirData = ""
NumFiles = 0
NumDirs = 0
GrandTotalSize = 0


# functions definition
def DirToArray(ScanDir):
    global DirData
    global NumFiles
    global NumDirs
    global GrandTotalSize
    
    # assing a number identifier to each directory
    i = 1
    dirIDsDictionary = {}
    dirIDsDictionary[ScanDir] = 0
    for currentDir, dirs, files in os.walk(ScanDir):
        for dir in dirs:
            pathDir = os.path.join(currentDir, dir)

            dirIDsDictionary[pathDir] = i  # HERE

            i = i + 1

    # initilize array to hold all dir data, dimensioning it to hold the total number of dirs
    fullDirArr = []
    for p in range(i):
        fullDirArr.append(p)

    # traverse the directory tree
    for currentDir, dirs, files in os.walk(ScanDir):
       

        currentDirId = dirIDsDictionary[currentDir]
        currentDirArray = []  # array to hold all current dir data
        currentDirModifiedTime = datetime.datetime.fromtimestamp(
            os.path.getmtime(currentDir)
        )
        currentDirModifiedTime = currentDirModifiedTime.strftime("%d/%m/%Y %H:%M:%S")
        currentDirFixed = currentDir.replace(
            "\\", "\\\\"
        )  # replace / with \\ in the dir path (necessary for javascript functions to work properly

        currentDirArray.append(
            currentDirFixed + "*0*" + currentDirModifiedTime
        )  # append directory info to currentDirArray

        totalSize = 0
        for file in files:
            #if os.path.isfile(file):
                NumFiles = NumFiles + 1
                fileSize = getsize(currentDir + "/" + file)
                totalSize = totalSize + fileSize
                GrandTotalSize = GrandTotalSize + fileSize
                fileModifiedTime = datetime.datetime.fromtimestamp(
                    #os.path.getmtime(currentDir + "/" + file)
                    os.path.getmtime(os.path.join(currentDir, file))
                )
                fileModifiedTime = fileModifiedTime.strftime("%d/%m/%Y %H:%M:%S")

                # Check the file if its corrupted or not
                #file = os.path.join(currentDir, file)
                checkFile = CheckFile()
                getHex, getType = checkFile.get_hex(os.path.join(currentDir, file))
                status = checkFile.check_data(getHex, getType)
                status = str(status)
                currentDirArray.append(
                    file + "*" + str(fileSize) + "*" + fileModifiedTime + "*" + status
                ) 

                

        currentDirArray.append(totalSize)  # append total file size to currentDirArray
        # create the list of directory IDs correspondent to the subdirs present on the current directory
        # this acts as a list of links to the subdirectories on the javascript code
        dirLinks = ""
        for dir in dirs:
            NumDirs = NumDirs + 1
            pathChild = os.path.join(currentDir, dir)
            dirLinks = dirLinks + str(dirIDsDictionary[pathChild]) + "*"
        dirLinks = dirLinks[:-1]  # remove last *
        currentDirArray.append(dirLinks)
        fullDirArr[
            currentDirId
        ] = currentDirArray  # store currentDirArray on the correspondent position of fullDIrArr
    list_data = []
    for d in range(len(fullDirArr)):
        list_data.append("dirs[" + str(d) + "] = [\n")
        for g in range(len(fullDirArr[d])):
            if type(fullDirArr[d][g]) == int:
                list_data.append(str(fullDirArr[d][g]) + ",\n")
            else:
                list_data.append('"' + fullDirArr[d][g] + '",\n')
        list_data.append("];\n")
        list_data.append("\n")
    DirData += "".join(list_data)

    return


def make_HTML(
    DirData,
    AppName,
    GenDate,
    GenTime,
    outputPath,
    AppLink,
    NumFiles,
    NumDirs,
    GrandTotalSize,
    LinkFiles,
):
    title = ("test")
    templateFile = open((Path(__file__).parent / 'template.html'), 'r')
    outputFile = open(f'{os.path.join(outputPath, title)}.html', 'w', encoding="utf-8")
    for line in templateFile:
        modifiedLine = line
        modifiedLine = modifiedLine.replace("[DIR DATA]", DirData)
        modifiedLine = modifiedLine.replace("[APP NAME]", AppName)
        modifiedLine = modifiedLine.replace("[GEN DATE]", GenDate)
        modifiedLine = modifiedLine.replace("[GEN TIME]", GenTime)
        modifiedLine = modifiedLine.replace("[TITLE]", title)
        modifiedLine = modifiedLine.replace("[APP LINK]", AppLink)
        modifiedLine = modifiedLine.replace("[NUM FILES]", str(NumFiles))
        modifiedLine = modifiedLine.replace("[NUM DIRS]", str(NumDirs))
        modifiedLine = modifiedLine.replace("[TOT SIZE]", str(GrandTotalSize))
        modifiedLine = modifiedLine.replace("[LINK FILES]", LinkFiles)
        outputFile.write(modifiedLine)
    templateFile.close()
    outputFile.close()
    logging.warning("Wrote output to: " + os.path.realpath(outputFile.name))

def main():
    # ------ Menu Definition ------ #
    menu_def = [['Toolbar', ['About', 'Help']]]


    # ------ GUI Definition ------ #
    layout = [[sg.MenubarCustom(menu_def, tearoff=False)],
              [sg.T("Input Folder:", s=15, justification="r"), sg.I(key="-IN-"), sg.FolderBrowse()],
              [sg.T("Output Folder:", s=15, justification="r"), sg.I(key="-OUT-"), sg.FolderBrowse()],
              [sg.Exit(s=16, button_color="tomato"), sg.B("Start", s=16)]]
    
    window = sg.Window('Snap2Check', layout, use_custom_titlebar=True)
    while True:
        event, values = window.read()
        pathToIndex = values['-IN-'] 
        outputPath = values['-OUT-']
        if event in (sg.WINDOW_CLOSED, "Exit"):
            break
        if event == "About":
            window.disappear()
            sg.popup('About Snap2Check', "Version 1.0", "Used to scan file integrity and" \
            " return HTML with results", grab_anywhere=True)
            window.reappear()
        if event == "Help":
            window.disappear()
            sg.popup('How to use Snap2Check', "Select the directory of files you wish to verify" \
            " and an output directory for the HTML file generated", grab_anywhere=True)
            window.reappear()
        if event == "Start":
            if os.path.exists(pathToIndex) and os.path.exists(outputPath):  # check if the specified directory exists
                DirToArray(pathToIndex)
                make_HTML(
                    DirData,
                    APP_NAME,
                    GEN_DATE,
                    GEN_TIME,
                    outputPath,
                    APP_LINK,
                    NumFiles,
                    NumDirs,
                    GrandTotalSize,
                    LinkFiles="",
                    )
            else:
                sg.popup_error("Error", "One or both of the specified directories don't exist")

    window.close()



    
if __name__ == "__main__":
    main()


