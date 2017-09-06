import glob
#import os
#import csv
import pandas as pd
import matplotlib.pyplot as plt
import os.path

def find_rows_to_read(datalist):
    #print(len(datalist))
    find_small=[]
    for i in range(0,len(datalist)):
        find_small.append(datalist[i][0])
    return(min(find_small))

def makedf(csvfile_cloth, no_of_files):
    cloth_list=[]
    for file_ in csvfile_cloth:
        cloth_ = pd.read_csv(file_, index_col=None, header=None)
        cloth_list.append(cloth_.shape)
    rows_to_read = find_rows_to_read(cloth_list)
    print("rows to read are ",rows_to_read)
    cloth_list = []
    for file_ in csvfile_cloth:
        cloth_ = pd.read_csv(file_, index_col=None, header=None, nrows=rows_to_read)
        cloth_list.append(cloth_)
    cloth_sum = cloth_list[0]
    ylen = len(cloth_sum)
    xlen = 3
    
    for i in range(1,len(cloth_list)):
        for x in range(0, xlen):
            for y in range(0, ylen):
                cloth_sum[x][y] = cloth_sum[x][y]+cloth_list[i][x][y]

    cloth_avg=cloth_sum
    for x in range(0, xlen):
        for y in range(0, ylen):
            cloth_avg[x][y] = cloth_sum[x][y]/no_of_files

    cloth_frame = pd.DataFrame(cloth_avg)
    print(cloth_frame.shape)
    return(cloth_frame)
    
def clipframe(fr1, fr2, fr3, fr4):
    s1 = fr1.shape
    s2 = fr2.shape
    s3 = fr3.shape
    s4 = fr4.shape
    #print(s1[0], s2[0], s3[0], s4[0])
    return(min(s1[0], s2[0], s3[0], s4[0]))
    
    
path = "D:\Cloth simulations blender\cloth sphere sim\simulation9\forceapplied"
print(os.path.exists(path))
csvfile_cotton = glob.glob(path + "\\cotton*.csv")
csvfile_denim = glob.glob(path + "\\denim*.csv")
csvfile_leather = glob.glob(path + "\\leather*.csv")
csvfile_silk = glob.glob(path + "\\silk*.csv")

no_of_cotton = len(glob.glob(path + "\\cotton*.csv"))
no_of_denim = len(glob.glob(path + "\\denim*.csv"))
no_of_leather = len(glob.glob(path + "\\leather*.csv"))
no_of_silk = len(glob.glob(path + "\\silk*.csv"))

cotton_frame = pd.DataFrame()
denim_frame = pd.DataFrame()
leather_frame = pd.DataFrame()
silk_frame = pd.DataFrame()

cotton_frame = makedf(csvfile_cotton, no_of_cotton)
denim_frame = makedf(csvfile_denim, no_of_denim)
leather_frame = makedf(csvfile_leather, no_of_leather)
silk_frame = makedf(csvfile_silk, no_of_silk)

clip_value = clipframe(cotton_frame, denim_frame, leather_frame, silk_frame)

cotton_frame = cotton_frame.drop(cotton_frame.index[clip_value+1:])
denim_frame = denim_frame.drop(denim_frame.index[clip_value+1:])
leather_frame = leather_frame.drop(leather_frame.index[clip_value+1:])
silk_frame = silk_frame.drop(silk_frame.index[clip_value+1:])

csvfile_cotton_no = glob.glob(path + "\\noballcotton*.csv")
csvfile_denim_no = glob.glob(path + "\\noballdenim*.csv")
csvfile_leather_no = glob.glob(path + "\\noballleather*.csv")
csvfile_silk_no = glob.glob(path + "\\noballsilk*.csv")

no_of_cotton_no = len(glob.glob(path + "\\noballcotton*.csv"))
no_of_denim_no = len(glob.glob(path + "\\noballdenim*.csv"))
no_of_leather_no = len(glob.glob(path + "\\noballleather*.csv"))
no_of_silk_no = len(glob.glob(path + "\\noballsilk*.csv"))

cotton_frame_no = pd.DataFrame()
denim_frame_no = pd.DataFrame()
leather_frame_no = pd.DataFrame()
silk_frame_no = pd.DataFrame()

cotton_frame_no = makedf(csvfile_cotton_no, no_of_cotton_no)
denim_frame_no = makedf(csvfile_denim_no, no_of_denim_no)
leather_frame_no = makedf(csvfile_leather_no, no_of_leather_no)
silk_frame_no = makedf(csvfile_silk_no, no_of_silk_no)

clip_value_no = clipframe(cotton_frame_no, denim_frame_no, leather_frame_no, silk_frame_no)

cotton_frame_no = cotton_frame_no.drop(cotton_frame_no.index[clip_value_no+1:])
denim_frame_no = denim_frame_no.drop(denim_frame_no.index[clip_value_no+1:])
leather_frame_no = leather_frame_no.drop(leather_frame_no.index[clip_value_no+1:])
silk_frame_no = silk_frame_no.drop(silk_frame_no.index[clip_value_no+1:])

csvfile_nocloth = glob.glob(path + "\\nocloth*.csv")

no_of_nocloth = len(glob.glob(path + "\\nocloth*.csv"))

no_cloth_frame = pd.DataFrame()

no_cloth_frame = makedf(csvfile_nocloth, no_of_nocloth)
#print(no_cloth_frame)

fig = plt.figure()
ax1 = fig.add_subplot(321)
ax1.plot(cotton_frame.iloc[:,0:1], label='Cotton')
ax1.plot(denim_frame.iloc[:,0:1], label='Denim')
ax1.plot(leather_frame.iloc[:,0:1], label='Leather')
ax1.plot(silk_frame.iloc[:,0:1], label='Silk')
ax1.set_xlabel('Frames')
ax1.set_ylabel('Force')
ax1.set_title('Force variation with types of cloth')
ax1.legend(loc="lower right")

ax2 = fig.add_subplot(322)
ax2.plot(cotton_frame.iloc[:,1:2], label='Cotton')
ax2.plot(denim_frame.iloc[:,1:2], label='Denim')
ax2.plot(leather_frame.iloc[:,1:2], label='Leather')
ax2.plot(silk_frame.iloc[:,1:2], label='Silk')
ax2.set_xlabel('frames')
ax2.set_ylabel('Velocity')
ax2.set_title('Velocity variation with types of cloth')
ax2.legend(loc="upper right")

ax3 = fig.add_subplot(323)
ax3.plot(cotton_frame_no.iloc[:,0:1], label='Cotton')
ax3.plot(denim_frame_no.iloc[:,0:1], label='Denim')
ax3.plot(leather_frame_no.iloc[:,0:1], label='Leather')
ax3.plot(silk_frame_no.iloc[:,0:1], label='Silk')
ax3.set_xlabel('Frames')
ax3.set_ylabel('Force')
ax3.set_title('Force variation with no ball')
ax3.legend(loc="lower right")

ax4 = fig.add_subplot(324)
ax4.plot(cotton_frame_no.iloc[:,1:2], label='Cotton')
ax4.plot(denim_frame_no.iloc[:,1:2], label='Denim')
ax4.plot(leather_frame_no.iloc[:,1:2], label='Leather')
ax4.plot(silk_frame_no.iloc[:,1:2], label='Silk')
ax4.set_xlabel('frames')
ax4.set_ylabel('Velocity')
ax4.set_title('Velocity variation with no ball')
ax4.legend(loc="upper right")

ax5 = fig.add_subplot(325)
ax5.plot(no_cloth_frame.iloc[:,0:1], label='No cloth')
ax5.set_xlabel('frames')
ax5.set_ylabel('Force')
ax5.set_title('Force on grippers with no cloth')
ax5.legend(loc="upper right")

ax6 = fig.add_subplot(326)
ax6.plot(no_cloth_frame.iloc[:,1:2], label='No cloth')
ax6.set_xlabel('frames')
ax6.set_ylabel('Velocity')
ax6.set_title('Velocity of grippers with no cloth')
ax6.legend(loc="upper right")
plt.show()