import csv


def append_fail():
    count = 0
    update_file = []
    with open('C:/Users/kamal/Desktop/status.csv', 'r') as file:
        f = [f.rstrip() for f in file]  # Below two line did the same thing
        for k in range(0, len(f)):
            if 'failed' in f[k]:
                """""with open('C:/Users/kamal/Desktop/status2.csv', "a", newline="") as write:
                    writer = csv.writer(write)
                    writer.writerow([f[k]])
                write.close()"""""
                count = count + 1
                update_file = [f[k]]
                add_file(update_file)
                # print(f[k])
        print(count)
        #print(update_file)

    with open('C:/Users/kamal/Desktop/status.csv', 'r') as file:
        f = [f.rstrip() for f in file]  # Below two line did the same thing
        for k in range(0, len(f)):
            if 'passed' in f[k]:
                count = count + 1
                update_file = [f[k]]
                add_file(update_file)
                # print(f[k])
        print(count)


def add_file(update_file):
    with open('C:/Users/kamal/Desktop/status2.csv', "a", newline="") as write:
        writer = csv.writer(write)
        writer.writerow(update_file)
    write.close()


append_fail()
