import os
import sys

current_directory = os.path.dirname(os.path.abspath(__file__))

if os.name == "nt":
    splitter = '\\'
else:
    splitter = "/"
	
script_name = sys.executable.split(splitter)[-1]
print script_name
if not os.path.isdir(os.path.join(current_directory, "RESULT")):
    os.makedirs(os.path.join(current_directory, "RESULT"))

for d, dirs, files in os.walk(current_directory):
    if d.split(splitter)[-1] != "RESULT":
        for f in files:
            if f != script_name:
                f2 = f
                if os.path.isfile(os.path.join(current_directory, "RESULT", f2)):
                    c = 0
                    while os.path.isfile(os.path.join(current_directory, "RESULT", f2)):
                        c += 1
                        f2 = "%s_%s" % (c, f)
                os.rename(os.path.join(d,f), os.path.join(current_directory, "RESULT", f2))
                print "Moving %s -> %s" % (os.path.join(d,f), os.path.join(current_directory, "RESULT", f2))
