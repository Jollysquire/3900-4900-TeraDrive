from ast import arg
import os
import sys
import datetime
import argparse
from pathlib import Path
import logging
from os.path import getsize
from hex import CheckFile


# Constant Variables
APP_NAME = "File Recovery"
GEN_DATE = datetime.datetime.now().strftime("%d/%m/%Y")
GEN_TIME = datetime.datetime.now().strftime("%H:%M")
APP_LINK = "https://github.com/Jollysquire/3900-4900-TeraDrive"

# global variable
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
    title,
    AppLink,
    NumFiles,
    NumDirs,
    GrandTotalSize,
    LinkFiles,
):
    templateFile = open((Path(__file__).parent / 'template.html'), 'r')
    outputFile = open(f'{title}.html', 'w', encoding="utf-8")
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
    arggparser = argparse.ArgumentParser()
    arggparser.add_argument(
        "-d",
        "--dir",
        help="The directory to be scanned.",
        required=True,
    )
    arggparser.add_argument(
        "-t",
        "--title",
        help="The title of the HTML file.",
        required=True,
    )
    arggparser.add_argument(
        "-l",
        "--link",
        help="The link to the directory to be scanned.",
        required=True,
    )
    arggparser.add_argument(
        "-v",
        "--verbose",
        help="Verbose output.",
        action="store_true",
    )
   
    
    args = arggparser.parse_args()
    pathToIndex = args.path
    title = args.title
    linkFiles = args.linkfiles
    if os.path.exists(pathToIndex):  # check if the specified directory exists
        DirToArray(pathToIndex)
        make_HTML(
            DirData,
            APP_NAME,
            GEN_DATE,
            GEN_TIME,
            title,
            APP_LINK,
            NumFiles,
            NumDirs,
            GrandTotalSize,
            LinkFiles=str(linkFiles).lower(),
        )
    else:
        print("The specified directory doesn't exist")


if __name__ == "__main__":
    main()


"""

    logging.debug("Starting...")
    logging.debug("Scanning directory: " + args.dir)
    logging.debug("Title: " + args.title)
    logging.debug("Link: " + args.link)

    # get current date and time
    GenDate = datetime.datetime.now().strftime("%d/%m/%Y")
    GenTime = datetime.datetime.now().strftime("%H:%M:%S")
"""