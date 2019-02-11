# lab 5: GUI and Threads
# Wanjing Zhang, Yuxi Yu

import os
import os.path
# from collections import defaultdict
import re
from strsearch import strIsInFile
import time

class FileSearch():
    
     #A constructor that accepts a start directory, recursively walk down all subdirectories 
     #of the start directory, and caches the absolute paths of all files in a dictionary
    def __init__(self, directory):
        self.files = []
        for (directory, dirtList, fileList) in os.walk(directory):
            for file in fileList: 
                self.files.append(tuple((os.path.join(directory, file), file)))
        # self._fileDict = defaultdict(list)
        #for (path, dirlist, filelist) in os.walk(directory) :
            #for file in filelist :
                #self._fileDict[file].append(os.path.realpath(os.path.join(path,file)))       # create FileSearch object so files can be stored in the dictionary
    
    
    # A searchName method that accepts a regular expression as a filter, searches through 
    # the dictionary for all file names that match the filter, and returns the corresponding 
    # paths in a sorted list
    def searchName(self, regex, searchString, listOfResults):
        for filesTuple in self.files:
            if re.search(regex, filesTuple[1]):
                if strIsInFile(searchString, filesTuple[0]) or len(searchString) == 0 : 
                    listOfResults.append(filesTuple)
                    time.sleep(0.5)
        listOfResults.sort(key=lambda fTup: fTup[0])
        
        #fileList = []
        #for item in self._fileDict:
            #if re.search(regex, item, re.I):
                #fileList.extend(self._fileDict[item])
        #return sorted(fileList)
