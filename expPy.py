

import re,os

video_name = "IQIYI_VID_TRAIN_00005570.mp4"
file , extension = os.path.splitext(video_name)
print file
print extension
totalCount = re.sub("\D", "", file)
totalCount = int(totalCount)
print totalCount
if totalCount > 5570:
    print "{} is bigger".format(totalCount)
else:
    print "{} is small".format(totalCount)