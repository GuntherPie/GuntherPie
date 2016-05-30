import os
from time import sleep

mydevices = ['', '']

while True:

    print "### Scanning for nearby devices ###"

    for device in mydevices:
        dev_name = os.popen('hcitool name %s'%(device)).read()
        if dev_name is not None and len(dev_name) > 0:
                print '%s is around'%(dev_name)

        sleep(2)