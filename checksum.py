import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox, Button

UDP_list = [
    0b0110011001100000,
    0b0101010101010101,
    0b1000111100001100,
]


def checksum(num_list):
    check = 0
    for num in num_list:
        check += num
        if check >> 16 > 0:
            check -= 0xffff
    return 0xffff - check


textbox1 = TextBox(plt.axes([0.3, 0.8, 0.5, 0.075]), 'first 16-bit', initial=format(UDP_list[0], '016b'))
textbox2 = TextBox(plt.axes([0.3, 0.7, 0.5, 0.075]), 'second 16-bit', initial=format(UDP_list[1], '016b'))
textbox3 = TextBox(plt.axes([0.3, 0.6, 0.5, 0.075]), 'third 16-bit', initial=format(UDP_list[2], '016b'))
textbox4 = TextBox(plt.axes([0.3, 0.3, 0.5, 0.075]), 'checksum', initial='')
button = Button(plt.axes([0.3, 0.5, 0.4, 0.075]), "calculate")


def calculate(event):
    UDP_list[0] = int(textbox1.text, 2)
    UDP_list[1] = int(textbox2.text, 2)
    UDP_list[2] = int(textbox3.text, 2)
    textbox4.set_val(format(checksum(UDP_list), '016b'))
    textbox4.text_disp.set_color('blue')
    plt.draw()


button.on_clicked(calculate)
plt.show()
