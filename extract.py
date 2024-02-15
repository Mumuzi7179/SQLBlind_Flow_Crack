import pyshark
from urllib.parse import unquote

def judgtype(pcap_file):
    #判断时间盲注 or Bool盲注(= or <>);只对GET类型有效
    ty = 255
    packets = pyshark.FileCapture(pcap_file, display_filter='http')
    for packet in packets:
        try:
            if('HTTP' in packet and 'GET' in packet.http.request_method):
                chat = unquote(packet.http.chat).replace(" ", "")
                if("sleep(" in chat):
                    ty = 0
                    break
                elif("1,1)" in chat):
                    ty = 1
                    break
                else:
                    pass
        except:
            continue
    packets.close()
    return ty

def extract(pcap_file):
    f = open("data.txt",'w')
    packets = pyshark.FileCapture(pcap_file, display_filter='http')
    count = 0
    for packet in packets:
        try:
            if ('HTTP' in packet):
                res = unquote(packet.http.response_for_uri)
                length = len(packet.http.file_data)
                f.write(str(length)+'LENGTH'+res+'END'+'\n')
        except:
            continue
        count += 1
    packets.close()

