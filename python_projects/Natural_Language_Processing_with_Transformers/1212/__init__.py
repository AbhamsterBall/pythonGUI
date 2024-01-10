from itertools import zip_longest

import torch.nn as nn
import torch.optim as optim
import torch

def train(x, y):
    input_size = 784  # Assuming the input size required by the model is 784

    # Generate random input data within the required range
    X = torch.randn(x, input_size)  # Creating random data with shape (x, 784)
    y = torch.empty(x, dtype=torch.float).random_(y) # 标签，来自官方文档

    model = nn.Sequential(
        nn.Linear(input_size, 200),
        nn.ReLU(),
        nn.Linear(200, 10)
    )
    loss_fn = nn.CrossEntropyLoss()
    optimizer = optim.SGD(model.parameters(), lr=0.01)

    # Assuming y is a tensor containing the target labels

    for epoch in range(10):
        for i in range(len(X)):

            y_pred = model(X[i])

            loss = loss_fn(y_pred, y) # Ensure y[i] has proper shape for CrossEntropyLoss
            print("epoch: {}, i: {}, loss: {}".format(epoch, i, loss.item())) # print loss

            # Before the backward pass, use the optimizer object to zero all of the
            # gradients for the variables it will update (which are the learnable weights
            # of the model)
            optimizer.zero_grad()

            loss.backward() # compute gradient of the loss
            optimizer.step() # let optimizer to update parameter

# print("hello")
def testPytorch():
    print(torch.rand(5, 3))

def pytorchExample():
    loss = nn.CrossEntropyLoss()
    input = torch.randn(3, 5, requires_grad=True)
    target = torch.empty(3, dtype=torch.long).random_(5)
    output = loss(input, target)
    output.backward()

def zip_logge():
    nested_list = [
        [1, 2, 3],
        [4, 5],
        [6]
    ]
    print(list(zip_longest(*nested_list)))

if __name__ == '__main__':
    # testPytorch()
    # train(10, 2)
    # pytorchExample()
    zip_logge()
