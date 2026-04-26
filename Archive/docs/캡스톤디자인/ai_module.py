import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import f1_score
import time

start = time.time()

# 구글 드라이브 마운트
from google.colab import drive
drive.mount('/content/drive')

# 첫 번째 데이터 로드
df1 = pd.read_csv('/content/drive/MyDrive/Dataset/MachineLearningCSV/MachineLearningCVE/Tuesday-WorkingHours.pcap_ISCX.csv')

# 두 번째 데이터 로드
df2 = pd.read_csv('/content/drive/MyDrive/Dataset/MachineLearningCSV/MachineLearningCVE/Wednesday-workingHours.pcap_ISCX.csv')

# 두 데이터셋을 병합
df = pd.concat([df1, df2])

# infinity 값을 NaN으로 변환
df.replace([np.inf, -np.inf], np.nan, inplace=True)

# NaN 값이 있는 행 제거
df.dropna(inplace=True)

# feature와 class 나누기
X = df[[' Destination Port', 'Total Length of Fwd Packets',
       ' Total Length of Bwd Packets', ' Fwd Packet Length Max',
       ' Fwd Packet Length Mean', 'Bwd Packet Length Max',
       ' Bwd Packet Length Mean', ' Flow IAT Max', ' Bwd Header Length',
       ' Bwd Packets/s', ' Max Packet Length', ' Packet Length Mean',
       ' Packet Length Std', ' Packet Length Variance', ' Average Packet Size',
       ' Avg Fwd Segment Size', ' Avg Bwd Segment Size',
       ' Fwd Header Length.1', ' Subflow Bwd Packets', ' Subflow Bwd Bytes',
       'Init_Win_bytes_forward', ' Init_Win_bytes_backward']]
y = df[' Label'].values

# 데이터프레임 일부 데이터 예시 출력
print(df.head())

# 데이터프레임 크기 확인
print("데이터프레임 크기:", df.shape)

# 데이터프레임 열 정보 출력
print(df.info())

# 데이터 전처리
scaler = StandardScaler()
X = scaler.fit_transform(X)
le = LabelEncoder()
y = le.fit_transform(df[' Label'])

# 학습 데이터와 검증 데이터 분리
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# 모델 정의
class MultiClassLogisticRegression(nn.Module):
    def __init__(self, input_dim, num_classes):
        super(MultiClassLogisticRegression, self).__init__()
        self.linear = nn.Linear(input_dim, num_classes)

    def forward(self, x):
        x = self.linear(x)
        return x

model = MultiClassLogisticRegression(input_dim=X_train.shape[1], num_classes=len(le.classes_))

# 손실 함수와 옵티마이저 정의
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# 배치 크기 지정
batch_size = 128

# 모델 학습
num_epochs = 100

for epoch in range(num_epochs):
    for i in range(0, len(X_train), batch_size):
        inputs = torch.tensor(X_train[i:i+batch_size], dtype=torch.float32)
        labels = torch.tensor(y_train[i:i+batch_size], dtype=torch.long)

        optimizer.zero_grad()

        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()

        optimizer.step()

    if (epoch+1) % 10 == 0:
        with torch.no_grad():
            inputs = torch.tensor(X_train, dtype=torch.float32)
            labels = torch.tensor(y_train, dtype=torch.long)

            outputs = model(inputs)
            predicted = torch.argmax(outputs, dim=1)
            accuracy = (predicted == labels).sum().item() / len(labels)
            train_loss = loss.item()

            print(f"Epoch [{epoch+1}/{num_epochs}], Train Loss: {train_loss:.8f}, Accuracy: {accuracy*100:.2f}%")

with torch.no_grad():
    inputs = torch.tensor(X_val, dtype=torch.float32)
    labels = torch.tensor(y_val, dtype=torch.long)

    outputs = model(inputs)
    predicted = torch.argmax(outputs, dim=1)
    accuracy = (predicted == labels).sum().item() / len(labels)

    # 레이블 디코딩
    predicted_labels = le.inverse_transform(predicted)
    true_labels = le.inverse_transform(labels)

    print('Accuracy: {:.2f}%'.format(accuracy * 100))
    print('Time:', time.time() - start)

    # 예측된 레이블과 실제 레이블을 패킷마다 출력
    for i in range(len(predicted_labels)):
        print(f"Packet {i+1}: Predicted Label - {predicted_labels[i]}, True Label - {true_labels[i]}")

    # 클래스와 레이블 값 출력
    for i in range(len(le.classes_)):

        print(f"Class {i}: Label - {le.classes_[i]}")

# 모델 저장
torch.save(model.state_dict(), '/content/drive/MyDrive/MCLogistic.pt')