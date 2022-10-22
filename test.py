from model import Net
import torch
from LettersDataset import testloader


classes = [c for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
classes.append("space")
classes.append("del")
classes.append("nothing")


def test(net, testloader):
    # prepare to count predictions for each class
    correct_pred = {classname: 0 for classname in classes}
    total_pred = {classname: 0 for classname in classes}

    # again no gradients needed
    with torch.no_grad():
        for data in testloader:
            images, labels = data
            # print(labels)
            outputs = net(images)
            _, predictions = torch.max(outputs, 1)
            # collect the correct predictions for each class
            for label, prediction in zip(labels, predictions):
                if label == prediction:
                    correct_pred[classes[label]] += 1
                total_pred[classes[label]] += 1

    # print accuracy for each class
    for classname, correct_count in correct_pred.items():
        if total_pred[classname] != 0:
            accuracy = 100 * float(correct_count) / total_pred[classname]
            print(f'Accuracy for class: {classname:5s} is {accuracy:.1f} %')
            print(correct_count)
            print(total_pred[classname])
        else:
            print("No predictions for " + str(classname) +
                  ", should be " + str(correct_count))


if __name__ == '__main__':
    PATH = './asl_net.pth'
    net = Net()
    net.load_state_dict(torch.load(PATH))
    test(net, testloader=testloader)
