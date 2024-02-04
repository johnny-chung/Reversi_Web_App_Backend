import torch
import torch.nn as nn

class MyCNN(nn.Module):
    def __init__(self):
        super(MyCNN, self).__init__()
        
        self.conv1 = nn.Conv2d(1, 16, kernel_size=3, stride=1, padding=1)
        self.batch_norm1 = nn.BatchNorm2d(16)
        self.leaky_relu1 = nn.LeakyReLU(0.02)
        self.dropout1 = nn.Dropout(0.02)
        
        self.conv2 = nn.Conv2d(16, 64, kernel_size=3, stride=1, padding=1)
        self.batch_norm2 = nn.BatchNorm2d(64)
        self.leaky_relu2 = nn.LeakyReLU(0.02)
        self.dropout2 = nn.Dropout(0.02)

        self.conv3 = nn.Conv2d(64, 128, kernel_size=3, stride=1, padding=1)
        self.batch_norm3 = nn.BatchNorm2d(128)
        self.leaky_relu3 = nn.LeakyReLU(0.04)
        self.dropout3 = nn.Dropout(0.04)
        
        self.flatten = nn.Flatten()
        
        self.fc1 = nn.Linear(128 * 8 * 8, 2048)
        self.batch_norm_fc1 = nn.BatchNorm1d(2048)
        self.leaky_relu_fc1 = nn.LeakyReLU(0.1)
        self.tanh = nn.Tanh()

        self.dropout_fc1 = nn.Dropout(0.1)
        
        self.fc2 = nn.Linear(2048, 2)

    def forward(self, x):
        x = self.conv1(x)
        x = self.batch_norm1(x)
        x = self.leaky_relu1(x)
        x = self.dropout1(x)
        
        x = self.conv2(x)
        x = self.batch_norm2(x)
        x = self.leaky_relu2(x)
        x = self.dropout2(x)
        
        x = self.conv3(x)
        x = self.batch_norm3(x)
        x = self.leaky_relu3(x)
        x = self.dropout3(x)
        
        x = self.flatten(x)
        
        x = self.fc1(x)
        x = self.batch_norm_fc1(x)
        x = self.leaky_relu_fc1(x)
        x = self.dropout_fc1(x)
        
        x = self.fc2(x)
        
        return x