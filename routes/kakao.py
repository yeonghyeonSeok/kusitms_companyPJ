# -*- coding: euc-kr -*-
#import numpy as np
import pandas as pd
#from pandas import DataFrame
import re
import datetime as dt
import json
from numpyencoder import NumpyEncoder
#import glob
#from sklearn.preprocessing import StandardScaler
#from scipy.stats import norm

#�� ���� ù�ٰ� �Ʒ� 4���� VSCODE ���ڵ� ���������� �߰��ѰŶ� �Ű�Ⱦ��ŵ��˴ϴ�!
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

def read_kko_msg(filename):
    with open(filename, encoding='utf-8') as f:
        msg_list = f.readlines()
    return msg_list

def apply_kko_regex(msg_list):
    kko_pattern = re.compile("\[([\S\s]+)\] \[(����|����) ([0-9:\s]+)\] ([^\n]+)")
    kko_date_pattern = re.compile("--------------- ([0-9]+�� [0-9]+�� [0-9]+��) ")

    emoji_pattern = re.compile("["u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               "]+", flags=re.UNICODE)

    kko_parse_result = list()
    cur_date = ""

    for msg in msg_list:
        # ��¥ �κ��� ���
        if len(kko_date_pattern.findall(msg)) > 0:
            cur_date = dt.datetime.strptime(kko_date_pattern.findall(msg)[0], "%Y�� %m�� %d��")
            cur_date = cur_date.strftime("%Y-%m-%d")
        else:
            kko_pattern_result = kko_pattern.findall(msg)
            if len(kko_pattern_result) > 0:
                tokens = list(kko_pattern_result[0])
                # �̸��� ������ ����
                tokens[-1] = re.sub(emoji_pattern, "", tokens[-1])
                tokens.insert(0, cur_date)
                kko_parse_result.append(tokens)

    kko_parse_result = pd.DataFrame(kko_parse_result, columns=["Date", "User", "Timetype", "Time", "Message"])
    kko_parse_result.to_csv("kko_regex.csv", index=False)

    return kko_parse_result

def extract_period(df) :
    start = df.iloc[0]['Date']
    end = df.iloc[-1]['Date']
    #print("Start :", start) #TODO: print�ϴ� �׸���� ���� ������ return�Ǵ� ������ �켱 print�� �ʿ��� �׸�鸸 ���ܵξ����ϴ�!
    #print("End :", end) #TODO: print�ϴ� �׸���� ���� ������ return�Ǵ� ������ �켱 print�� �ʿ��� �׸�鸸 ���ܵξ����ϴ�!
    start = start.strftime('%Y-%m-%d')
    end = end.strftime('%Y-%m-%d')
    date_data = {
        "start": start,
        "end": end
    }
    #print(start, end) #TODO: print�ϴ� �׸���� ���� ������ return�Ǵ� ������ �켱 print�� �ʿ��� �׸�鸸 ���ܵξ����ϴ�!
    #return start, end
    return date_data
    # with open('extract_period_func.json', 'w', encoding='utf-8') as file:
    #     return json.dump(date_data, file)
    
def participant_show(df):
    df = df['User'].value_counts(dropna=True, sort=True)
    df = pd.DataFrame(df)
    df = df.reset_index()
    df.columns = ['User', 'Chat_counts']
    #print(df['User']) #TODO: print�ϴ� �׸���� ���� ������ return�Ǵ� ������ �켱 print�� �ʿ��� �׸�鸸 ���ܵξ����ϴ�!
    df_f=df['User']
    #print(df_f) #TODO: print�ϴ� �׸���� ���� ������ return�Ǵ� ������ �켱 print�� �ʿ��� �׸�鸸 ���ܵξ����ϴ�!
    return df_f.values
    # with open('participant_show_func.json', 'w', encoding='utf-8') as file:
    #     return df_f.to_json(file, force_ascii=False)

def chat_counts(df) :
    df = df['User'].value_counts(dropna=True, sort=True)
    df = pd.DataFrame(df)
    df = df.reset_index()
    df.columns = ['User', 'Chat_counts']
    df_f=df
    #print(df_f) #TODO: print�ϴ� �׸���� ���� ������ return�Ǵ� ������ �켱 print�� �ʿ��� �׸�鸸 ���ܵξ����ϴ�!
    return df_f.values
    # with open('chat_counts_func.json', 'w', encoding='utf-8') as file:
    #     return df_f.to_json(file, force_ascii=False)

def count_send_question(df):
    df = df[df['Message'].str.contains('\?')]
    df = df['User'].value_counts(dropna=True, sort=True)
    df = pd.DataFrame(df)
    df = df.reset_index()
    df.columns = ['User', 'count_send_question']
    df_f=df
    #print(df_f)
    return df_f.values
    # with open('count_send_question_func.json', 'w', encoding='utf-8') as file:
    #     return df_f.to_json(file, force_ascii=False)

def count_send_file(df):
    df = df[df['Message'].str.contains('����')]
    df = df['User'].value_counts(dropna=True, sort=True)
    df = pd.DataFrame(df)
    df = df.reset_index()
    df.columns = ['User', 'count_send_file']
    df_f=df
    #print(df_f)
    return df_f._values
    # with open('count_send_file_func.json', 'w', encoding='utf-8') as file:
    #     return df_f.to_json(file, force_ascii=False)

def count_send_picture(df):
    df = df[df['Message'].str.contains('����')]
    df = df['User'].value_counts(dropna=True, sort=True)
    df = pd.DataFrame(df)
    df = df.reset_index()
    df.columns = ['User', 'count_send_picture']
    df_f=df
    #print(df_f)
    return df_f._values
    # with open('count_send_picture_func.json', 'w', encoding='utf-8') as file:
    #     return df_f.to_json(file, force_ascii=False)

def num_of_user(df) :
    df = df['User'].value_counts(dropna=True, sort=True)
    df = pd.DataFrame(df)
    df = df.reset_index()
    df.columns = ['User', 'Chat_counts']
    num_of_user = len(df)
    #print(num_of_user)
    return num_of_user
    # num_of_user_data = {
    #     "num_of_user": num_of_user
    # }
    # with open('num_of_user_func.json', 'w', encoding='utf-8') as file:
    #     return json.dump(num_of_user_data, file)

def mean_of_message_len(df) :
    df_f=df.groupby(['User'])['length'].mean()
    #print(df_f)
    return df_f
    # with open('mean_of_message_len_func.json', 'w', encoding='utf-8') as file:
    #     return df_f.to_json(file, force_ascii=False)

def time_chat_counts(df) :
    df['24time_H']= df['24time'].astype(str)
    df['24time_H']=df['24time_H'].str[:2]
    df_f = df['24time_H'].value_counts()
    #print(df_f)
    return df_f
    # with open('time_chat_counts_func.json', 'w', encoding='utf-8') as file:
    #     return df_f.to_json(file, force_ascii=False)

# def merge_json():
#     result = []
#     for f in glob.glob("*.json"):
#         with open(f, "rb") as infile:
#             result.append(json.load(infile))

#     with open("merged_file.json", "wb") as outfile:
#         return json.dump(result, outfile)

# def merge_json():
#     result = []
#     for f in glob.glob("*.json"):
#         with open(f, "r", encoding="utf-8") as infile:
#             result.append(json.load(infile))

#     with open("merged_file.json", "w", encoding="cp949") as outfile:
#         json.dump(result, outfile)

if __name__ == '__main__':
    msg_list = read_kko_msg("kakao.txt")
    apply_kko_regex(msg_list)
    df = pd.read_csv("kko_regex.csv")

    df.Date = pd.to_datetime(df.Date)
    
    df["hour"] = df["Date"].apply(lambda x : x.hour)
    df["minute"] = df["Date"].apply(lambda x : x.minute)
    df["year"] = df['Date'].dt.strftime('%Y')
    df["month"] = df['Date'].dt.strftime('%m')
    df["day"] = df['Date'].dt.strftime('%d')
    df["weekday"] = df['Date'].dt.day_name()

    ## 24�ð��� ǥ��
    df["24time"] = df["Timetype"] + " " + df["Time"]
    df["24time"] = df["24time"].map(lambda x : x.replace("����","AM"))
    df["24time"] = df["24time"].map(lambda x : x.replace("����","PM"))

    temp = []
    transform_time = []
    for i in range(len(df)) :
        time = df["24time"][i]
        temp.append(dt.datetime.strptime(time,"%p %I:%M"))
        transform_time.append(temp[i].time())

    df["24time"] = transform_time

    ## ���� ��
    title_len = []

    for i in range(len(df)):
        ttl = len(df['Message'][i])
        title_len.append(ttl)

    df['length'] = title_len
    df.head()

    ## ���� ����
    quarter = []
    for i in range(len(df)) :
        a = int(df["month"][i])
        if a >= 1 and a <= 3 :
            quarter.append("1q")
        if a >= 4 and a <= 6 :
            quarter.append("2q")
        if a >= 7 and a <= 9 :
            quarter.append("3q")
        if a >= 10 and a <= 12 :
            quarter.append("4q")

    df["quarter"] = quarter
    
    # files=['extract_period_func.json','participant_show_func.json','chat_counts_func.json']

    #print('==========kakaotalk ����, ���� ��¥==========')
    date_data = {}
    date_data = extract_period(df) #TODO: return�� �޾Ƽ� ����
    #print('==========ä�ù��� ������ ��==========')
    participant_num = 0
    participant_num = num_of_user(df) #TODO: return�� �޾Ƽ� ����
    #print('==========������ ���==========')
    participant_list = {}
    participant_list = participant_show(df) #TODO: return�� �޾Ƽ� ����
    #print(json.dumps(participant_list))
    #print('==========�����ں� ä�� Ƚ��==========')
    participant_chat = {}
    participant_chat = chat_counts(df) #TODO: return�� �޾Ƽ� ����
    #print('==========�����ں� ���� ���� Ƚ��==========')
    participant_file = {}
    participant_file = count_send_file(df) #TODO: return�� �޾Ƽ� ����
    #print('==========�����ں� ���� ���� Ƚ��==========')
    participant_question = {}
    participant_question = count_send_question(df) #TODO: return�� �޾Ƽ� ����
    #print('==========�����ں� ���� ���� Ƚ��==========')
    participant_picture = {}
    participant_picture = count_send_picture(df) #TODO: return�� �޾Ƽ� ����
    #print('==========�����ں� ä�� ��� ����==========')
    #mean_of_message_len(df) #TODO: �� �Լ��� �ؿ� �Լ��� ���� �Լ����̶� �ٸ��� df�� ����ϴ� �����...? ���� �ٸ��Ű��Ƽ� ���� ���ǵ�Ⱦ��Ф�
    #print('==========�ð��뺰 ä�� �󵵼�==========')
    #time_chat_counts(df)
    # merge_json()

    #TODO: ��°�� �ѹ��� �ֱ����� analyze_result ����ü ����
    analyze_result = {}
    analyze_result = {
        'date_data': date_data,
        'participant_num': participant_num,
        'participant_list': participant_list,
        'participant_chat' :participant_chat,
        'participant_file' : participant_file,
        'participant_question' : participant_question,
        'participant_picture' : participant_picture
    }

    #TODO: json.dumps�� ��°�� json���·� return, ensure_ascii=False�ɼ��� �ѱ� ���ڵ����� �ɼ�, cls=NumpyEncoder�� ndarray�� jsonȭ �ϱ����� �ɼ�
    print(json.dumps(analyze_result, ensure_ascii=False, cls=NumpyEncoder))