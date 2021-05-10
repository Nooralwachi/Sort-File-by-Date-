from datetime import datetime
def sort_bydate(filename):
    files=[]
    with open (filename, 'r') as file:
        for line in file:
            item = line.split()
            date=(' '.join(item[2:5]))
            file_date= datetime.strptime(date, "%B %d, %Y")
            name = item[-1]
            files.append([name,file_date])
        sorted_files= sorted(files, key=lambda x:x[1], reverse = True)
    for name, date_obj in sorted_files:
        print(f'{name}, {date_obj.strftime("%B %d, %Y")}')

sort_bydate("file_sortbydate.txt")