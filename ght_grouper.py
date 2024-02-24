__author__ = "Da young Lee"
__credits__ = ["Seung hyup Hyun", "Jong chul Han", "Da young Lee"]
__version__ = "1.0.0"
__date__ = "2018.05.04"
__maintainer__ = "Da young Lee"
__email__ = "dyan.lee717@gmail.com"
__status__ = "Unofficial"

import os
import sys
import glob
import shutil
import pandas as pd

data_dirr = 'GHT_image/'
data_list = glob.glob(data_dirr+'*.jpg')
data_len = len(data_list)
print('》 Image data directory is, "', data_dirr,'"')
print('》 There are  (',data_len,')  image files in data directory.  \n')

xlsx_path = 'ght2txt_result.xlsx'
df = pd.read_excel(xlsx_path,index_col=False, columns = False)
file_name = df['FileName']
print("》 Please Enter a name of column as criteria for sorting.")
print("    (If 'KeyError' occurs,")
print("        check the typed value matches column name.)" )
col_name = input('Column >>> ')


def mkdir_path(folder_dir):
    if not os.path.exists(folder_dir):
        os.mkdir(folder_dir)
    return folder_dir


def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(round(length * iteration // float(total)))
    bar = fill * filledLength + '-' * (length - filledLength)
    sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percent, '%', suffix))#, end = '\r')
    # Print New Line on Complete
    if iteration == total: 
        sys.stdout.write('\n')
    sys.stdout.flush()


print('\n')
print('》 Grouping images... ')
target_col = df[col_name]
for i, value in enumerate(target_col):   
    gr_dir = os.path.join(data_dirr+value+'\\')
    os.makedirs(gr_dir, exist_ok=True)
    shutil.copy(data_dirr+file_name[i], gr_dir+file_name[i])
    printProgressBar(i, len(target_col)-1, 'Sorting: ', 'Complete!', 1, 60)
    if data_len-i-1 == 0:
        break

print('》 Done. \n')

input('Press ENTER key to exit >>> ')
