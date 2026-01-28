#!/usr/bin/env python
# coding: utf-8

# In[2]:


from scapy.all import *
import pandas as pd
from statistics import stdev

# 전역 데이터프레임
global_dataframe = pd.DataFrame()

# 데이터 전처리 함수 정의
def preprocess_packet(packet):
    if IP in packet and TCP in packet:
        src_ip = packet[IP].src
        dst_port = packet[TCP].dport
        total_length_fwd_packets = packet[IP].len
        total_length_bwd_packets = packet[IP].len
        fwd_packet_length_max = packet[IP].len
        fwd_packet_length_mean = packet[IP].len
        bwd_packet_length_max = packet[IP].len
        bwd_packet_length_mean = packet[IP].len
        flow_iat_max = packet[IP].len
        bwd_header_length = packet[IP].ihl * 32 // 8
        bwd_packets_per_sec = packet[IP].len
        max_packet_length = packet[IP].len
        packet_length_mean = packet[IP].len
        packet_length_std = packet[IP].len
        packet_length_var = packet[IP].len
        avg_packet_size = packet[IP].len
        avg_fwd_segment_size = packet[IP].len
        avg_bwd_segment_size = packet[IP].len
        subflow_bwd_packets = packet[IP].len
        subflow_bwd_bytes = packet[IP].len
        init_win_bytes_forward = packet[TCP].window
        init_win_bytes_backward = packet[TCP].window

        # 전처리한 데이터를 딕셔너리로 반환
        preprocessed_data = {
            ' Source IP': src_ip,
            ' Destination Port': dst_port,
            'Total Length of Fwd Packets': total_length_fwd_packets,
            ' Total Length of Bwd Packets': total_length_bwd_packets,
            ' Fwd Packet Length Max': fwd_packet_length_max,
            ' Fwd Packet Length Mean': fwd_packet_length_mean,
            'Bwd Packet Length Max': bwd_packet_length_max,
            ' Bwd Packet Length Mean': bwd_packet_length_mean,
            ' Flow IAT Max': flow_iat_max,
            ' Bwd Header Length': bwd_header_length,
            ' Bwd Packets/s': bwd_packets_per_sec,
            ' Max Packet Length': max_packet_length,
            ' Packet Length Mean': packet_length_mean,
            ' Packet Length Std': packet_length_std,
            ' Packet Length Variance': packet_length_var,
            ' Average Packet Size': avg_packet_size,
            ' Avg Fwd Segment Size': avg_fwd_segment_size,
            ' Avg Bwd Segment Size': avg_bwd_segment_size,
            ' Subflow Bwd Packets': subflow_bwd_bytes,
            ' Subflow Bwd Bytes': subflow_bwd_bytes,
            'Init_Win_bytes_forward': init_win_bytes_forward,
            ' Init_Win_bytes_backward': init_win_bytes_backward
        }
        return preprocessed_data
    else:
        return None

# 패킷 캡처 및 데이터프레임 업데이트 함수
def capture_packets():
    global global_dataframe
    pkts = sniff(timeout=None, filter="ip and tcp")
    pkt_data = []
    for packet in pkts:
        preprocessed_data = preprocess_packet(packet)
        if preprocessed_data is not None:
            pkt_data.append(preprocessed_data)
    columns = [' Source IP',' Destination Port','Total Length of Fwd Packets',
               ' Total Length of Bwd Packets', ' Fwd Packet Length Max', ' Fwd Packet Length Mean',
               'Bwd Packet Length Max', ' Bwd Packet Length Mean', ' Flow IAT Max', ' Bwd Header Length',
               ' Bwd Packets/s', ' Max Packet Length', ' Packet Length Mean', ' Packet Length Std',
               ' Packet Length Variance', ' Average Packet Size', ' Avg Fwd Segment Size',
               ' Avg Bwd Segment Size', ' Subflow Bwd Packets',' Subflow Bwd Bytes',
               'Init_Win_bytes_forward', ' Init_Win_bytes_backward']
    global_dataframe = pd.DataFrame(pkt_data, columns=columns)

# 데이터프레임 반환 함수
def get_dataframe():
    return global_dataframe

# 패킷 캡처 및 데이터프레임 생성
capture_packets()

# 데이터프레임 확인
print(global_dataframe.head())

# 데이터프레임을 엑셀 파일로 저장(패킷이 잘나오나 확인)
global_dataframe.to_excel('packet_data.xlsx', index=False)


# In[ ]: