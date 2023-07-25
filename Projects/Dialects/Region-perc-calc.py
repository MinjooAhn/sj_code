import pandas as pd
import numpy as np
"""
Python code for data analysis
Creating an excel sheet with percentage values of each intent / intent category to view major trends
Analysing different age groups in different regions seperately 
Uses a template of data counts provided as excel in the repository ""
"""

# Indexing the Categories in the excel file

REPstart = 2 #추측
REPend = 23   #자랑
EXPstart = 24 #한탄
EXPend = 39   #안타까움
DESstart = 40 #안내
DESend = 45   #객관적경험
INTstart = 46 #WH질문
INTend = 48   #확인질문
DIRstart = 49 #명령
DIRend = 52   #주의
PROstart = 53 #부탁
PROend = 55   #제안
ETCstart = 56 #인사
ETCend = 57 
emostart = 58  #irrel
emoend = 61    #posi
gramstart = 62  #DEC
gramend = 66   #YNI

def load_data():
    """
    Load data from an Excel file based on user input for the 'Type' and 'Region' parameters.

    # Note that file pathing must be set to run the code.

    Input:
    This function prompts the user to input a value for 'Type' (1 or 2) and 'Region'
    (전라, 충청, 제주, 강원, 경상). Type 1 refers to '1인발화' and type 2 refers to '2인발화' but the file paths have been removed.
    Based on the input, it determines the appropriate file path
    and creates a list of region_variable corresponding to the chosen region. It then reads
    the data from the Excel file and returns the needed objects

    Returns:
    - df (pandas.DataFrame): A pandas DataFrame containing the loaded data from the Excel file.
    - region_variable (list): A list of integers representing a range of region codes based on the chosen region.
    - type_input (str): The user-provided 'Type' input 1 for 1인발화 and 2 for 2인발화 but this is determined by file pathing
    - region_input (str): The user-provided 'Region' input (one of '전라', '충청', '제주', '강원', '경상')
.
    """
    type_input = input("Enter Type (1 or 2): ")
    
    if type_input == '1':
        file_path = r""
    elif type_input == '2':
        file_path = r""
    else:
        print("Invalid Type input. Exiting.")
        return None
    
    # Accept user input for the 'Region' parameter
    region_input = input("Enter Region (전라, 충청, 제주, 강원, 경상): ")
    
    if region_input == '전라':
        region_variable = list(range(13, 23))
    elif region_input == '충청':
        region_variable = list(range(3, 13))
    elif region_input == '제주':
        region_variable = list(range(23, 33))
    elif region_input == '강원':
        region_variable = list(range(33, 43))
    elif region_input == '경상':
        region_variable = list(range(43, 53))
    else:
        print("Invalid Region input. Exiting.")
        return None
    
    df = pd.read_excel(file_path)
    
    return df, region_variable, type_input, region_input

# Call the function to load the data and obtain the region_variable
data_frame, region_variable, type_input,region_input = load_data()


# This part of the code sets creates a pandas dataframe for all the possible categories.
# In my run of the code, there were some cells in the excel file missing that created zero division error.
# Code should have been fine with 0 values in cells, but due to the error I set if statements to manualy set it to 0 to prevent error.  (Should be improved) 
# Lastly as this a repetitive code block, it could be tidied up by setting repeating variable strings and calling them as a for loop. (Future improvement)

#REP
REP_df = data_frame.iloc[REPstart:REPend+1, [2]+ region_variable]
REP_df.columns = ["REP", 
                     f"{region_input} 50대 남", 
                     f"{region_input} 60대 남", 
                     f"{region_input} 70대 남", 
                     f"{region_input} 80대 남", 
                     f"{region_input} 90대 남", 
                     f"{region_input} 50대 여", 
                     f"{region_input} 60대 여", 
                     f"{region_input} 70대 여", 
                     f"{region_input} 80대 여",
                     f"{region_input} 90대 여"]
REP_df = REP_df.sort_values(by=f"{region_input} 50대 남", ascending=False)
REP_df[f'{region_input} 50대 남 백분율(%)'] = (REP_df[f"{region_input} 50대 남"] / REP_df[f"{region_input} 50대 남"].sum()) * 100
REP_df[f'{region_input} 60대 남 백분율(%)'] = (REP_df[f"{region_input} 60대 남"] / REP_df[f"{region_input} 60대 남"].sum()) * 100
REP_df[f'{region_input} 70대 남 백분율(%)'] = (REP_df[f"{region_input} 70대 남"] / REP_df[f"{region_input} 70대 남"].sum()) * 100
REP_df[f'{region_input} 80대 남 백분율(%)'] = (REP_df[f"{region_input} 80대 남"] / REP_df[f"{region_input} 80대 남"].sum()) * 100
REP_df[f'{region_input} 90대 남 백분율(%)'] = (REP_df[f"{region_input} 90대 남"] / REP_df[f"{region_input} 90대 남"].sum()) * 100
REP_df[f'{region_input} 50대 여 백분율(%)'] = (REP_df[f"{region_input} 50대 여"] / REP_df[f"{region_input} 50대 여"].sum()) * 100
REP_df[f'{region_input} 60대 여 백분율(%)'] = (REP_df[f"{region_input} 60대 여"] / REP_df[f"{region_input} 60대 여"].sum()) * 100
REP_df[f'{region_input} 70대 여 백분율(%)'] = (REP_df[f"{region_input} 70대 여"] / REP_df[f"{region_input} 70대 여"].sum()) * 100
REP_df[f'{region_input} 80대 여 백분율(%)'] = (REP_df[f"{region_input} 80대 여"] / REP_df[f"{region_input} 80대 여"].sum()) * 100
REP_df[f'{region_input} 90대 여 백분율(%)'] = (REP_df[f"{region_input} 90대 여"] / REP_df[f"{region_input} 90대 여"].sum()) * 100

#EXP
EXP_df = data_frame.iloc[EXPstart:EXPend+1, [2]+ region_variable]
EXP_df.columns = ["EXP", 
                     f"{region_input} 50대 남", 
                     f"{region_input} 60대 남", 
                     f"{region_input} 70대 남", 
                     f"{region_input} 80대 남", 
                     f"{region_input} 90대 남", 
                     f"{region_input} 50대 여", 
                     f"{region_input} 60대 여", 
                     f"{region_input} 70대 여", 
                     f"{region_input} 80대 여",
                     f"{region_input} 90대 여"]
EXP_df = EXP_df.sort_values(by=f"{region_input} 50대 남", ascending=False)
EXP_df[f'{region_input} 50대 남 백분율(%)'] = (EXP_df[f"{region_input} 50대 남"] / EXP_df[f"{region_input} 50대 남"].sum()) * 100
EXP_df[f'{region_input} 60대 남 백분율(%)'] = (EXP_df[f"{region_input} 60대 남"] / EXP_df[f"{region_input} 60대 남"].sum()) * 100
EXP_df[f'{region_input} 70대 남 백분율(%)'] = (EXP_df[f"{region_input} 70대 남"] / EXP_df[f"{region_input} 70대 남"].sum()) * 100
EXP_df[f'{region_input} 80대 남 백분율(%)'] = (EXP_df[f"{region_input} 80대 남"] / EXP_df[f"{region_input} 80대 남"].sum()) * 100
EXP_df[f'{region_input} 90대 남 백분율(%)'] = (EXP_df[f"{region_input} 90대 남"] / EXP_df[f"{region_input} 90대 남"].sum()) * 100
EXP_df[f'{region_input} 50대 여 백분율(%)'] = (EXP_df[f"{region_input} 50대 여"] / EXP_df[f"{region_input} 50대 여"].sum()) * 100
EXP_df[f'{region_input} 60대 여 백분율(%)'] = (EXP_df[f"{region_input} 60대 여"] / EXP_df[f"{region_input} 60대 여"].sum()) * 100
EXP_df[f'{region_input} 70대 여 백분율(%)'] = (EXP_df[f"{region_input} 70대 여"] / EXP_df[f"{region_input} 70대 여"].sum()) * 100
EXP_df[f'{region_input} 80대 여 백분율(%)'] = (EXP_df[f"{region_input} 80대 여"] / EXP_df[f"{region_input} 80대 여"].sum()) * 100
EXP_df[f'{region_input} 90대 여 백분율(%)'] = (EXP_df[f"{region_input} 90대 여"] / EXP_df[f"{region_input} 90대 여"].sum()) * 100

#DES
DES_df = data_frame.iloc[DESstart:DESend+1,[2]+ region_variable]
DES_df.columns = ["DES", 
                     f"{region_input} 50대 남", 
                     f"{region_input} 60대 남", 
                     f"{region_input} 70대 남", 
                     f"{region_input} 80대 남", 
                     f"{region_input} 90대 남", 
                     f"{region_input} 50대 여", 
                     f"{region_input} 60대 여", 
                     f"{region_input} 70대 여", 
                     f"{region_input} 80대 여",
                     f"{region_input} 90대 여"]
DES_df = DES_df.sort_values(by=f"{region_input} 50대 남", ascending=False)
DES_df[f'{region_input} 50대 남 백분율(%)'] = (DES_df[f"{region_input} 50대 남"] / DES_df[f"{region_input} 50대 남"].sum()) * 100
DES_df[f'{region_input} 60대 남 백분율(%)'] = (DES_df[f"{region_input} 60대 남"] / DES_df[f"{region_input} 60대 남"].sum()) * 100
DES_df[f'{region_input} 70대 남 백분율(%)'] = (DES_df[f"{region_input} 70대 남"] / DES_df[f"{region_input} 70대 남"].sum()) * 100
DES_df[f'{region_input} 80대 남 백분율(%)'] = (DES_df[f"{region_input} 80대 남"] / DES_df[f"{region_input} 80대 남"].sum()) * 100
DES_df[f'{region_input} 90대 남 백분율(%)'] = (DES_df[f"{region_input} 90대 남"] / DES_df[f"{region_input} 90대 남"].sum()) * 100
DES_df[f'{region_input} 50대 여 백분율(%)'] = (DES_df[f"{region_input} 50대 여"] / DES_df[f"{region_input} 50대 여"].sum()) * 100
DES_df[f'{region_input} 60대 여 백분율(%)'] = (DES_df[f"{region_input} 60대 여"] / DES_df[f"{region_input} 60대 여"].sum()) * 100
DES_df[f'{region_input} 70대 여 백분율(%)'] = (DES_df[f"{region_input} 70대 여"] / DES_df[f"{region_input} 70대 여"].sum()) * 100
DES_df[f'{region_input} 80대 여 백분율(%)'] = (DES_df[f"{region_input} 80대 여"] / DES_df[f"{region_input} 80대 여"].sum()) * 100
DES_df[f'{region_input} 90대 여 백분율(%)'] = (DES_df[f"{region_input} 90대 여"] / DES_df[f"{region_input} 90대 여"].sum()) * 100

#INT
INT_df = data_frame.iloc[INTstart:INTend+1, [2]+ region_variable]
INT_df.columns = ["INT", 
                     f"{region_input} 50대 남", 
                     f"{region_input} 60대 남", 
                     f"{region_input} 70대 남", 
                     f"{region_input} 80대 남", 
                     f"{region_input} 90대 남", 
                     f"{region_input} 50대 여", 
                     f"{region_input} 60대 여", 
                     f"{region_input} 70대 여", 
                     f"{region_input} 80대 여",
                     f"{region_input} 90대 여"]
INT_df = INT_df.sort_values(by=f"{region_input} 50대 남", ascending=False)
INT_df[f'{region_input} 50대 남 백분율(%)'] = (INT_df[f"{region_input} 50대 남"] / INT_df[f"{region_input} 50대 남"].sum()) * 100
INT_df[f'{region_input} 60대 남 백분율(%)'] = (INT_df[f"{region_input} 60대 남"] / INT_df[f"{region_input} 60대 남"].sum()) * 100
INT_df[f'{region_input} 70대 남 백분율(%)'] = (INT_df[f"{region_input} 70대 남"] / INT_df[f"{region_input} 70대 남"].sum()) * 100
INT_df[f'{region_input} 80대 남 백분율(%)'] = (INT_df[f"{region_input} 80대 남"] / INT_df[f"{region_input} 80대 남"].sum()) * 100
INT_df[f'{region_input} 90대 남 백분율(%)'] = (INT_df[f"{region_input} 90대 남"] / INT_df[f"{region_input} 90대 남"].sum()) * 100
INT_df[f'{region_input} 50대 여 백분율(%)'] = (INT_df[f"{region_input} 50대 여"] / INT_df[f"{region_input} 50대 여"].sum()) * 100
INT_df[f'{region_input} 60대 여 백분율(%)'] = (INT_df[f"{region_input} 60대 여"] / INT_df[f"{region_input} 60대 여"].sum()) * 100
INT_df[f'{region_input} 70대 여 백분율(%)'] = (INT_df[f"{region_input} 70대 여"] / INT_df[f"{region_input} 70대 여"].sum()) * 100
INT_df[f'{region_input} 80대 여 백분율(%)'] = (INT_df[f"{region_input} 80대 여"] / INT_df[f"{region_input} 80대 여"].sum()) * 100
INT_df[f'{region_input} 90대 여 백분율(%)'] = (INT_df[f"{region_input} 90대 여"] / INT_df[f"{region_input} 90대 여"].sum()) * 100

#DIR
DIR_df = data_frame.iloc[DIRstart:DIRend+1, [2]+ region_variable]
DIR_df.columns = ["DIR", 
                     f"{region_input} 50대 남", 
                     f"{region_input} 60대 남", 
                     f"{region_input} 70대 남", 
                     f"{region_input} 80대 남", 
                     f"{region_input} 90대 남", 
                     f"{region_input} 50대 여", 
                     f"{region_input} 60대 여", 
                     f"{region_input} 70대 여", 
                     f"{region_input} 80대 여",
                     f"{region_input} 90대 여"]
DIR_df = DIR_df.sort_values(by=f"{region_input} 50대 남", ascending=False)
DIR_df[f'{region_input} 50대 남 백분율(%)'] = (DIR_df[f"{region_input} 50대 남"] / DIR_df[f"{region_input} 50대 남"].sum()) * 100
DIR_df[f'{region_input} 60대 남 백분율(%)'] = (DIR_df[f"{region_input} 60대 남"] / DIR_df[f"{region_input} 60대 남"].sum()) * 100
DIR_df[f'{region_input} 70대 남 백분율(%)'] = (DIR_df[f"{region_input} 70대 남"] / DIR_df[f"{region_input} 70대 남"].sum()) * 100
DIR_df[f'{region_input} 80대 남 백분율(%)'] = (DIR_df[f"{region_input} 80대 남"] / DIR_df[f"{region_input} 80대 남"].sum()) * 100
DIR_df[f'{region_input} 90대 남 백분율(%)'] = (DIR_df[f"{region_input} 90대 남"] / DIR_df[f"{region_input} 90대 남"].sum()) * 100
if DIR_df[f"{region_input} 50대 여"].sum() == 0:
    DIR_df[f'{region_input} 50대 여 백분율(%)'] = 0
else:
    DIR_df[f'{region_input} 50대 여 백분율(%)'] = (DIR_df[f"{region_input} 50대 여"] / DIR_df[f"{region_input} 50대 여"].sum()) * 100
DIR_df[f'{region_input} 60대 여 백분율(%)'] = (DIR_df[f"{region_input} 60대 여"] / DIR_df[f"{region_input} 60대 여"].sum()) * 100
DIR_df[f'{region_input} 70대 여 백분율(%)'] = (DIR_df[f"{region_input} 70대 여"] / DIR_df[f"{region_input} 70대 여"].sum()) * 100
DIR_df[f'{region_input} 80대 여 백분율(%)'] = (DIR_df[f"{region_input} 80대 여"] / DIR_df[f"{region_input} 80대 여"].sum()) * 100
DIR_df[f'{region_input} 90대 여 백분율(%)'] = (DIR_df[f"{region_input} 90대 여"] / DIR_df[f"{region_input} 90대 여"].sum()) * 100

#PRO
PRO_df = data_frame.iloc[PROstart:PROend+1, [2]+ region_variable]
PRO_df.columns = ["PRO", 
                     f"{region_input} 50대 남", 
                     f"{region_input} 60대 남", 
                     f"{region_input} 70대 남", 
                     f"{region_input} 80대 남", 
                     f"{region_input} 90대 남", 
                     f"{region_input} 50대 여", 
                     f"{region_input} 60대 여", 
                     f"{region_input} 70대 여", 
                     f"{region_input} 80대 여",
                     f"{region_input} 90대 여"]
PRO_df = PRO_df.sort_values(by=f"{region_input} 50대 남", ascending=False)
PRO_df[f'{region_input} 50대 남 백분율(%)'] = (PRO_df[f"{region_input} 50대 남"] / PRO_df[f"{region_input} 50대 남"].sum()) * 100
PRO_df[f'{region_input} 60대 남 백분율(%)'] = (PRO_df[f"{region_input} 60대 남"] / PRO_df[f"{region_input} 60대 남"].sum()) * 100
PRO_df[f'{region_input} 70대 남 백분율(%)'] = (PRO_df[f"{region_input} 70대 남"] / PRO_df[f"{region_input} 70대 남"].sum()) * 100
PRO_df[f'{region_input} 80대 남 백분율(%)'] = (PRO_df[f"{region_input} 80대 남"] / PRO_df[f"{region_input} 80대 남"].sum()) * 100
PRO_df[f'{region_input} 90대 남 백분율(%)'] = (PRO_df[f"{region_input} 90대 남"] / PRO_df[f"{region_input} 90대 남"].sum()) * 100
PRO_df[f'{region_input} 50대 여 백분율(%)'] = (PRO_df[f"{region_input} 50대 여"] / PRO_df[f"{region_input} 50대 여"].sum()) * 100
PRO_df[f'{region_input} 60대 여 백분율(%)'] = (PRO_df[f"{region_input} 60대 여"] / PRO_df[f"{region_input} 60대 여"].sum()) * 100
PRO_df[f'{region_input} 70대 여 백분율(%)'] = (PRO_df[f"{region_input} 70대 여"] / PRO_df[f"{region_input} 70대 여"].sum()) * 100
PRO_df[f'{region_input} 80대 여 백분율(%)'] = (PRO_df[f"{region_input} 80대 여"] / PRO_df[f"{region_input} 80대 여"].sum()) * 100
PRO_df[f'{region_input} 90대 여 백분율(%)'] = (PRO_df[f"{region_input} 90대 여"] / PRO_df[f"{region_input} 90대 여"].sum()) * 100

#ETC
ETC_df = data_frame.iloc[ETCstart:ETCend+1, [2]+ region_variable]
ETC_df.columns = ["ETC", 
                     f"{region_input} 50대 남", 
                     f"{region_input} 60대 남", 
                     f"{region_input} 70대 남", 
                     f"{region_input} 80대 남", 
                     f"{region_input} 90대 남", 
                     f"{region_input} 50대 여", 
                     f"{region_input} 60대 여", 
                     f"{region_input} 70대 여", 
                     f"{region_input} 80대 여",
                     f"{region_input} 90대 여"]
ETC_df = ETC_df.sort_values(by=f"{region_input} 50대 남", ascending=False)
if ETC_df[f"{region_input} 50대 남"].sum() == 0:
    ETC_df[f'{region_input} 50대 남 백분율(%)'] = 0
else:
    ETC_df[f'{region_input} 50대 남 백분율(%)'] = (ETC_df[f"{region_input} 50대 남"] / ETC_df[f"{region_input} 50대 남"].sum()) * 100
ETC_df[f'{region_input} 60대 남 백분율(%)'] = (ETC_df[f"{region_input} 60대 남"] / ETC_df[f"{region_input} 60대 남"].sum()) * 100
ETC_df[f'{region_input} 70대 남 백분율(%)'] = (ETC_df[f"{region_input} 70대 남"] / ETC_df[f"{region_input} 70대 남"].sum()) * 100
ETC_df[f'{region_input} 80대 남 백분율(%)'] = (ETC_df[f"{region_input} 80대 남"] / ETC_df[f"{region_input} 80대 남"].sum()) * 100
ETC_df[f'{region_input} 90대 남 백분율(%)'] = (ETC_df[f"{region_input} 90대 남"] / ETC_df[f"{region_input} 90대 남"].sum()) * 100
if ETC_df[f"{region_input} 50대 여"].sum() == 0:
    ETC_df[f'{region_input} 50대 여 백분율(%)'] = 0
else:
    ETC_df[f'{region_input} 50대 여 백분율(%)'] = (ETC_df[f"{region_input} 50대 여"] / ETC_df[f"{region_input} 50대 여"].sum()) * 100
ETC_df[f'{region_input} 60대 여 백분율(%)'] = (ETC_df[f"{region_input} 60대 여"] / ETC_df[f"{region_input} 60대 여"].sum()) * 100
ETC_df[f'{region_input} 70대 여 백분율(%)'] = (ETC_df[f"{region_input} 70대 여"] / ETC_df[f"{region_input} 70대 여"].sum()) * 100
ETC_df[f'{region_input} 80대 여 백분율(%)'] = (ETC_df[f"{region_input} 80대 여"] / ETC_df[f"{region_input} 80대 여"].sum()) * 100
ETC_df[f'{region_input} 90대 여 백분율(%)'] = (ETC_df[f"{region_input} 90대 여"] / ETC_df[f"{region_input} 90대 여"].sum()) * 100

#Emotion
emotion_df = data_frame.iloc[emostart:emoend +1, [2]+ region_variable]
emotion_df.columns = ["Emotion", 
                     f"{region_input} 50대 남", 
                     f"{region_input} 60대 남", 
                     f"{region_input} 70대 남", 
                     f"{region_input} 80대 남", 
                     f"{region_input} 90대 남", 
                     f"{region_input} 50대 여", 
                     f"{region_input} 60대 여", 
                     f"{region_input} 70대 여", 
                     f"{region_input} 80대 여",
                     f"{region_input} 90대 여"]
emotion_df = emotion_df.sort_values(by=f"{region_input} 50대 남", ascending=False)
emotion_df[f'{region_input} 50대 남 백분율(%)'] = (emotion_df[f"{region_input} 50대 남"] / emotion_df[f"{region_input} 50대 남"].sum()) * 100
emotion_df[f'{region_input} 60대 남 백분율(%)'] = (emotion_df[f"{region_input} 60대 남"] / emotion_df[f"{region_input} 60대 남"].sum()) * 100
emotion_df[f'{region_input} 70대 남 백분율(%)'] = (emotion_df[f"{region_input} 70대 남"] / emotion_df[f"{region_input} 70대 남"].sum()) * 100
emotion_df[f'{region_input} 80대 남 백분율(%)'] = (emotion_df[f"{region_input} 80대 남"] / emotion_df[f"{region_input} 80대 남"].sum()) * 100
emotion_df[f'{region_input} 90대 남 백분율(%)'] = (emotion_df[f"{region_input} 90대 남"] / emotion_df[f"{region_input} 90대 남"].sum()) * 100
emotion_df[f'{region_input} 50대 여 백분율(%)'] = (emotion_df[f"{region_input} 50대 여"] / emotion_df[f"{region_input} 50대 여"].sum()) * 100
emotion_df[f'{region_input} 60대 여 백분율(%)'] = (emotion_df[f"{region_input} 60대 여"] / emotion_df[f"{region_input} 60대 여"].sum()) * 100
emotion_df[f'{region_input} 70대 여 백분율(%)'] = (emotion_df[f"{region_input} 70대 여"] / emotion_df[f"{region_input} 70대 여"].sum()) * 100
emotion_df[f'{region_input} 80대 여 백분율(%)'] = (emotion_df[f"{region_input} 80대 여"] / emotion_df[f"{region_input} 80대 여"].sum()) * 100
emotion_df[f'{region_input} 90대 여 백분율(%)'] = (emotion_df[f"{region_input} 90대 여"] / emotion_df[f"{region_input} 90대 여"].sum()) * 100

#Grammar
grammar_df = data_frame.iloc[gramstart:gramend +1, [2]+ region_variable]
grammar_df.columns = ["Grammar", 
                     f"{region_input} 50대 남", 
                     f"{region_input} 60대 남", 
                     f"{region_input} 70대 남", 
                     f"{region_input} 80대 남", 
                     f"{region_input} 90대 남", 
                     f"{region_input} 50대 여", 
                     f"{region_input} 60대 여", 
                     f"{region_input} 70대 여", 
                     f"{region_input} 80대 여",
                     f"{region_input} 90대 여"]
grammar_df = grammar_df.sort_values(by=f"{region_input} 50대 남", ascending=False)
grammar_df[f'{region_input} 50대 남 백분율(%)'] = (grammar_df[f"{region_input} 50대 남"] / grammar_df[f"{region_input} 50대 남"].sum()) * 100
grammar_df[f'{region_input} 60대 남 백분율(%)'] = (grammar_df[f"{region_input} 60대 남"] / grammar_df[f"{region_input} 60대 남"].sum()) * 100
grammar_df[f'{region_input} 70대 남 백분율(%)'] = (grammar_df[f"{region_input} 70대 남"] / grammar_df[f"{region_input} 70대 남"].sum()) * 100
grammar_df[f'{region_input} 80대 남 백분율(%)'] = (grammar_df[f"{region_input} 80대 남"] / grammar_df[f"{region_input} 80대 남"].sum()) * 100
grammar_df[f'{region_input} 90대 남 백분율(%)'] = (grammar_df[f"{region_input} 90대 남"] / grammar_df[f"{region_input} 90대 남"].sum()) * 100
grammar_df[f'{region_input} 50대 여 백분율(%)'] = (grammar_df[f"{region_input} 50대 여"] / grammar_df[f"{region_input} 50대 여"].sum()) * 100
grammar_df[f'{region_input} 60대 여 백분율(%)'] = (grammar_df[f"{region_input} 60대 여"] / grammar_df[f"{region_input} 60대 여"].sum()) * 100
grammar_df[f'{region_input} 70대 여 백분율(%)'] = (grammar_df[f"{region_input} 70대 여"] / grammar_df[f"{region_input} 70대 여"].sum()) * 100
grammar_df[f'{region_input} 80대 여 백분율(%)'] = (grammar_df[f"{region_input} 80대 여"] / grammar_df[f"{region_input} 80대 여"].sum()) * 100
grammar_df[f'{region_input} 90대 여 백분율(%)'] = (grammar_df[f"{region_input} 90대 여"] / grammar_df[f"{region_input} 90대 여"].sum()) * 100

#Intention
intention_df = data_frame.iloc[REPstart:ETCend +1, [1] + region_variable]
intention_df.columns = ["Intention", 
                     f"{region_input} 50대 남", 
                     f"{region_input} 60대 남", 
                     f"{region_input} 70대 남", 
                     f"{region_input} 80대 남", 
                     f"{region_input} 90대 남", 
                     f"{region_input} 50대 여", 
                     f"{region_input} 60대 여", 
                     f"{region_input} 70대 여", 
                     f"{region_input} 80대 여",
                     f"{region_input} 90대 여"]
intention_df["Intention"] = intention_df["Intention"].fillna(method='ffill')

# Larger Intention category was a joint category of all sub categories as shown in the excel file.
# There probably is a better way to deal with these joint category situation, but I just took the measure to add all the rows and use index slicing to create the df.
# Create a new DataFrame to store the counts
intention2_df = pd.DataFrame(columns=["Intention"])

# Get unique intention types from the original DataFrame
intention_types = intention_df["Intention"].unique()

# Iterate over the unique intention types
for intention_type in intention_types:
    # Filter the rows for the current intention type
    filtered_rows = intention_df[intention_df["Intention"] == intention_type]

    # Sum the values in each column for the filtered rows
    summed_values = filtered_rows.iloc[:, 1:].sum()

    # Create a new row with the intention type and summed values
    row = {"Intention": intention_type}
    for column, value in summed_values.items():
        row[column] = value

    # Append the row to the counts DataFrame
    intention2_df = pd.concat([intention2_df,pd.DataFrame([row])],ignore_index=True)


# Excel file creation (path name should be set)


path = r""
writer = pd.ExcelWriter(path + region_input +type_input +"인발화 통계.xlsx", engine = "xlsxwriter")
REP_df.to_excel(writer, sheet_name="REP")
EXP_df.to_excel(writer, sheet_name="EXP")
DES_df.to_excel(writer, sheet_name="DES")
INT_df.to_excel(writer, sheet_name="INT")
DIR_df.to_excel(writer, sheet_name="DIR")
PRO_df.to_excel(writer, sheet_name="PRO")
ETC_df.to_excel(writer, sheet_name="ETC")
emotion_df.to_excel(writer, sheet_name="Emotion")
grammar_df.to_excel(writer, sheet_name="Grammar")
intention2_df.to_excel(writer, sheet_name='Intention')
writer.close()


if __name__ == '__main__':
    # Call the function to load the data and obtain the region_variable
     data_frame, region_variable, type_input, region_input = load_data()
