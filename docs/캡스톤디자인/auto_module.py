import torch
from torch.utils.data import Dataset
import torch.nn.functional as F
import pandas as pd
import torch.nn as nn
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import socketio
import threading
from queue import Queue
import json
import subprocess
from packet_capture import capture_packets

app = Flask(__name__)
sio = SocketIO(app, async_mode='threading')
cio = socketio.Client()

class MultiClassLogisticRegression(nn.Module):
    def __init__(self, input_dim, num_classes):
        super(MultiClassLogisticRegression, self).__init__()
        self.linear = nn.Linear(input_dim, num_classes)

    def forward(self, x):
        x = self.linear(x)
        return x

model_path = 'C:/python/baejoon/test_model_MCLogistic_21.pt'
loaded_model = torch.load(model_path)
input_dim = 21
num_classes = 5
model = MultiClassLogisticRegression(input_dim, num_classes)
model.load_state_dict(loaded_model)
model.eval()

def get_attack_name(class_index):
    attack_names = {
        1: "DoS GoldenEye",
        2: "DoS Hulk",
        3: "FTP-Patator",
        4: "SSH-Patator",
    }
    return attack_names.get(class_index, "Unknown")


global_dataframe = pd.DataFrame({
    ' Source IP': [],
    ' Destination Port': [],
})

def log_data(data):
    with open("log.txt", "a") as f:
        f.write(f"Malicious data: {data}\n")

def send_packet_log(log_data):
    cio.emit('data', log_data)

def add_firewall_rule(ip_address, port_number):
    # Windows Firewall with Advanced Security에 규칙 추가
    script = f'''
    New-NetFirewallRule -DisplayName "Block {ip_address}:{port_number}" -Direction Inbound -Action Block -Protocol TCP -LocalPort {port_number} -RemoteAddress {ip_address}
    '''
    subprocess.run(['powershell', '-Command', script], capture_output=True)

ip_port_list = []

@cio.event
def connect():
    print('Connected to server')

@cio.event
def disconnect():
    cio.emit('disconnect')
    print('Disconnected from server')

@cio.on('message')
def handle_message(data):
    print('Received message:', data)

def process_packets(queue):
    cio.connect('http://localhost:3000')

    while True:
        global_dataframe = queue.get()

        for i, data in enumerate(global_dataframe.values, start=1):
            inputs = torch.tensor(data, dtype=torch.float).unsqueeze(0)
            outputs = model(inputs)
            probabilities = F.softmax(outputs, dim=1)

            line_number = str(i)
            _, predicted_class = torch.max(probabilities, dim=1)
            percentage = probabilities[0, predicted_class] * 100
            class_index = predicted_class.item()
            class_name = get_attack_name(class_index)

            if class_index != 0 and percentage >= 0.5:
                print(f"Malware Sudden Attacked!\nAttack Type: {class_name}")
                log_data(class_name)
                print(f"{line_number}: {percentage.item():.2f}% ({class_name})")

                ip_address = global_dataframe.iloc[i-1][' Source IP']
                port_number = global_dataframe.iloc[i-1][' Destination Port']
                packet_log = {
                    "line_number": line_number,
                    "percentage": percentage.item(),
                    "class_name": class_name,
                    "ip_address": ip_address,
                    "port_number": port_number
                }
                send_packet_log(packet_log)

            if ip_port_list:
                for ip_port in ip_port_list:
                    ip_address, port_number = ip_port
                    add_firewall_rule(ip_address, port_number)
            
@app.route('/')
def index():
    sio.emit('connect')
    return render_template('index.html')

if __name__ == '__main__':
    queue = Queue()
    capture_thread = threading.Thread(target=capture_packets, args=(queue,))
    capture_thread.start()
    
    threading.Thread(target=process_packets, args=(queue,)).start()
    sio.run(app, port=3300)