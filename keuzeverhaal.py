from pprint import pprint
import time





answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
answer_D = ["D", "d"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]




required = ("\nUse only A, B, or C\n")


#intro

def intro():
  print ("You are a Ukranian citizen living in kiev with your family. "
  "You are listening to the radio, an there are " 
  "some news saying that russia is invading Ukraine. "
  "The broadcasters say to evacuate as soon as possible. "
  "what whill you do?: ")
  time.sleep(2)
  print ("""  A. run inside house
  B. Stay and defend your house
  C. Leave alone
  D. Do nothing""")
  choice = input(">>> ") 
  if choice in answer_A: #route 1
    option_house()
  elif choice in answer_B: #route 2
    option_stay()
  elif choice in answer_C: #route 3
    option_leave()
  elif choice in answer_D: #route 4
    option_nothing()
  else:
    print (required)
    intro()


def option_leave():
    print("\nYou run away and leave your family behind to save your self "
    "while runing you encounter some russian soldiers"
    "what do you do?:")
    time.sleep(2)
    print("""  A. keep runnnig
    B. offer them vodka """)
    choice = input(">>> ")
    if choice in answer_A:
      option_run()
    elif choice in answer_B:
      print ("\nthey kill you "
    "\n\n")
    else:
      print (required)
      option_leave
  

def option_run():
    print("\nyou keep running and the soldiers mind their own business. "
    "what do you do now?:")
    time.sleep(2)
    print("""  A. keep runnnig
    B. stop running """)
    choice = input(">>> ")
    if choice in answer_A:
      option_run1()
    elif choice in answer_B:
      print ("\nyou stoped running "
    "\n\n")
    else:
      print (required)
      option_run


def option_run1():
    print("\nyou keep running again. "
    "what will you do now?:")
    time.sleep(2)
    print("""  A. keep runnnig
    B. stop running """)
    choice = input(">>> ")
    if choice in answer_A:
      option_run2()
    elif choice in answer_B:
      print ("\nyou stoped running "
    "\n\n")
    else:
      print (required)
      option_run1    


def option_run2():
    print("\nyou keep running and the soldiers mind their own business. "
    "what do you do now?:")
    time.sleep(2)
    print("""  A. keep runnnig
    B. stop running """)
    choice = input(">>> ")
    if choice in answer_A:
      print ("\nsomehow after running so much you made it to poland. "
      "far away from the war and far away from you family tha you left behind. (you monster)"
    "\n\nYou survived")
    elif choice in answer_B:
      print ("\nyou stoped running "
    "\n\n")
    else:
      print (required)
      option_run2    


#route 1

def option_house(): 
  print ("\nYou run inside the house, what will you do? "
  "You will:")
  time.sleep(2)
  print ("""  A. Warn family 
  B. Stay and fight""")
  choice = input(">>> ")
  if choice in answer_A: #route 1.1
    option_family()
  elif choice in answer_B: #route 2.3
   option_stay()
  else:
    print (required)
    option_house()


#route 1.1

def option_family():
  print ("\nYou warn your family about the incoming invasion and run out of the house, where will you go now? "
  "you will go to:")
  time.sleep(2)
  print ("""  A. Poland
  B. Airport""")
  choice = input(">>> ")
  if choice in answer_A: #route 1.2
    option_poland()
  elif choice in answer_B: #route 1.3
    option_airport()
    ()
  else:
    print (required)
    option_family()


#route 1.2

def option_poland():
  print("\nYou and your family decide that the best option is to leave everything behind and escape to Poland."
  "You go in your car and start driving, but in the way to poland you encounter some ukranians "
  "soldiers that are recruiting anyone willing to fight the russians."
  "Do you:")
  time.sleep(2)
  print ("""  A. Leave the country with your family
  B. insult soldiers """)
  choice = input(">>> ")
  if choice in answer_A: 
    print ("\nYou decide to run away with your family to poland. "
    "The soldiers seem dissapointed, but respect your decision an let you go on your way. "
    "You succeeded and got into poland safely. "
    "altough, you feel remorce for leaving your house and belongins behind  "
    "and not fighting for yourcountry \n\nYou survived.")
  elif choice in answer_B: 
    print ("\nYou say to the soldiers that it is insulting "
    "fighting for your country, you tell them to tun while they still have the chance or they will die poiintlesly"
    "\n\nthey shooot and kill you")
  else:
    print (required)
    option_poland()


#route 1.3

def option_airport():
  print("\nYou decide to drive to the airport with your family, and "
  "try to grab the first flight that leaves the country."
  "unfortunatley, everyone thought of going to the airport "
  "and now the airport is full of people and theres no flight out of the country."
  "What will you do now?: ")
  time.sleep(2)
  print(""" A. Poland 
  B. wait for a flight """)
  choice = input(">>> ")
  if choice in answer_A: #route 1.2
     option_poland()
  elif choice in answer_B: #rpute 1.4
    option_waitairport()
  else:
    print (required)
    option_airport()


  #route 1.4

  def option_waitairport():
    print("\nYou stubbornly decide to wait in the airport in hopes for a flight to be available, "
    "surprisingly and unexpectely a new flight opend up. but there are only 2 seats left available."
    "you must now chooose, let your family get on the flight and you get left behind, or find another "
    "way to travel with your family. "
    "What will you choose?: ")
    time.sleep(2)
  print(""" A. let your family fly
  B. poland """)
  choice = input(">>> ")
  if choice in answer_A: 
    print ("\nYou let your wife and teenage kid get into the plane to get out of the country safely. "
    "you get left behind amd have to find your own way out of the country. \n\nYou surviived?")
  elif choice in answer_B: #route 1.2
    option_poland()
  else:
    print (required)
    option_waitairport()


  #route 2
  
def  option_stay():
  print("\nIn panic you begin to board up your wiindows, you grab your gun a wait for anything to happen. "
  "After waiting for hours you hear a platoon of russian soldiers crossing by your street. "
  "Do you:")
  time.sleep(2)
  print(""" A. let them pass
  B. ambush the soldiers """)
  choice = input(">>> ")
  if choice in answer_A: 
    option_pass()
  elif choice in answer_B: #route 2.1
    print ("\nYou try to ambush the russian soldiers, you banaged to kill a few but the other 10 imidiatly shot back and kill you. "
    "\n\nYou died")
  else:
    print (required)
    option_stay()

  
  # route 2.1

  def option_pass():
    print("\nThe russians outnumber you so you let them pass. "
    "you cant fight the russians on your own so you begin to question you place in this war. "
    "what will you do next?:")
    time.sleep(2)
  print(""" A. escape country
  B. join a military group """)
  choice = input(">>> ")
  if choice in answer_A: #route 1.3
    option_airport()
  elif choice in answer_B: #route 2.2
    option_group()
  else:
    print (required)
    option_pass()


    #route 2.2
    def option_group():
      print("\nYou decide that your best chance against the russians is joining the rebellion, "
      "youll be fighting for your country and your freedom. "
      "but you wont be able to see your family for a while since you are gonna be in the front lines. "
      "fast forward a few weeks and now you are fighting to liberate kiev. "
      "out of nowhere a T-62 russian tanmks is infront of you. "
      "what will you do now?:")
      time.sleep(2)
  print(""" A. run and hide
  B. shoot it """)
  choice = input(">>> ")
  if choice in answer_A: #route 2.3
    option_run()
  elif choice in answer_B: 
    print ("\nYou died "
    "\n\nWhat did you expect?")
  else:
    print (required)
    option_group()


    #route 2.3

    def option_run():
      print("\nYou run and hide from the tank, you try hiding under some ruble in a building. "
      "what willyou do next?:")
      time.sleep(2)
  print(""" A. run and hide
  B. shoot it """)
  choice = input(">>> ")
  if choice in answer_A: #route 2.4
    option_hide()
  elif choice in answer_B: 
    print ("\nYou died "
    "\n\nWhat did you expect?")
  else:
    print (required)
    option_run()

def option_hide():
  print("\nyou decide to hide. "
  "do you keep hiding?")
  time.sleep(2)
  print(""" yes
 no """)
  choice = input(">>> ")
  if choice in yes: 
    option_hide1()
  elif choice in no: 
    print ("\nYou died "
    "\n\nyoull have to wait a bit longer")
  else:
    print (required)
    option_hide()


  def option_hide1():
    print("\nyou decide to keep hiding. "
  "do you keep hiding?")
  time.sleep(2)
  print(""" yes
 no """)
  choice = input(">>> ")
  if choice in yes: 
    option_hide2()
  elif choice in no: 
    print ("\nYou died "
    "\n\nwait a bit more")
  else:
    print (required)
    option_hide1()


    def option_hide2():
      print("\nyou decide to keep hiding a bit more. "
  "do you keep hiding?")
  time.sleep(2)
  print(""" yes
 no """)
  choice = input(">>> ")
  if choice in yes: 
    option_hide3()
  elif choice in no: 
    print ("\nYou died "
    "\n\nnot yet")
  else:
    print (required)
    option_hide2()


    def option_hide3():
      print("\nyou decide to keep hiding a bit more eeven more. "
  "do you keep hiding?")
  time.sleep(2)
  print(""" no
 no """)
  choice = input(">>> ")
  if choice in yes: 
    option_hide1()
  elif choice in no: 
    print ("\the tank left "
    "\n\nyou survived")
  else:
    print (required)
    option_hide3()


def option_nothing():
  print("\nyou decide to do nothing, you think that russia would never invade ukraine "
  "do you:")
  print("""  A. keep doing nothing
   B. run inside the house """)
  choice = input(">>> ")
  if choice in answer_A:
    option_nothing1()
  elif choice in answer_B:
    option_house
  else:
    print (required)
    option_nothing  
 

def option_nothing1():
  print("\nyou keep doing nothing. (you should probably move) "
  "do you:")
  print("""  A. keep doing nothing again
   B. run inside the house """)
  choice = input(">>> ")
  if choice in answer_A:
    option_nothing2()
  elif choice in answer_B:
    option_house
  else:
    print (required)
    option_nothing1


def option_nothing2():
  print("\nyou keep doing nothing. (dude just move) "
  "do you:")
  print("""  A. keep doing nothing again again
   B. run inside the house """)
  choice = input(">>> ")
  if choice in answer_A:
    option_nothing3()
  elif choice in answer_B:
    option_house
  else:
    print (required)
    option_nothing2

def option_nothing3():
  print("\nyou keep doing nothing. (you definetly need to move) "
  "do you:")
  print("""  A. keep doing nothing again again agin
   B. run inside the house """)
  choice = input(">>> ")
  if choice in answer_A:
    print ("\nA bomb falls on your house and kills you and your entire family. "
    "you died\n\n(i warned you)")
  elif choice in answer_B:
    option_house
  else:
    print (required)
    option_nothing3

intro()
