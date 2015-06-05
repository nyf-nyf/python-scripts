# -*- coding: utf-8 -*-
import Image
import os
import sys
ll = ["jpeg", "jpg", "gif", "png", "tif"] # File extensions to get as an image

size = (480, 480) # Size of image: width, height
dirs = ["."] # Directories to scan. Default is directory where the script file is
color = True # Save images in color or grayscale


count = 1
for walk_dir in dirs:
    for root, subFolders, files in os.walk(walk_dir):
        for f in files:
            ff = f.split(".")
            if str(ff[len(ff)-1]).lower() not in ll:
                continue
            d = "../resized/" + root[2:]
            out = d + "/" + str(count) + ".jpg"
            cur = root + "/" + f
            if os.path.isdir(d) is False:
                os.makedirs(d)
            try:
                i = Image.open(cur, "r")
                #if i.size[0] < i.size[1]:
                    #i = i.rotate(90)	
                if i.size[0] < size[0] or i.size[1] < size[1]:
                    continue
                if i.size[0] >= i.size[1]:
                    ratio = float(i.size[0])/float(i.size[1])
                else:
                    ratio = float(i.size[1])/float(i.size[0])
                t_size = (int(size[0]*ratio), int(size[1]*ratio))
                if i.size[0] > size[0] or i.size[1] > size[1]:
                    i.thumbnail(t_size, Image.ANTIALIAS)
                ic = i.crop(((i.size[0]-size[0])/2, (i.size[1]-size[1])/2, (i.size[0]-size[0])/2+size[0], (i.size[1]-size[1])/2+size[1]))
		if color is False:
		    ic = ic.convert("L")                
		ic.save(out, "JPEG")
                print "Saving %s" % out
            except IOError:
                print "Error saving '%s'" % out
            count += 1
