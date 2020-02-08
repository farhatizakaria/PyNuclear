# Importing functions
from numpy import log # Ln function
from math import * # import any functions from math library
from time import sleep # do you know what ? I love make my programs sleep
from packages import constants as const # Import constants



class Nuclear():
    """ The main class including the essential functions for studying a nuclide """

    def __init__(self):
        print("Welcome To Petron, I'm here to help you study any nuclide :) \n")
        print("Starting ...")
        sleep(4) # Waiting for 4 seconds

        #Let's get the data from user
        self.name = str(input("What is the name of your nuclide ")) # A name of the nuclide :)
        self.nuclides = int(input("What is the number of nuclides ")) # The number A
        self.protons = int(input("Also the number of the protons ")) # The number Z
        self.neutrons = int(self.nuclides - self.protons) # Yeb it's a good line to get the neutrons values

        # So the program finish taking data from user :p

    def mass_deficiency(self):
        """ A method for calculating the value of Mass Deficiency """

        nuclide_mass = float(input("Please write the nuclide mass "))
        mass_deficiency = float(self.protons * const.proton_mass + self.neutrons * const.neutron_mass) - nuclide_mass
        print("So the mass deficiency ", format(mass_deficiency,'.5f'))
        

    def bonding_energy(self):
        """ Looking for bonding energy ! """
        nuclide_mass = float(input("Please write the nuclide mass to get the bonding energy ")) # From the user
        bonding_energy = float((self.protons * const.proton_mass + self.neutrons * const.neutron_mass) - nuclide_mass) * const.u
        print("The energy of bonding is ",format(bonding_energy,'5f')," MeV")

    def bonding_energy_one_nucleus(self):
        """ What about for one nucleus """
        bonding_energy = float(input("Write the value of bonding energy "))
        E = float(bonding_energy / self.nuclides) # The value of binding energy of one nucleus
        print("So the bonding energry for one nucleus is ", format(E,'.2f')," MeV /Nucleus ")
        

    def stability_nucleus(self):
        """ For know if the nucleus is stable or no """
        nuclide1_name = str(input("What's the name of the first nuclide "))
        nuclide1_be = float(input("Give me the value of bonding energy for the nuclide 1 "))
        nuclide2_name = str(input("What's the name of the second nuclide "))
        nuclide2_be = float(input("Also of the value of bonding energy for the nuclide 2"))

        if nuclide1_be > nuclide2_be:
            print(nuclide1_name," more stable than ",nuclide2_name)
            sleep(1)
            print("That's mean ",nuclide2_name, " is a radioactive nucleus")

        else:
            print(nuclide2_name, " more stable than ", nuclide1_name)
            sleep(2)
            print("That's mean ",nuclide1_name, " is a radioactive nucleus")

    def radioactivity(self):
        """ The most important method """
        print("So I can help you to know the radioactivity ...\n")
        sleep(2)
        if self.nuclides > 100: # That's mean that nucleus is too heavy
            print("You have the radioactivity ALPHA")
            print("And the nuclide generated Y has: ")
            print(self.nuclides - 4," of nuclides")
            print(self.protons - 2," of protons \n")
            print("Plus the Helium A=4 Z=2 ")

        elif self.neutrons > self.protons:
            print("You have the radioactivity BETA -")
            print("The nuclide generated Y has: ")
            print(self.nuclides, " of nuclides")
            print(self.nuclides + 1, " of protons \n")
            print("Plus an electron -e")

        elif self.neutrons < self.protons:
            print("You have the radioactivity BETA +")
            print("The nuclide generated Y has: ")
            print(self.nuclides, " of nuclides")
            print(self.nuclides - 1, " of protons \n")
            print("Plus a positron +e")

        else:
            print("May be your nuclide is stable or you have the radioactivity GAMMA :/ ")

    def Fragmentation_nucleus(self):
        """ The energy from fragmentation of nucleus """
        print("Here I can also help you to know the energy generated by the fragmentation of part of the nucleus \n")
        sleep(2)
        print("1- the fragmentation of (mol) from the nuclide of ",self.name)
        print("2- the fragmentation of (g) from the nuclide of ",self.name)



        fragmentation_option = int(input("Write your option: "))
        if fragmentation_option == 1:
            mol_quantity = float(input("How many moles of the break-up of carbon nuclide ? "))
            nuclear_energy = float(input("give me the value of the nuclear energy ? "))

            ef = float(mol_quantity * const.NA * nuclear_energy)
            print("So the energy of the fragmentation of ",mol_quantity," mol from ",self.name," is ",ef)

        elif fragmentation_option == 2:
            g_quantity = int(input("How many grams of fragmentation of carbon nuclide ? "))
            nuclear_energy = float(input("give me the value of the nuclear energy  ? "))

            ef = float(((g_quantity * const.NA) / self.nuclides) * nuclear_energy)
            print("So the energy of the fragmentation of ",g_quantity," gram from ",self.name," is ",ef)

        else:
            print("You may chose a wrong option! check what did you do last commands! ")

    def decreasing_radiation(self):
        """ STILL UNDER-DEVELOPMENT !!!! IF THERE'S ANY ERROR CREATE AN ISSUE! """
        halflife = float(input("Please give me the value of halflife "))
        N = float(input("alse the number of remaining cores "))
        t = float((-log(N) * halflife) / log(2))
        print("So the the time required to break up the nucleus is ",t)
        
        print("Looking for lambda ...")
        sleep(3) #Just to make the scipt wait for a 3 seconds
        constant_decreasing_raditation = float(log(2)/halflife)
        print("Also the value of lambda is", constant_decreasing_raditation)
        sleep(2) #Just to make the scipt wait for a 3 seconds
        print("Looking for the time constant Tho")
        sleep(2) #Just to make the scipt wait for a 2 seconds
        time_constant = float(1/constant_decreasing_raditation)
        print("The value of time constant is ",time_constant)








nuclide = Nuclear() #New nuclide which we study it




def command():
    """ the main function """
    print("After I get the main data about the nuclide! I'm ready for the commands ")
    # Let's creat a guide list
    print("1 - mass defect")
    print("2 - binding energy")
    print("3 - binding energy for one nucleus")
    print("4 - radiocativity")
    print("5 - fragmentation of nucleus")
    print("6 - decreasing radiation ")
    print("7 - stability")
    cmnd = int(input(">>> "))
    if cmnd == 1:
        nuclide.mass_deficiency()
    elif cmnd == 2:
        nuclide.bonding_energy()
    elif cmnd == 3:
        nuclide.bonding_energy_one_nucleus()

    elif cmnd == 4:
        nuclide.radioactivity()

    elif cmnd == 5:
        nuclide.Fragmentation_nucleus()

    elif cmnd == 6:
        nuclide.decreasing_radiation()

    elif cmnd == 7:
        nuclide.stability_nucleus()

    else:
        print("You may chose a wrong option! ")

        #May be the user will think to retry so let's write some lines about that
        yes_list = ["Yes","yes","Y","y","Yeah","yeah"]
        ask_retry = str(input("You wanna to retry ?"))
        if ask_retry in yes_list:
            command()


if __name__ == "__main__": command()
