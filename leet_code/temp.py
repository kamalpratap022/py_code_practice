import csv

import pandas as pd

count=0
with open('C:/Users/kamal/Desktop/status.csv', 'r') as file:
    f=[f.rstrip() for f in file] # Below two line did the same thing
    #f1 = file.readlines()
    #f2 = [x.strip() for x in f1]
    #print(len(f)+1)
    for k in range(0,len(f)):
        if 'failed' in f[k]:
            with open('C:/Users/kamal/Desktop/status.csv',"a",newline="") as write:
                writer = csv.writer(write)
                writer.writerow([f[k]])
            write.close()
            count = count + 1;
            #print(f[k])
    print(count)


# Replace the target string
#filedata = filedata.replace('mail.smtp.host="localhost"', 'mail.smtp.host="smtp.gmail.com"')
""""df = pd.read_csv("C:/Users/kamal/Desktop/status1.csv")
//dept_emp_num =  df.groupby('Status')['Status'].count()
//print(dept_emp_num)"""""

"""""df = pd.read_csv("C:/Users/kamal/Desktop/status.csv", header = None)
print(df)"""""
"""""import csv

with open('C:/Users/kamal/Desktop/status.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=';')
    for row in readCSV:
        print(row[2])"""""