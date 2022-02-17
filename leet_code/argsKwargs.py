import csv
def main():
    # 1. This code snippet asks the user for a username and deletes the user's record from file.
    updatedlis t =[]
    with open("fakefacebook.txt" ,newline="") as f:
        reade r =csv.reader(f)
        usernam e =input("Enter the username of the user you wish to remove from file:")

        for row in reader:  # for every row in the file
            if row[0 ]! =username:  # as long as the username is not in the row .......
                updatedlist.append(row)  # add each row, line by line, into a list called 'udpatedlist'
        print(updatedlist)
        updatefile(updatedlist)

def updatefile(updatedlist):
    with open("fakefacebook.txt" ,"w" ,newline="") as f:
        Write r =csv.writer(f)
        Writer.writerows(updatedlist)
        print("File has been updated")


main()


username,password,email,no_of_likes
marvR,pass123,marv@gmail.com,400
smithC,open123,cart@gmail.com,200
blogsJ,2bg123,blog@gmail.com,99

Output

test data: marvR ....would delete the entire record or row for marvR

username,password,email,no_of_likes
smithC,open123,cart@gmail.com,200
blogsJ,2bg123,blog@gmail.com,99