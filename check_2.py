import csv
import statistics
## 还要写成csv file
csv_list = []
csv_file_path = "./check_day_3.csv"
txt_file = "C:/Users/17717/Desktop/day_3.txt"
bpm_list = []
pre = 0
now = 0
with open(txt_file,"r") as file:
    for line in file:
        file_list = []
        l_split = line.split("|")
        #print(l_split)
        if(l_split[3] == "MotionMeasurement"or l_split[3] == "start" or l_split[3] == "end"):
            if(l_split[3] == "start" or l_split[3] == "end"):
                file_list = ["start/end",l_split[4]]
                csv_list.append(file_list)
                pre = (int)(l_split[4])
            continue
        else:
            file_list = [l_split[3],l_split[4]]
            now = (int)(l_split[4])

        bpm_list.append(60*4000/(2.5*(now - pre)))
        #print(str(pre) + "+" + str(now))
        print(60*4000/(2.5*(now - pre)))
        file_list.append(60*4000/(2.5*(now - pre)))
        pre = now
        csv_list.append(file_list)


print(len(bpm_list))


median_value = statistics.median(bpm_list)
print(median_value)


with open(csv_file_path,'w',newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(csv_list)





