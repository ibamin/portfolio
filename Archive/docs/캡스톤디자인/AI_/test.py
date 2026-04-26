#Labeling Code
import os
import torch
import torch.nn as nn
import torchvision.transforms as transforms
from torchvision.datasets import ImageFolder
from torch.utils.data import DataLoader
import pandas as pd
import torchvision.models as models

# 모델 정의 (ResNet18 사용)
model = models.resnet18(pretrained=False)
num_ftrs = model.fc.in_features
model.fc = nn.Linear(num_ftrs, 2)

# 학습된 모델의 가중치를 로드합니다.
model_path = '/content/drive/MyDrive/imagemodel_best.pt'
model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))

# 디바이스 설정
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)

# 데이터 경로
data_root = '/content/drive/MyDrive/testdata'

# 데이터 전처리 및 로드
transform = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
])

dataset = ImageFolder(data_root, transform=transform)

# 데이터 로더 설정
data_loader = DataLoader(dataset, shuffle=False)

# 분류 결과 저장할 리스트
predictions = []
probabilities_list = []

# 모델을 평가 모드로 설정
model.eval()

# 이미지 분류 예측
with torch.no_grad():
    for images, _ in data_loader:
        images = images.to(device)

        # 모델을 통해 예측 수행
        outputs = model(images)
        probabilities = torch.softmax(outputs, dim=1)
        _, predicted = torch.max(outputs, 1)

        # 분류 결과 저장
        predictions.extend(predicted.cpu().numpy())
        probabilities_list.extend(probabilities.cpu().numpy())

# 분류 결과 출력
for i, prediction in enumerate(predictions):
    image_path = dataset.imgs[i][0]
    image_name = os.path.basename(image_path)
    label = 'Fake' if prediction == 0 else 'Real'
    probability = probabilities_list[i][prediction]  # 추가된 부분: 예측된 클래스에 해당하는 확률값 추출
    print(f'{image_name}: {label} (Probability: {probability})')

# 분류 결과를 데이터프레임으로 변환
results = pd.DataFrame({'idx': [os.path.basename(image_path) for image_path, _ in dataset.imgs],
                       'label': ['Fake' if prediction == 0 else 'Real' for prediction in predictions]})

# 결과를 엑셀 파일로 저장
output_path = '/content/drive/MyDrive/submit.csv'
results.to_csv(output_path, index=False)
