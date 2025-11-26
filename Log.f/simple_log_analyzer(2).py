successfully = 0
failed = 0

with open('fake_logs.txt') as file:
    for line in file:
        if 'Failed' in line:
            failed += 1
        elif 'successfully' in line:
            successfully += 1

print(f'Successful count: {successfully}')
print(f'Fail count: {failed}')
