from os import system
from os import listdir, remove
from os.path import isdir, abspath

import csv

inputDir = raw_input('Input directory: ')
outputDir = raw_input('Output directory: ')
summaryFile = raw_input('Summary file: ')
keepTempFiles = raw_input('Keep temp files [yes/no] ')

files = listdir(inputDir)

for f in files:
  s = inputDir + '/' + f 
  if(isdir(s)):
    system('cloc ' + s + ' --csv --out=' + outputDir + "/" + f + ".csv")

files = [f for f in listdir(outputDir) if f.endswith(".csv")]

fout = file(summaryFile, "w")  
  
for f in files:
  fname = outputDir + f 
  aFile = file(fname, "rt")
  reader = csv.reader(aFile)
  count = 0
  cpp   = 0
  other = 0
  for row in reader:
    if(count == 0): 
      row.insert(0, 'project')
    else: 
     if(row[1] == "C++" or row[1].startswith("C/C++")):
       cpp += int(row[4])
     else: 
       other += int(row[4])
     row.insert(0, f)
    count += 1
  
  writer = csv.writer(fout)
  writer.writerow((f, cpp, other))
  aFile.close()
   
  if(keepTempFiles == 'no'): 
    remove(fname)

fout.close()
