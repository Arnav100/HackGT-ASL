import torch
from torchvision import datasets, transforms

trainpath = "/Users/manvirchahal/Downloads/archive/asl_alphabet_train"
testpath = "/Users/manvirchahal/Downloads/archive/asl_alphabet_test"

trainset = datasets.ImageFolder(
    trainpath, transform=transforms.ToTensor())
trainloader = torch.utils.data.DataLoader(
    trainset, batch_size=32, shuffle=True)

testset = datasets.ImageFolder(
    testpath, transform=transforms.ToTensor())
testloader = torch.utils.data.DataLoader(
    testset, batch_size=32, shuffle=True)
