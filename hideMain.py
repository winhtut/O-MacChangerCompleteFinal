from hideMac import ChangeMac

if __name__ == "__main__":
    changemac = ChangeMac()
    print("System Mac Address:> ",changemac.get_mac("eth0"))
    print("We random choosen mac is>: ",changemac.default_mac())
    changedMacXx=changemac.change_system_mac("eth0",changemac.system_choosen_mac)
    print("We changed mac address is:>",changedMacXx)

