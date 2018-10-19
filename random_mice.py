import ctypes
from random import sample
from pprint import pformat

test_conditions = ['Saline', 'CNO', 'Baseline']

mice = {
    mouse: sample(test_conditions, len(test_conditions))
    for mouse in range(1, 11)
}

pretty_mice = ' ' + pformat(mice)[1:-1]


def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

	
Mbox('Random Mice Test Condition Results', pretty_mice, 1)