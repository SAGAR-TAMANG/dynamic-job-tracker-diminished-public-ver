import threading
import os
import datetime
import subprocess

print("###########################")
print("DATA VISUALIZATION UNDERWAY")
print("###########################")
current_directory = os.path.abspath(os.path.curdir)

def check(file):
    naukri_path = os.path.join(current_directory, 'templates', 'IndianMap', 'map_of_india_NaukriJobListing_' +  str(datetime.date.today())+ '.html')
    iimjobs_path = os.path.join(current_directory, 'templates', 'IndianMap', 'map_of_india_IIMJobListing_' +  str(datetime.date.today())+ '.html')
    timesjobs_path = os.path.join(current_directory, 'templates', 'IndianMap', 'map_of_india_TimesJobs_' +  str(datetime.date.today())+ '.html')

    if file == 'naukri':
        if os.path.exists(naukri_path):
            print("NAUKRI FILE FOUND!")
        else:
            print("NAUKRI FILE DOESN'T EXIST \n RUNNING NAUKRI SCRIPT")
            i = subprocess.run(['python', os.path.join(current_directory, 'data_visualization', 'scripts', 'naukri_viz.py')])
            print("NAUKRI SCRIPT RAN SUCCESSFULLY")
    elif file == 'iimjobs':
        if os.path.exists(iimjobs_path):
            print("IIMJOBS FILE FOUND!")
        else:
            print("IIMJOBS FILE DOESN'T EXIST \n RUNNING IIMJOBS SCRIPT")
            i = subprocess.run(['python', os.path.join(current_directory, 'data_visualization', 'scripts', 'iimjobs_viz.py')])
            print("IIMJOBS SCRIPT RAN SUCCESSFULLY")
    elif file == 'timesjobs':
        if os.path.exists(timesjobs_path):
            print("TIMESJOBS FILE FOUND!")
        else:
            print("TIMESJOBS FILE DOESN'T EXIST \n RUNNING TIMESJOBS SCRIPT")
            i = subprocess.run(['python', os.path.join(current_directory, 'data_visualization', 'scripts', 'timesjobs_viz.py')])
            print("TIMESJOBS SCRIPT RAN SUCCESSFULLY")

    print('CHECKING COMPLETE \n ##############################################')


def main():
    print("##############################################")
    print("CHECKING IF FILES EXIST")
    print("##############################################")
    naukri = threading.Thread(target=check, args=('naukri',))
    iimjobs = threading.Thread(target=check, args=('iimjobs',))
    timesjobs = threading.Thread(target=check, args=('timesjobs',))

    naukri.start()
    iimjobs.start()
    timesjobs.start()

    naukri.join()
    iimjobs.join()
    timesjobs.join()

    print("##############################################")
    print("ALL FILES CHECKED")
    print("##############################################")


main()