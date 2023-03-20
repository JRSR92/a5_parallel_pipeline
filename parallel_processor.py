import subprocess
import json
import os
from multiprocessing import Pool, freeze_support


# this function takes in links from the json file for each run and processes them using the normal a5_pipline
def process_data(run_id, f1, f2):

    #does a check to see if output folder exists, and creates if it doesnt to use for output files.
    dir_check = os.path.exists(run_id)
    if not dir_check:
        os.makedirs(run_id)
    #moves into the output directory
    os.chdir(run_id)
    #normal a5_pipeline is called.
    subprocess.run(["/home/jack/Desktop/a5_miseq_linux_20160825/bin/a5_pipeline.pl",
                f1,
                f2,
                run_id],
                stderr=subprocess.PIPE, text=True)
    #move out of output directory
    os.chdir('../')

if __name__ == '__main__':
    #reads in the json document to get file locations
    with open("/home/jack/Desktop/a5_files/files_for_processing.json") as f:
        json_data = json.loads(f.read())

    run_tuples = []
    # creates and iterable item for supplying the function with variables
    for k, v in json_data.items():
        run_id = k
        f1 = v['f1']
        f2 = v['f2']
        run_tuples.append((run_id, f1, f2))
    print(run_tuples)

    # start 4 worker processes
    with Pool(processes=4) as pool:
        pool.starmap(process_data, run_tuples)



