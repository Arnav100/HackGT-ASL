import torch
from torchvision import datasets, transforms

trainpath = ""
testpath = ""

trainset = datasets.ImageFolder(
    trainpath, transform=transforms.transform)
trainloader = torch.utils.data.DataLoader(
    trainset, batch_size=32, shuffle=True)

testset = datasets.ImageFolder(
    testpath, transform=transforms.transform)
testloader = torch.utils.data.DataLoader(
    testset, batch_size=32, shuffle=True)
