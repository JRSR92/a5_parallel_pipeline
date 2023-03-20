import json
import os
import pathlib

root_folder = pathlib.Path(__file__).parent.resolve() # finds current working directory

files = os.listdir(root_folder)

files_set = set(())

file_dictionary = {}

for root, dirs, files in os.walk(root_folder):
    for file in files:
        if file.endswith(".fastq.gz"):
            run_names = file.split('.')[0]  # this is the r1 and r2 run names
            run_name_generic = run_names.split("_") # this is the generic name for that run
            path = os.path.join(root)
            files_set.add(f"{path}/{run_name_generic[0]}_{run_name_generic[1]}")


# this bit converts all the single run names back into r1 and r2 structure and pops them in a dictionary
for i in files_set:
    run_name = i.split("/")[-1]
    f1 = f"{i}_R1_001.fastq.gz"
    f2 = f"{i}_R2_001.fastq.gz"
    file_dictionary[run_name] = {"f1": f1, "f2": f2}

#here the dictionary is converted to json for writing to a file.

json_string = json.dumps(file_dictionary)

with open("files_for_processing.json", "w") as output_file:
    output_file.write(json_string)
    output_file.close()
