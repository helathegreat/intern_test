txt_file = "C:/Users/17717/Desktop/tc3410.txt"

list_important = {
    "MotionMeasurement": 3,
    "BreathDetected": 3
}
## 3-4 是最关键的
## 首先要计算某一个activity中的开始时间--sra 决定的 按照第一个sra的提前2000个时钟周期作为开始时间，结束时间则按照计数计算（12个），最后一个的侯半个T就是aperature的技术时间
## 计算在这个aperature中有效的呼吸个数
## 计算时间差

## 要用队列维护
import queue
time_queue = queue.Queue()
flag = True
time_stamp = []
time_line = []
with open(txt_file,"r") as file:
    for line in file:
        l_split = line.split("|")
        if(l_split[3] in ("MotionMeasurement","BreathDetected")):
            time_stamp.append(l_split[4])
            if flag and l_split[3] == "MotionMeasurement":
                judge = [ele for ele in time_stamp if ele < (l_split - 2000)]
                if len(judge) == 0:
                    # 为空则说明存在的，因此这个activity就可以开始了
                    filter_list = []
                    filter_list.appned(l_split - 2000)
                    for ele in time_stamp:
                        if ele > (l_split - 2000):
                            filter_list.append(ele)
                else:
                    # 这个activity 不可以 要去除





            if(l_split[3] == "MotionMeasurement"):
                ## 对头的抛弃
                if(head < (l_split[4] - 2000)):
                    time_stamp.append(l_split[4] - 2000)



                ## 中间的计算

                print(l_split[4])

            if(l_split[3] == "BreathDetected"):
                print(l_split[4])



