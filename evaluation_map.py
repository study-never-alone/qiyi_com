# -*- coding: utf-8 -*-
import os

# PERSION_NUM = 5000.
PERSION_NUM = 574.

def calculate_map(val_path, my_val_path):
    id2videos = dict()
    with open(val_path, 'rb') as fin:
        lines = fin.readlines()
        # 5000 person ids
        assert(len(lines) == PERSION_NUM)
        for line in lines:
            terms = line.strip().split(' ')
            id2videos[terms[0]] = terms[1:]

    ap_total = 0.
    with open(my_val_path, 'rb') as fin:
        lines = fin.readlines()
        # 5000 person ids
        assert(len(lines) == PERSION_NUM)
        for line in lines:
            terms = line.strip().split(' ')
            my_videos = terms[1:]
            # recall number upper bound
            assert(len(my_videos) <= 100)
            videos = id2videos[terms[0]]
            ap = 0.
            ind = 0.
            for ind_video, my_video in enumerate(my_videos):
                if my_video in videos:
                    ind += 1
                    ap += ind / (ind_video + 1)   
            ap_total += ap / len(videos)

    return ap_total / PERSION_NUM

if __name__ == '__main__': 
    # val_path = './gt_val.txt'
    # my_val_path = './my_val.txt'
    val_path = './val.txt'
    my_val_path = './val.txt'
    print 'mAP: {}'.format(calculate_map(val_path, my_val_path))
    
