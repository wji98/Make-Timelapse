# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 01:11:30 2020

@author: xy
"""

#imports
import os
import moviepy.editor as mp 

#parameters
direc = 'E:\\June14\\' #where your videos are located
freq = 4 #make a timelapse with every nth video
min_duration = 300 #minimum length of video you want included in timelapse
new_size = 0.7 #scaling factor, note quality is reduced by factor of n^2, so 0.5 -> 25% resolution
new_fps = 15 #fps of your timelapse
speed = 20 #how much you want the video to be sped up

#dummy variables
file_no = 0
clip_list = []
for filename in os.listdir(direc):
    if file_no % freq != 0: #every nth video
        file_no += 1
        continue
		
    temp_clip = mp.VideoFileClip(direc+filename) #get clip
    if not temp_clip or temp_clip.duration<min_duration: #if video can't be opened or too short
        continue
	
	#process clip
    temp_clip = temp_clip.resize(new_size)
    #temp_clip = temp_clip.set_fps(new_fps)
    temp_clip = temp_clip.without_audio()
    temp_clip = temp_clip.speedx(factor=speed)
    clip_list.append(temp_clip)
	
    file_no += 1

final_clip = mp.concatenate_videoclips(clip_list) #stitch clip together
final_clip.write_videofile(direc + "timelapse.mp4") #write to file this step takes the longest