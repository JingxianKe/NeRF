# import the necessary packages
import json
import numpy as np

# define the json training file
jsonTrainFile = "transforms_train.json"

# open the file and read the contents of the file
with open(jsonTrainFile, "r") as fp:
    jsonTrainData = json.load(fp)

# print the content of the json file
print(f"[INFO] Focal length train: {jsonTrainData['camera_angle_x']}")
print(f"[INFO] Number of frames train: {len(jsonTrainData['frames'])}")

# OUTPUT
# [INFO] Focal length train: 0.6911112070083618
# [INFO] Number of frames train: 100

# grab the first frame
firstFrame = jsonTrainData["frames"][0]

# grab the transform matrix and file name
tMat = np.array(firstFrame["transform_matrix"])
fName = firstFrame["file_path"]

# print the data
print(tMat)
print(fName)

# OUTPUT
# array([[-0.92501402,  0.27488998, -0.26226836, -1.05723763],
#       [-0.37993318, -0.66926789,  0.63853836,  2.5740304 ],
#       [ 0.        ,  0.6903013 ,  0.72352195,  2.91661024],
#       [ 0.        ,  0.        ,  0.        ,  1.        ]])
# ./train/r_0