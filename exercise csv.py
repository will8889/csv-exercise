import csv
from statistics import mean 
from statistics import median
import numpy as np
import matplotlib.pyplot as plt


#1
with open('activity.csv','r') as f:
    data = csv.reader(f)
    step_per_day = {}
    interval2 = []
    for row in data: 
         
        if not row[1] == 'date':
            if not row[0] == 'NA':
                if not row[0] == '0':
                    interval2.append(row[2])
                    if row[1] not in step_per_day:
                        step_per_day[row[1]] = [int(row[0])]
                    else:
                        step_per_day[row[1]].append(int(row[0]))
    total_step_day = {}
    data_mean={}
    data_median={}
    for key, value in step_per_day.items():   
        total_step_day[key] = sum(value)
        data_mean[key] = round(mean(value),2)
        data_median[key] = median(value)

    print(total_step_day)
    print(data_mean)
    print(data_median)

    date = tuple(total_step_day.keys())
    y = np.arange(len(step_per_day))
    totalstepperday = tuple(total_step_day.values())

    plt.bar(y, totalstepperday, align='center', alpha=0.5)
    plt.xticks(y, date)
    plt.ylabel('Total number of steps')
    plt.title('HISTOGRAM')
    plt.show()
#2  
    interval2 = tuple(interval2)
    average_per_day = (tuple(data_mean.values()))
    yz = np.arange(len(data_mean.keys()))

    plt.bar (yz, average_per_day,align='center', alpha=0.5)
    plt.title('HISTOGRAM')
    plt.xticks(y, interval2)
    plt.ylabel('steps')
    plt.show()

with open('activity.csv','r') as f:
    data = csv.reader(f)
    maximum_number = 0
    interval = {}
    for row in data:
        if row[1] != 'date':
            if row[0] != 'NA':
                if row[0] != '0':
                    if maximum_number < int(row[0]):
                        maximum_number = int(row[0])
                        interval['highest step at interval'] = int(row[2])
    print('\nMaximum Steps: ',maximum_number)
    print(interval)

#3
with open('activity.csv','r') as f:
    data = csv.reader(f)
    na_counter = {'NA':0}
    new_dataset = {}
    for row in data:
        if row[1] != "date":
            if row[0] == 'NA':
                na_counter['NA'] += 1
                if row[1] not in new_dataset:
                    new_dataset[row[1]] = [0]
                else:
                    new_dataset[row[1]].append(0)
            if row[0] != 'NA':
                if row[1] not in new_dataset:
                    new_dataset[row[1]] = [int(row[0])]
                else:
                    new_dataset[row[1]].append(int(row[0]))
    print(na_counter) 
    
    new_total_step_day = {}
    new_data_mean={}
    new_data_median={}

    for key, value in new_dataset.items():   
        new_total_step_day[key] = sum(value)
        new_data_mean[key] = round(mean(value),2)
        new_data_median[key] = median(value)
   
    # print(new_total_step_day)
    # print(new_data_mean)
    # print(new_data_median)

    date2 = tuple(new_total_step_day.keys())
    y2 = np.arange(len(new_dataset))
    totalstepperday2 = tuple(new_total_step_day.values())

    plt.bar(y2, totalstepperday2, align='center', alpha=0.5)
    plt.xticks(y2, date2)
    plt.ylabel('Total number of steps')
    plt.title('HISTOGRAM')
    plt.show()
  
#4
with open('activity.csv','r') as f:
    data = csv.reader(f)
    counter = 0
    step_per_day3 = {}
    weekday={}
    weekend={}
    for row in data:
        if row[1] != 'date':
            if row[0] == 'NA':
                if row[1] not in step_per_day3:
                    step_per_day3[row[1]] = [0]
                    counter +=1
                    if counter == 8:
                        counter = 1
                    if counter <=5 and counter > 0:
                            weekday[row[1]] = [0]
                    elif counter > 5 and counter < 8:
                            weekend[row[1]] = [0]
                else:
                    step_per_day3[row[1]].append(0)
                    if row[1] in weekday:
                            weekday[row[1]].append(0)
                    elif row[1] in weekend:
                        weekend[row[1]].append(0)

            elif row[0] != 'NA':
                    if row[1] not in step_per_day3:
                        step_per_day3[row[1]] = [int(row[0])]
                        counter +=1
                        if counter == 8:
                            counter = 1
                        if counter <=5 and counter > 0:
                            weekday[row[1]] = [int(row[0])]
                        elif counter > 5 and counter < 8:
                            weekend[row[1]] = [int(row[0])] 
                    else:
                        step_per_day3[row[1]].append(int(row[0]))
                        if row[1] in weekday:
                            weekday[row[1]].append(int(row[0]))
                        elif row[1] in weekend:
                            weekend[row[1]].append(int(row[0]))
    print('weekday: ',weekday)
    print('\nweekend: ',weekend)


             
    

