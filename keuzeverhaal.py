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
  time.sleep(1)
  print ("""  A. run inside house
  B. Stay and defend your house
  C. Drive away
  D. Do nothing""")
  choice = input(">>> ") 
  if choice in answer_A: #route 1
    option_house()
  elif choice in answer_B: #route 2
    #option
    ()
  elif choice in answer_C: #route 3
    option_family()
  elif choice in answer_D: #route 4
    #option
    ()
  else:
    print (required)
    intro()

#route 1
def option_house(): 
  print ("\nYou run inside the house, what will you do? "
  "You will:")
  time.sleep(1)
  print ("""  A. Warn family 
  B. Stay and fight""")
  choice = input(">>> ")
  if choice in answer_A: #route 1.1
    option_family()
  elif choice in answer_B: #route 2.3
   #option
   ()
  else:
    print (required)
    option_house()


#route 1.1
def option_family():
  print ("\nYou warn your family about the incoming invasion and run out of the house, where will you go now? "
  "you will go to:")
  time.sleep(1)
  print ("""  A. Poland
  B. Airport""")
  choice = input(">>> ")
  if choice in answer_A: #route 1.2
    #option
    ()
  elif choice in answer_B: #route 1.3
    #option
    ()
  else:
    print (required)
    option_family()
    


intro()
