import math

# Function to generate decimals of π up to `n` places
def generate_pi_decimals(n):
    pi_str = f"{math.pi:.{n}f}"
    decimals = [int(digit) for digit in pi_str if digit.isdigit()]
    return decimals

# Generate π decimals
pi_decimals = generate_pi_decimals(100)  # Up to the 100th decimal
print(f"First 100 decimals of π: {pi_decimals}")

import torch
import torch.nn as nn
import torch.optim as optim

# Define a single block (sub-network)
class VerticalBlock(nn.Module):
    def __init__(self, input_size, output_size, pi_value):
        super(VerticalBlock, self).__init__()
        self.fc1 = nn.Linear(input_size, output_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(output_size, output_size)
        # Initialize weights based on π decimals
        self._initialize_weights(pi_value)
    
    def _initialize_weights(self, pi_value):
        with torch.no_grad():
            for param in self.parameters():
                param.uniform_(-pi_value, pi_value)
    
    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

# Define the vertical neural network
class VerticalNetwork(nn.Module):
    def __init__(self, num_blocks, input_size, block_size):
        super(VerticalNetwork, self).__init__()
        self.blocks = nn.ModuleList([
            VerticalBlock(input_size if i == 0 else block_size, block_size, pi_decimals[i % len(pi_decimals)] / 10.0)
            for i in range(num_blocks)
        ])
        self.fc_final = nn.Linear(block_size, 1)  # Final layer for output
    
    def forward(self, x):
        for block in self.blocks:
            x = block(x)
        return self.fc_final(x)

# Parameters
num_blocks = 10  # Number of vertical blocks
input_size = 5  # Input features
block_size = 20  # Size of each block
learning_rate = 0.001
epochs = 100

# Generate random data for training
inputs = torch.randn(100, input_size)  # 100 samples, 5 features each
targets = torch.randn(100, 1)  # 100 target outputs

# Instantiate the model
model = VerticalNetwork(num_blocks, input_size, block_size)
criterion = nn.MSELoss()  # Mean Squared Error Loss
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

# Training loop
for epoch in range(epochs):
    optimizer.zero_grad()
    outputs = model(inputs)
    loss = criterion(outputs, targets)
    loss.backward()
    optimizer.step()
    
    if (epoch + 1) % 10 == 0:
        print(f"Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}")
