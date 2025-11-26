import re
import numpy as np

with open('fake_logs.txt') as file:
    successfully = 0
    failed = 0

    for x in file:
        words = x.split()
        for key in words:
            if key == 'successfully':
                successfully += 1
            elif key == 'Failed':
                failed += 1
            
    print(f'Successful count: {successfully}')
    print(f'Failed count: {failed}')
