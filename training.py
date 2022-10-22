# File for training the model
import torch.optim as optim
from model import Net
import torch.nn as nn
import torch
from LettersDataset import trainloader

net = Net()

criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)


def train(epochs, trainloader):
    print("Beginning Training!")
    for epoch in range(epochs):  # loop over the dataset multiple times

        running_loss = 0.0
        for i, data in enumerate(trainloader, 0):
            # get the inputs; data is a list of [inputs, labels]
            inputs, labels = data
            if i % 100 == 0:
                print(i)
            # zero the parameter gradients
            optimizer.zero_grad()

            # forward + backward + optimize
            outputs = net(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            # print statistics
            running_loss += loss.item()
            if i % 200 == 199:    # print every 2000 mini-batches
                print(f'[{epoch + 1}, {i + 1:5d}] loss: {running_loss / 200:.3f}')
                running_loss = 0.0
        torch.save(net.state_dict(), './asl_net_' + str(epoch) + ".pth")
    print('Finished Training')


if __name__ == '__main__':
    epochs = 5
    train(epochs, trainloader=trainloader)
    PATH = './asl_net.pth'
    torch.save(net.state_dict(), PATH)
