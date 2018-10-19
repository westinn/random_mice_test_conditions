# random_mice_test_conditions
Small script for randomizing order of test conditions on mice/rats.

Used PyInstaller to generate exe.
`pyinstaller --onefile --windowed random_mice.py`

```python
import ctypes
from random import sample
from pprint import pformat

test_conditions = ['Saline', 'CNO', 'Baseline']

# Dictionary comprehension taking random sample of conditions to shuffle and return new list for each mouse
# random.shuffle randomizes inplace vs random.sample(list, len(list)) which returns new list
mice = {
    mouse: sample(test_conditions, len(test_conditions))
    for mouse in range(1, 11)
}

# Format and then remove extra spaces for better readability when outputing to popup window
pretty_mice = ' ' + pformat(mice)[1:-1]


# Defining popup window
def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)
    

# Actual popup window, passing (title, text, style)
Mbox('Random Mice Test Condition Results', pretty_mice, 1)
```
