# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 14:36:46 2019

@author: RTV-3
"""


#n_path ="\\\\192.168.1.100\\员工重要文件共享\\中新社\\1022"
n_path ="C:\\Users\\RTV-3\\Downloads\\1023"
import subprocess
import os
from datetime import timedelta




def cut_video(video_pathand_name,file_number):
    #file_path = os.path.join(n_path,files[0])
    print(video_pathand_name)
    log_f = open('temp_duration00.txt','w')
    subprocess.call(['ffprobe','-show_format',file_path],stdout=log_f)
    log_f.close()
    
    #tail is 8 seconds long
    #video_tail_long="Sat Mar 28 " + "00:00:07" + " 2019"
    #tail_t = time.mktime(time.strptime(video_tail_long,"%a %b %d %H:%M:%S %Y"))
    # get duration of video
    try:
        with open('temp_duration00.txt','r',encoding='UTF-8') as f:
            try:
                line = f.readline()
                while line :
                    if "duration" in line:
                        dr=float(line[9:])-8.0
                        print(float(line[9:])-8.0)
                        end_time = str(timedelta(seconds=dr))
                        print(end_time)
                        subprocess.Popen(['ffmpeg.exe','-ss','00:00:00', '-t',
                                          end_time, '-i',file_path,
                                          '-vcodec', 'copy', '-acodec' ,'copy',
                                          file_number])
                        break
                    else:
                        line = f.readline()
            except IOError as err:
                print("File Error:"+str(err)) 
           
    except IOError as err:
        print("File Error:"+str(err))
    log_f.close()


files= os.listdir(n_path)
   


i=0
for file in files:
    file_path = os.path.join(n_path,file)
    file_number= 'output\\'+str(i)+".mp4"
    cut_video(file_path,file_number)
    i+=1





