import csv


def append_fail():
    with open('C:/Users/kamal/Desktop/status.csv', 'r') as file:
        failed = [f.rstrip() for f in file]  # Below two line did the same thing
        for k in range(0, len(failed)):
            if 'failed' in failed[k]:
                add_file([failed[k]])

    with open('C:/Users/kamal/Desktop/status.csv', 'r') as file:
        passed = [f.rstrip() for f in file]  # Below two line did the same thing
        for k in range(0, len(passed)):
            if 'passed' in passed[k]:
                add_file([passed[k]])


def add_file(update_file):
    with open('C:/Users/kamal/Desktop/status2.csv', "a", newline="") as write:
        writer = csv.writer(write)
        writer.writerow(update_file)
    write.close()


append_fail()
