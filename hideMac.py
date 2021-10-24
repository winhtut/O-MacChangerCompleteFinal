import random
import subprocess
import re #regular expression
import termcolor as color
# import random

class ChangeMac:
    def __init__(self):
        self.current_mac=""
        self.user_input_mac=""
        self.system_choosen_mac=""

    def get_mac(self,interface:"example eth0"):
        """ """ #docstring
        output=subprocess.run(["ifconfig" , interface],shell=False , capture_output=True)
        result=output.stdout.decode()

        regex_mac_pattern = r'ether\s[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}'
        regex=re.compile(regex_mac_pattern)
        serach_result=regex.search(result)

        if serach_result:
            self.current_mac=serach_result.group().split(" ")[1]
        else:
            print("[xxx]Regular Expression pattern compile error \n please check pattern")
        return self.current_mac

    def default_mac(self)->"This function will return random choosen mac add":
        defaultMac=["2C:54:91:88:C9:E3","3D:54:91:88:C9:E3","2E:54:91:88:C9:E3","4C:54:91:88:C9:E3","5C:54:91:88:C9:E3"]
        count=0
        for i in defaultMac:
            count = count+1
            print(color.colored("[+{0}] {1}".format(count , i),'green'))
        state=int(input(color.colored("Press 1 to use our default mac address or \n Press 2 to user your own mac:",'yellow')))
        if state==2:
            self.user_input_mac=input("please enter your mac>:")
        else:
            list_index_randInput=len(defaultMac)-1
            mac_list=random.randint(0,list_index_randInput)
            rand_choosen_mac = defaultMac[mac_list]

            original_mac=self.get_mac("eth0")
            if original_mac == rand_choosen_mac:
                mac_list=mac_list+1
                if mac_list == len(defaultMac)-1:
                    mac_list=0
                    random_mac = defaultMac[mac_list]
                    self.system_choosen_mac=random_mac
            else:
                random_mac = defaultMac[mac_list]
                self.system_choosen_mac=random_mac

        return self.system_choosen_mac

    def change_system_mac(self,interface:"example=eth0",new_mac:"mac address")->"Change mac address":

        output=subprocess.run(["ifconfig", interface,"down"], shell=False, capture_output=True)
        print(output.stdout.decode())

        output = subprocess.run(["ifconfig", interface, "hw","ether",new_mac], shell=False, capture_output=True)
        print(output.stdout.decode())

        output = subprocess.run(["ifconfig", interface, "up"], shell=False, capture_output=True)
        print(output.stdout.decode())

        return self.get_mac(interface)












