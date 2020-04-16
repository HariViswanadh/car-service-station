import time
from tkinter import *
import tkinter.messagebox

debt = 0

def Maintenance():
    global debt
    """
    G - Good
    B - Bad
    W - Worn Out
    NR - Needs Replacement
    NM - Needs Maintenance

    Inspect your vehicle - Category | Indication    0   1   2

    different warning signal indicators             G    W  NR                      
    tire pressure                                   G    B                     
    check tread depth                               G    B  NR
    rotate tires and alignment                      G    NM
    clean break                                     G    W  NR
    check oil levelds                                G    NR
    engine coolant level                            G    NR
    engine air filter                               G    NR
    spark plugs                                     G    NR
    octane rating(fuel)     -       A rating from 0 to 100

    """
    print("0  : Good", "1 :  Bad/Worn Out"," 2 : Needs Replacement")

    #Lists containing the various categories of the parameters for the car health indication
    param_3_list = ["Lights", "Engine", "Breaks","Tire", "Tire Rotation", "Coolant", "Air Filter", "Indicators"]
    param_3_dict = {0:"Good", 1:"Bad/Worn Out", 2: "Needs Replacement"}
    

    good_condition = []
    bad_condition = []
    replacement_condition = []
    other_condition = []


    print("Enter the rating from the self analysis of the car")
    #Selecting Inputs from user and taking action accordingly
    maintenance_car_rating  = []

    for ele in param_3_list:
        maintenance_car_rating.append(int(input("Q > "+ele+": ")))
        if maintenance_car_rating[-1] == 0:
            good_condition.append(ele)
        elif maintenance_car_rating[-1] == 1:
            bad_condition.append(ele)
        elif maintenance_car_rating[-1] == 2:
            replacement_condition.append(ele)
        else:
            other_condition.append(ele)
    
    maintenance_car_rating.append(int(input("Q > Octane rating : ")))

    #print(maintenance_car_rating)

    print("Parts in Good condition")
    if len(good_condition) > 0:
        for ele in good_condition:
            print(ele)
    else:
        print("None")
    print("\n" * 2)

    print("Parts in Bad/Worn Out condition")
    if len(bad_condition) > 0:
        for ele in bad_condition:
            print(ele)
    else:
        print("None")
    print("\n" * 2)
    
    print("Parts in Replacement/Maintenance condition")
    if len(replacement_condition) > 0:
        for ele in replacement_condition:
            print(ele)
    else:
        print("None")
    print("\n" * 2)
    
    
    #Maintenance rating
    maintenance_rating = 0
    #Checking oil and Octane rating
    if maintenance_car_rating[-1] <= 50:
        #Chekcing Oil levels
        if maintenance_car_rating[5] == 0:
            print("The car needs an Oil Maintenance")
            maintenance_rating += 1
        else:
            print("The car needs a replacement of Oil")
            maintenance_rating += 2
    elif 50 < maintenance_car_rating[-1] <= 80:
        if maintenance_car_rating[5] == 0:
            print("The car is in good condition")
        else:
            print("The car needs an Oil Maintenance")
            maintenance_rating += 1
    else:
        print("The car is in good condition")

    #Checking Engine condition
    #If engine coolant level needs replacement, then the air filter needs replacement too
    if maintenance_car_rating[6] == 1:
        print("Your Engine needs to be repaired")
        maintenance_rating += 2
    if maintenance_car_rating[7] == 1:
        print("Clean your engine air filter")
        maintenance_rating += 1
    
    if maintenance_car_rating[1] == 0 and maintenance_car_rating[3] == 0:
        print("Your Tires are in good condition")
    elif maintenance_car_rating[1] in [1, 2]:
        if maintenance_car_rating[3] == 1:
            maintenance_rating += 2
        if maintenance_car_rating[4] == 1:
            maintenance_rating += 2
        print("Your tires need to be replaced")

    #Calling Repair function and sending the bad_condition list to be repaired
    RepairM(bad_condition, replacement_condition, maintenance_rating)

    


def RepairM(bad_condition, replacement_condition, maintenance_rating):
    global debt
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("\nThe following parts have been repaired")
    print("\n".join(bad_condition))
    
    print("\nThe following parts have been replaced")
    print("\n".join(replacement_condition))
    
    print("\n**The car is repaired and is in good condition like a new one**")
    print(("Total Cost    " + str(maintenance_rating * 20)).center(100) )
    debt += maintenance_rating * 20

    menu()
    

def Wash():
    global debt
    wash_model = input("Q > Model Name : ")
    cheap_models = ['Maruti', 'breeza', 'Nano', 'hyundai']
    expensive_models = ['Audi', 'Merc', 'rollsroyce']
    
    print('The car wash is booked')

    if wash_model in cheap_models:
        print(("Total Cost    : 500" ).center(100) )
        debt += 500
    elif wash_model in expensive_models:
        print(("Total Cost    : 1000" ).center(100) )
        debt += 1000
    else:
        print(("Total Cost    : 800" ).center(100) )
        debt += 800

    menu()
    


def Repaint():
    global debt
    repaint_area = (input("Q> enter the area : "))
    repaint_cm = int(input("Q > Enter the area to be painted : "))
    print("\nThe car is painted")
    debt += repaint_cm * 40
    menu()
    


def Breakdown():
    """
    Problems in Car breakdowns
    Faulty Battery**
    Engine Problems
    Transmission Trouble
    Brake Trouble
    Damaged Tyres/Wheels
    Alternator faults*
    Fuel Problems*
    Clutch cables
    """ 
    print("This is the Breakdown Analysis system")
    print("++++++++++++++++++++++++++++++++++++++++++")
    print("Enter the input as per query with a y/n ")

    problems_list = []
    
    breakdown_usr_input = input("Q > Is the engine indicator red? ")
    if breakdown_usr_input == 'y':
        problems_list.append("indicator Red")

    breakdown_usr_input = input("Q > Are the headlights working? ")
    if breakdown_usr_input == 'n':
        problems_list.append("Headlights")

    breakdown_usr_input = input("Q > Is the engine switching on? ")
    if breakdown_usr_input == 'n':
        problems_list.append("Engine")

    breakdown_usr_input = input("Q > Are the brakes working? ")
    if breakdown_usr_input == 'n':
        problems_list.append("Brake")

    analysis_list = []
    #Backward Chaining
    if "indicator Red" in problems_list and "Headlights" in problems_list:
        analysis_list.append("The battery is damaged and need to be replaced")
        if "Engine" in problems_list:
            analysis_list.append("There is an alternator fault")
    
    if "Engine" in problems_list:
        if "There is an alternator fault" not in analysis_list:
            analysis_list.append("There is a starter motor problem")
    
    if "Brake" in problems_list:
        analysis_list.append("There is a problem with brakes")
    
    print("The following problems are diagnosed in the car".center(100))
    print("\n->".join(analysis_list))
    print("The SOS team is called")
    SOS()

    #menu()
    pass



def SOS():
    
    print("Calling for SOS help")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("\n")
    print("Service available at chennai:")
    print("1.shollinganallur")
    print("2.adyar")
    print("3.tambaram")
    print("4.kelambakam")
    print("5.turaipakam")
    
    sos_no= input("Q > Enter the sos number: ")
    sos_loc = input("Q > Enter the location to be picked up at: ")
    print("\n")
    print("\n")
    print("\nAn expert team is sent out for SOS. Please wait with patience till they arrive")
    menu()
    pass





def ClaimInsurance():
    global debt
    print("Claiming Insurance")
    insurance_policy = input("Q > Enter the Insurance policy number : ")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Your insurance is being claimed")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")   
    menu()
    pass

def Exit():
  exit=tkinter.messagebox.askyesno("Employee system","Do you want to exit the system")
  if exit>0:
    root.destroy()
    return
    print("Exiting the service")
    time.sleep(1)
    exit()




def menu():
    global debt
    print("Car Service Portal".center(50))
    #list of all services provided by the portal
    services = ["Maintenance","Wash", "Repaint", "Breakdown", "SOS", "ClaimInsurance", "Exit"]
    switch_services = [Maintenance, Wash, Repaint, Breakdown, SOS, ClaimInsurance, Exit]
    print("\nServices Provided:")
    
    z = zip( range(1, len(services) + 1), services)
    #div = lambda l: return l[0] + str(l[1])
    print("\n".join(map(lambda tup: str(tup[0]) + " " + tup[1], z)))
    print(("Existing\Debt Amount : " + str(debt)).center(100))
    
    #Selecting Inputs from user and taking action accordingly
    menu_usr_input  = int(input("Q > "))
    #assigning the respective function from the services list
    func = switch_services[menu_usr_input - 1]
    #Calling the function implementing an indirect switch case
    func()



#Main Driver Function
if __name__ == "__main__":    
    #Calling Menu function to display menu options
    menu()

