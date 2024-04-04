

image_dir = "training_files/PKLot.v2-640.yolov5pytorch/train/images/"
labels_dir = "training_files/PKLot.v2-640.yolov5pytorch/train/labels/"
from os import listdir
from os.path import isfile, join,exists
onlyfiles = [f for f in listdir(image_dir) if isfile(join(image_dir, f))]

onlyfiles.sort()
results = []
for only in onlyfiles:
    if exists(labels_dir + only.replace(".jpg","")+ ".txt" ):
        with open(labels_dir + only.replace(".jpg","") + ".txt", "r") as thisfile:
            count = 1
            for line in thisfile:
                taken = line.split(" ")[0]
                res = only.replace(".jpg","") + "#" + str(count).zfill(3) + ".jpg " + taken
                results.append(res)
                count += 1


with open("all.txt","w") as writing:
    for res in results:
        writing.write(res + "\n")

