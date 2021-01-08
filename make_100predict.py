import os

genename_array = os.listdir("sorted_gfa_files/")

f = open("100predict.sh", "w")

for genename in genename_array:

    f.write("python gfa_test.py sorted_gfa_files/" + genename + " 0.99 1000\n")
    f.flush()

f.close()