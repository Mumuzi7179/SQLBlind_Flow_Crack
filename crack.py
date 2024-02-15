from extract import *
import re

def cracks(types):
    datas = open('data.txt').read()
    if(types == 0):
        data = time_crack(datas.replace(" ","").splitlines())
    else:
        data = bool_crack(datas.replace(" ","").splitlines())
    return data

def time_crack(datas):
    #第一种
    data1 = ''
    for i in range(len(datas) - 1):
        try:
            chat = re.search(r',(\d+),1\)\)',datas[i])
            next_chat = re.search(r',(\d+),1\)\)',datas[i+1])
            if(chat):
                chat = chat.group(1)
            if(next_chat):
                next_chat = next_chat.group(1)
            if(chat != next_chat):
                data = re.search(r'\)\)(<|>|=)(.*?),sleep',datas[i])
                if(data):
                    data = data.group(2)
                    if(data.isdigit() and int(data) > 32):
                        data = chr(int(data))
                try:
                    data1 += data
                except:
                    data1 += ' '
        except:
            continue
    #第二种
    data2 = ''
    for i in range(len(datas)):
        data = re.search(r'\)=(.*?),sleep', datas[i])
        if (data):
            data = data.group(1)
            if (data.isdigit() and int(data) > 32):
                data = chr(int(data))
        try:
            data2 += data
        except:
            pass
    #第三种第四种
    data3, data4 = ''.join(chr(ord(c) - 1) if c != ' ' else ' ' for c in data1), ''.join(
        chr(ord(c) + 1) if c != ' ' else ' ' for c in data1)
    output = [data1.lstrip(),data2.lstrip(),data3.lstrip(),data4.lstrip()]
    return output

def bool_crack(datas):
    data1 = ''
    for i in range(len(datas) - 1):
        try:
            chat = re.search(r'\)\),(\d+),',datas[i])
            next_chat = re.search(r'\)\),(\d+),',datas[i+1])
            if(chat):
                chat = chat.group(1)
            if(next_chat):
                next_chat = next_chat.group(1)
            if(chat != next_chat):
                data = re.search(r'\)(>|<|=)(.*?)(\)|\)\)|--+|#|HTTP|END)',datas[i])
                if(data):
                    data = data.group(2).replace("'", "").replace('"', "")
                    if(data.isdigit() and int(data) > 32):
                        data = chr(int(data))
                try:
                    data1 += data
                except:
                    data1 += ' '
        except:
            continue
    data2, data3 = ''.join(chr(ord(c) - 1) if c != ' ' else ' ' for c in data1), ''.join(
        chr(ord(c) + 1) if c != ' ' else ' ' for c in data1)
    data4 = ''
    for i in range(len(datas) - 1):
        try:
            chat = re.search(r'\),(\d+),',datas[i])
            next_chat = re.search(r'\),(\d+),',datas[i+1])
            if(chat):
                chat = chat.group(1)
            if(next_chat):
                next_chat = next_chat.group(1)
            if(chat != next_chat):
                data = re.search(r'\)(>|<|=)(.*?)(\)|\)\)|--+|#|HTTP|END)',datas[i])
                if(data):
                    data = data.group(2).replace("'", "").replace('"', "")
                    if(data.isdigit() and int(data) > 32):
                        data = chr(int(data))
                try:
                    data4 += data
                except:
                    data4 += ' '
        except:
            continue
    data5,data6,IS_LEN,IS_SET,LENS = '','',False,False,[]
    for i in range(len(datas)):
        LEN = datas[i].split('LENGTH')
        if(len(LEN) != 1):
            IS_LEN = True
            LENS.append(LEN[0])
    LENS = list(set(LENS))
    if(len(LENS) == 2):
        IS_SET = True
    if(IS_SET and IS_LEN):
        for i in range(len(datas) - 1):
            try:
                chat = re.search(r'\),(\d+),', datas[i])
                next_chat = re.search(r'\),(\d+),', datas[i + 1])
                if (chat):
                    chat = chat.group(1)
                if (next_chat):
                    next_chat = next_chat.group(1)
                if (chat != next_chat):
                    length = datas[i].split('LENGTH')[0]
                    data = re.search(r'\)(>|<|=)(.*?)(\)|\)\)|--+|#|HTTP|END)', datas[i])
                    if (data):
                        data = data.group(2).replace("'", "").replace('"', "")
                        if (data.isdigit() and int(data) > 32):
                            try:
                                if(length == LENS[0]):
                                    data5 += chr(int(data))
                                    data6 += chr(int(data)+1)
                                else:
                                    data5 += chr(int(data)+1)
                                    data6 += chr(int(data))
                            except:
                                pass
            except:
                continue

    output = [data1.lstrip(),data2.lstrip(),data3.lstrip(),data4.lstrip(),data5.lstrip(),data6.lstrip()]
    return output

def mains(pcap_file):
    jt = judgtype(pcap_file)
    extract(pcap_file)
    crack_data = cracks(jt)
    return crack_data
