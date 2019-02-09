# Data-Analysis-Code
Python Code for Chattering Alarm


This is the code for the Chattering Alarm detecting process. Two dictionaries were used to store the time tag of different Alarm tags, as well as the amount of each Alarm tags. The purpose is to calculate the time difference between the third alarm and first alarm with the same tag. Also, the amount of each Alarm tag can assist determining if the third alarm with specific tag is reached when the algorithm runs. The standard for the chattering alarm used here is if we have equal to or more than three alarms with the same tag happening within one minute. This is the reason this algorithm tracks three alarms and calculate the time difference between the third alarm and the first alarm. 



The result is presented in a dynamic scatter plot. The "def" plot part in the code is used to finish the job. The function is called multiple times. When the plot is created, the result is first converted into either "0" for "Not a Chattering Alarm", and "1" for "Chattering Alarm". This way the result can be presented in the dynamic scatter plot. The y-axis label is then changed into the readable result, "Not a Chattering Alarm" and "Chattering Alarm". The x-axis labels are changed into time tag with the alarm tag. However, the determination step in the algorithm still uses only the alarm tag to make sure the results are accurate.
