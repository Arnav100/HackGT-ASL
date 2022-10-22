import torch
from torchvision import datasets, transforms
import matplotlib.pyplot as plt
import numpy as np
import torch.utils.data as dta


trainpath = "/Users/manvirchahal/Downloads/archive/asl_alphabet_train/asl_alphabet_train"
testpath = "/Users/manvirchahal/Downloads/archive/asl_alphabet_test"

trainset = datasets.ImageFolder(
    trainpath, transform=transforms.ToTensor())
testsize = int(len(trainset)*0.1)
trainsize = int(len(trainset)*0.9)

trainset, testset = dta.random_split(
    trainset, [trainsize, testsize], generator=torch.Generator().manual_seed(42))
trainloader = torch.utils.data.DataLoader(
    trainset, batch_size=32, shuffle=True)

# testset = datasets.ImageFolder(
#     testpath, transform=transforms.ToTensor())
testloader = torch.utils.data.DataLoader(
    testset, batch_size=32, shuffle=True)
print(trainset.dataset.class_to_idx)
print(testset.dataset.class_to_idx)
# for images, labels in trainloader:
#     print(labels)
#     # plt.imshow(np.transpose(images[0].numpy(), (1, 2, 0)))
#     # plt.show()
#     break
