# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import torch


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    x = torch.arange(4.0)
    print(x)
    print(x.requires_grad_(True))
    print(x.grad)
    y = 2 * torch.dot(x, x)
    #z = y*y
    print(y)
    print(y.requires_grad_(True))
    print(y.backward())
    print(x.grad)
    #print(z.backward())
    print(y.grad)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/

