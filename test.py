import os
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure(num=None, figsize=(25, 15), dpi=80, facecolor='c', edgecolor='k') 
ax1 = fig.add_subplot(111, axisbg = "black")
x = [] 
y_all = [] 
y_cover = [] 

def animate(frame_num):
    x.append(frame_num)
    all_steps = [] 
    normal_steps = []	
    for line in open("lfitanim.csv"): 
        step = line.split(',')[11]
        if step == '':
            step = 0
        step = int(step)
        all_steps.append(step)
        if step > 4000 and step < 15000: 
            normal_steps.append(step) 
        else:
            normal_steps.append(0)
        #print normal_steps 
    y_all.append(all_steps[frame_num]) 
    y_cover.append(normal_steps[frame_num]) 
    ax1.clear() 
    ax1.plot(x, y_all, 'g') 
    ax1.plot(x, y_all, 'ro')
    ax1.plot(x, y_cover, 'wo')
    plt.savefig('video/%03d' %len(x)) 

ani = animation.FuncAnimation(fig, animate, interval=1) 
#os.system("ffmpeg -start_number 1 -i video/%03d.png output.mp4") 
plt.show() 
