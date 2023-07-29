import os
import datetime
import pandas as pd
from data_fetcher.models import Num

# cur_path = os.path.dirname(os.path.abspath(__file__))
# scripts = os.path.join(cur_path, 'scripts')
# data = os.path.join(scripts, 'data')

# naukri=pd.read_excel(os.path.join(data, "NaukriJobListing_" + str(datetime.date.today()) + ".xlsx"))
# # df = naukri
# # dt = df['Job Titles']

# counter = 0
# for index, rows in naukri.iterrows():
#       counter += 1
# print(counter)

def check_database_emptiness(obj):
  if obj.exists():
    return True
  else:
    return False
  
print(check_database_emptiness(Num))