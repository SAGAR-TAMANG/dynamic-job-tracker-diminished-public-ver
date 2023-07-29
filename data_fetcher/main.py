# import re
# import string
# import datetime
# import os
# import subprocess

# import pandas as pd
# # import numpy as np
# # import matplotlib.pyplot as plt

# from data_fetcher.models import NumJobs, TitlesFrequency
# from storage.models import database_storage
# import nltk
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize

# cur_path = os.path.dirname(os.path.abspath(__file__))
# scripts = os.path.join(cur_path, 'scripts')
# data = os.path.join(scripts, 'data')

# # sys.path.append(scripts)
# ## Turn these on later:
# nltk.download('punkt')
# nltk.download('stopwords')

# database = pd.DataFrame(columns=['Job Title','Description', 'Experience Reqd', 'Company', 'City', 'Salary Range', 'Date Posted', 'Rating', 'Site', 'URL'])
# today = 0
# week = 0
# others = 0
# total = 0

# try:
#   naukri=pd.read_excel(os.path.join(data, "NaukriJobListing_" + str(datetime.date.today()) + ".xlsx"))
#   database = pd.concat([database, naukri], ignore_index=True)
#   print('exception did not occur')
#   print('THE DATABASE :', database)
# except Exception as e:
#   print('*****************\nEXCEPTION OCCURED \n DATA NOT PRESENT \n FETCHING DATA NOW\n*****************\n PLEASE WAIT...')
#   print('COULD NOT FIND FILE: ' + os.path.join(data, "NaukriJobListing_" + str(datetime.date.today()) + ".xlsx"))
#   n = subprocess.run(['python', os.path.join(scripts, 'naukri scraper.py')])
#   naukri=pd.read_excel(os.path.join(data, "NaukriJobListing_" + str(datetime.date.today()) + ".xlsx"))
#   database = pd.concat([database, naukri], ignore_index=True)

#   print('THE DATABASE :', database)

# try:
#   iimjobs=pd.read_excel(os.path.join(data, "IIMJobsJobListing_" + str(datetime.date.today()) + ".xlsx"))
#   database = pd.concat([database, naukri], ignore_index=True)
#   print('THE DATABASE :', database)
# except Exception as e: 
#   print('EXCEPTION OCCURED \n DATA NOT PRESENT \n \n FETCHING DATA NOW, PLEASE WAIT...')
#   print('COULD NOT FIND FILE: ' + os.path.join(data, "IIMJobsJobListing_" + str(datetime.date.today()) + ".xlsx"))
#   iim = subprocess.run(['python', os.path.join(scripts, 'iimjobs scraper.py')])
#   iimjobs=pd.read_excel(os.path.join(data, "IIMJobsJobListing_" + str(datetime.date.today()) + ".xlsx"))
#   database = pd.concat([database, iimjobs], ignore_index=True)

# try:
#   timesjobs=pd.read_excel(os.path.join(data, "TimesJobs_" + str(datetime.date.today()) + ".xlsx"))
#   database = pd.concat([database, timesjobs], ignore_index=True)
#   print('exception did not occur')
#   print('THE DATABASE :', database)
# except Exception as e:
#   print('*****************\nEXCEPTION OCCURED \n DATA NOT PRESENT \n FETCHING DATA NOW\n*****************\n PLEASE WAIT...')
#   print('COULD NOT FIND FILE: ' + os.path.join(data, "TimesJobs_" + str(datetime.date.today()) + ".xlsx"))
#   t = subprocess.run(['python', os.path.join(scripts, 'timesjobs scraper.py')])
#   timesjobs=pd.read_excel(os.path.join(data, "TimesJobs_" + str(datetime.date.today()) + ".xlsx"))
#   database = pd.concat([database, timesjobs], ignore_index=True)

# if os.path.join(data, "Database_" + str(datetime.date.today()) + ".xlsx"):
#   pass
# else:
#   database.to_excel(os.path.join(data, "Database_" + str(datetime.date.today()) + ".xlsx"), index=False)

# # job_titles=pd.read_excel(os.path.join(data, "job-titles.xlsx"))

# def frequency_title(column):
#   stop_words = stopwords.words()  

#   def cleaning(text):        
#       # converting to lowercase, removing URL links, special characters, punctuations...
#       text = text.lower()
#       text = re.sub('https?://\S+|www\.\S+', '', text)
#       text = re.sub('<.*?>+', '', text)
#       text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
#       text = re.sub('\n', '', text)
#       text = re.sub('[’“”…]', '', text)     

#       # removing the emojies               # https://www.kaggle.com/alankritamishra/covid-19-tweet-sentiment-analysis#Sentiment-analysis
#       emoji_pattern = re.compile("["
#                             u"\U0001F600-\U0001F64F"  # emoticons
#                             u"\U0001F300-\U0001F5FF"  # symbols & pictographs
#                             u"\U0001F680-\U0001F6FF"  # transport & map symbols
#                             u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
#                             u"\U00002702-\U000027B0"
#                             u"\U000024C2-\U0001F251"
#                             "]+", flags=re.UNICODE)
#       text = emoji_pattern.sub(r'', text)   
      
#       # removing the stop-words          
#       text_tokens = word_tokenize(text)
#       tokens_without_sw = [word for word in text_tokens if not word in stop_words]
#       filtered_sentence = (" ").join(tokens_without_sw)
#       text = filtered_sentence
      
#       return text
  
#   df = database
#   dt = df[column].apply(cleaning)

#   from collections import Counter
#   p = Counter(" ".join(dt).split()).most_common(4)
#   rslt = pd.DataFrame(p, columns=['Word', 'Frequency'])
#   for index, row in rslt.iterrows():
#         print(row)
#         bar_graph_data = TitlesFrequency(label=row['Word'], value=row['Frequency'])
#         bar_graph_data.save()
#   return(rslt)

# def exporting_excel(df_name):
#   df_name.to_excel(os.path.join(data, df_name + '.xlsx'), index = False)

# def remove_TitlesFrequency():
#   TitlesFrequency.objects.all().delete()
#   print('FLUSHED DATABASE "TitlesFrequency"')

# def remove_NumJobs():
#   NumJobs.objects.all().delete()
#   print('FLUSHED DATABASE "NumJobs"')

# def remove_Num():
#   Num.objects.all().delete()
#   print('FLUSHED DATABASE "Num"')

# def remove_storage():
#   database_storage.objects.all().delete()
#   print('FLUSHED STORAGE, DATABASE "database_storage"')

# def count_min_exp():
#   global zero, three, five 
#   global zero_sal, three_sal, five_sal
#   zero_sal = 0
#   three_sal = 0
#   five_sal = 0
#   exp_initial_fetcher = lambda text: text.split('-')[0]
#   for index, row in database.iterrows():
#     var = row['Experience Reqd']
    
#     if var != 'Not-Mentioned':
#       initial_val = exp_initial_fetcher(var)
#       initial_val = int(initial_val)
#       if initial_val == 0:
#         zero_sal += 1
#       elif initial_val >= 3 and initial_val < 5:
#         three_sal += 1
#       elif initial_val >= 5:
#         five_sal += 1
#   print('ZERO :', zero_sal)
#   print('THREE :', three_sal)
#   print('FIVE :', five_sal)
#   print('*********COMPLETED TAKING OUT THE MINIMUM EXPERIENCE REQUIRED**********')

# def date_posted(type, today, week, others, total):
#   if type == 'naukri':
#     print('NAUKRI INITIATED')
#     df = naukri
#     instance = NumJobs(today = 0, week = 0, others = 0, total = 0)
#     for index, row in df.iterrows():
#       try:
#         dates = row['Date Posted'].strip()
#       except Exception as e:
#         print("EXCEPTION OCCURED NAUKRI DATE")
#         print('DATE POSTED WAS:', dates)
#         pass
#       try:
#         if dates == 'Just Now':
#           today += 1
#           week += 1
#         elif dates == '1 Day Ago' or dates == '2 Days Ago'  or dates == '3 Days Ago' or dates == '4 Days Ago' or dates == '5 Days Ago' or dates == '6 Days Ago':
#           week += 1
#         else:
#           others += 1
#       except Exception as e: 
#         print('EXCEPTION OCCURED DURING THE RUNNING OF def date_posted')
#     # total = today + week + others
#     instance.today = today
#     instance.week = week
#     instance.others = others
#     instance.total = today + week + others
#     instance.save()
#   elif type == 'iimjobs':
#     print('IIM JOBS INITIATED')
#     df = iimjobs
#     current_date = datetime.date.today()
#     y0 = current_date.strftime("%d/%m/%Y")
#     for index, row in df.iterrows():
#       date = row['Date Posted'].strip()
#       y1 = current_date - datetime.timedelta(days=1)
#       y1 = y1.strftime("%d/%m/%Y")
#       y2 = current_date - datetime.timedelta(days=2)
#       y2 = y2.strftime("%d/%m/%Y")
#       y3 = current_date - datetime.timedelta(days=3)
#       y3 = y3.strftime("%d/%m/%Y")
#       y4 = current_date - datetime.timedelta(days=4)
#       y4 = y4.strftime("%d/%m/%Y")
#       y5 = current_date - datetime.timedelta(days=6)
#       y5 = y5.strftime("%d/%m/%Y")
#       if date == y0:
#         today+=1
#         week+=1
#       elif date == y1 or date == y2 or date == y3 or date == y4 or date == y5:
#         week+=1
#       else:
#         others+=1
#     total = today + week + others
#     instanceNumJobs = NumJobs(today = today, week = week, others = others, total = total)
#     instanceNumJobs.save()

# ## RUNNING THE FUNCTIONS:

# def check_database_emptiness(obj):
#   return obj.exists()

# # def main_temp():
# #   frequency = frequency_title('Job Title')
# #   data_exp_reqd = count_min_exp()
# #   naukri_date_posted=date_posted('naukri')
# #   iim_date_posted=date_posted('iimjobs')
# #   print('SUCCESSFUL CONCLUSION OF THE PROGRAM')

# def main():
#   print('RUNNING MAIN')
#   if check_database_emptiness(NumJobs.objects.all()) is False:
#     date_posted('naukri', today, week, others, total)
#     date_posted('iimjobs', today, week, others, total)

#   else:
#     remove_NumJobs()  
#     date_posted('naukri', today, week, others, total)
#     date_posted('iimjobs', today, week, others, total)

#   if check_database_emptiness(TitlesFrequency.objects.all()) is False:
#     frequency = frequency_title('Job Title')
#   else:
#     remove_TitlesFrequency()
#     frequency = frequency_title('Job Title')
  
#   if check_database_emptiness(database_storage.objects.all()) is False:
#     adding_database_instance = database_storage(database = "Database_" + str(datetime.date.today()) + ".xlsx", naukri = "NaukriJobListing_" + str(datetime.date.today()) + ".xlsx", iimjob = "IIMJobsJobListing_" + str(datetime.date.today()) + ".xlsx")
#     adding_database_instance.save()
#   else:
#     remove_storage()
#     adding_database_instance = database_storage(database = "Database_" + str(datetime.date.today()) + ".xlsx", naukri = "NaukriJobListing_" + str(datetime.date.today()) + ".xlsx", iimjob = "IIMJobsJobListing_" + str(datetime.date.today()) + ".xlsx")    
#     adding_database_instance.save()
#     # adding_database_instance = database_storage(database = "Database_" + str(datetime.date.today()) + ".xlsx")
#     # adding_naukri_instance = database_storage(naukri = "NaukriJobListing_" + str(datetime.date.today()) + ".xlsx")
#     # adding_iimjobs_instance = database_storage(iimjob = "IIMJobsJobListing_" + str(datetime.date.today()) + ".xlsx")

#   print('SUCCESSFUL CONCLUSION OF THE PROGRAM')
#   home_dir = os.path.abspath(os.path.curdir)
#   i = subprocess.Popen(['python', home_dir + '/data_visualization/main.py'])

# # if __name__ == '__main__': # Use this to make the script run only when it's directly executed
# #   main()

# main()  