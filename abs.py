import re

txt = 'Nepal is a beautiful country with beautiful places.'

x = re.findall('Nepal', txt)
print(x)
if (x):
    print('yes there is a match')
else:
    print('no match')
