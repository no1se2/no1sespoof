import os
import time
import random
import string
from colorama import Fore, Style


os.system('clear')
spoof = ':'.join(random.choices(string.hexdigits, k=2) + random.choices(string.hexdigits, k=2) + random.choices(string.hexdigits, k=2) + random.choices(string.hexdigits, k=2) + random.choices(string.hexdigits, k=2) + random.choices(string.hexdigits, k=2))

print(Fore.BLUE + "shutting down wlan0!")
time.sleep(2)
os.system('ifconfig wlan0 down')
print(Fore.LIGHTYELLOW_EX + "Changing Mac Address now!")
time.sleep(2)
os.system('ifconfig wlan0 hw ether {}'.format(spoof))
time.sleep(2)
os.system('ifconfig wlan0 up')
print(Fore.GREEN + "Done!")
exit()
#Made By no1se GGGGGGGGGG