import pyttsx3 
import os
import time
import platform
import subprocess
engine = pyttsx3.init()
rate = engine.getProperty('rate')  
engine.setProperty('rate', 200)    
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
print()
print("**********************************************")
print("HI!! I am Computer, Your new Virtual assistant")                    
print("**********************************************")
engine.runAndWait()
pyttsx3.speak("HI!! I am Computer, Your new Virtual assistant")

while True:
  print()
  pyttsx3.speak("What can I do for you?")
  p = input("What can I do for you? : ")
  
  if (("thank you" in p) or ("exit" in p)):
        print("Thanks!!! See You Soon")
        pyttsx3.speak("Thanks!!! See You Soon")
        break
  elif(("open" in p) or ("launch" in p) or ("start" in p) or ("show" in p)):
        if("browser" in p):
            pyttsx3.speak("Which browser you want to open : ")
            browser = input(" Which browser you want to open : ")

            if("chrome" in browser):
                    pyttsx3.speak("Opening Google Chrome")
                    os.system("start chrome")
                    time.sleep(1)

            elif("firefox" in browser):
                    pyttsx3.speak("Opening Firefox")
                    os.system("start firefox")
                    time.sleep(1)
            else:
                print("\n Browser Not Found")
                pyttsx3.speak("Browser Not Found!!")
        elif("text editor" in p):
            pyttsx3.speak("Which text editor you want to open: ")
            editor = input(" Which text editor you want to open: ")

            if("notepad" in editor):
                pyttsx3.speak("Opening Notepad")
                os.system("start notepad")
                time.sleep(1)

            elif (("ms-word" in editor) or ("microsoft office word" in editor) or ("word" in editor)):
                pyttsx3.speak("Opening Microsoft Office Word")
                os.system("start winword")
                time.sleep(1)
        elif ("date" in p): 
            pyttsx3.speak("showing todays date")
            os.system("date")
        elif ("time" in p): 
            pyttsx3.speak("showing current time")
            os.system("time")
        elif ("chrome" in p): 
            pyttsx3.speak("opening chrome")
            os.system("chrome")        
        elif ("google" in p):
            pyttsx3.speak("opening google")
            os.system("chrome google.com")
        elif ("gmail" in p):
            pyttsx3.speak("opening G mail")
            os.system("chrome www.gmail.com")
        elif ("youtube" in p):
            pyttsx3.speak("opening youtube")
            os.system("chrome www.youtube.com")
        elif ("facebook" in p):
            pyttsx3.speak("opening facebook")
            os.system("chrome www.facebook.com")
        elif ("linkedin" in p):
            pyttsx3.speak("opening linkedin")
            os.system("chrome www.linkedin.com")
        elif ("amazon" in p):
            pyttsx3.speak("opening amazon")
            os.system("chrome www.amazon.in") 
        elif("calendar" in p):
            pyttsx3.speak("Opening Calendar")
            os.system("start outlookcal:")
            time.sleep(1)

        elif("camera" in p):
            pyttsx3.speak("Starting Camera")
            os.system("start microsoft.windows.camera:")
            time.sleep(1)

        elif("clock" in p):
            pyttsx3.speak("Opening clock")
            os.system("start ms-clock:")
            time.sleep(1)

        elif (("calculator" in p) or ("calc" in p)):
            pyttsx3.speak("Opening Calculator")
            os.system("start calculator:")
            time.sleep(1)

        elif("paint" in p):
            pyttsx3.speak("Opening Paint")
            os.system("start mspaint")
            time.sleep(1)

        elif("photos" in p):
            pyttsx3.speak("Opening Photos")
            os.system("start ms-photos:")
            time.sleep(1)

        elif("settings" in p):
            pyttsx3.speak("Opening Settings")
            os.system("start ms-settings:")
            time.sleep(1)

        elif("weather" in p):
            pyttsx3.speak("Opening Weather")
            os.system("start bingweather:")
            time.sleep(1)

        elif (("ms-powerpoint" in p) or ("microsoft office powerpoint" in p) or ("powerpoint" in p)):
            pyttsx3.speak("Opening Microsoft Office Powerpoint")
            os.system("start powerpnt")
            time.sleep(1)

        elif (("ms-excel" in p) or ("microsoft office excel" in p) or ("excel" in p)):
            pyttsx3.speak("Opening Microsoft Office Excel")
            os.system("start excel")
            time.sleep(1)

        elif (("visual studio code" in p) or ("vs code" in p)):
            pyttsx3.speak("Opening Visual Studio Code")
            os.system("start code")
            time.sleep(1)
        else: 
            print("Sorry I am Still Learning.., Try Something else")
            pyttsx3.speak("Sorry I am Still Learning.., Try Something else")    
  elif ("Hello" in p) or ("hi" in p) or ("hey" in p):
            pyttsx3.speak("Hello Avi")
  elif(("stop" in p) or ("kill" in p)):
        pyttsx3.speak("Do you want to kill a process ? ")
        kill = input("\n Do you want to kill a process ? ")

        if(kill.lower() == "yes"):
            if("notepad" in p):
                result = os.system("taskkill /im notepad.exe /f")
                if (result == 0):
                    pyttsx3.speak("Notepad should be dead now...")
                else:
                    pyttsx3.speak("Error executing taskkill command!!!")

            elif("chrome" in p):
                result = os.system("taskkill /im chrome.exe /f")
                if (result == 0):
                    pyttsx3.speak("Chrome browser should be dead now...")
                else:
                    pyttsx3.speak("Error executing taskkill command!!!")

            elif("firefox" in p):
                result = os.system("taskkill /im firefox.exe /f")
                if (result == 0):
                    pyttsx3.speak("Firefox should be dead now...")
                else:
                    pyttsx3.speak("Error executing taskkill command!!!")

            elif("clock" in p):
                result = os.system("taskkill /im msclock.exe /f")
                if (result == 0):
                    pyttsx3.speak("Clocks should be dead now...")
                else:
                    pyttsx3.speak("Error executing taskkill command!!!")

            elif("calulator" in p):
                result = os.system("taskkill /im Calculator.exe /f")
                if (result == 0):
                    pyttsx3.speak("Calculators should be dead now...")
                else:
                    pyttsx3.speak("Error executing taskkill command!!!")

            elif("calendar" in p):
                result = os.system("taskkill /im HxCalendarAppImm.exe /f")
                if (result == 0):
                    pyttsx3.speak("Calendar should be dead now...")
                else:
                    pyttsx3.speak("Error executing taskkill command!!!")

            elif("camera" in p):
                result = os.system(
                    "taskkill /im WindowsCamera.exe /f")
                if (result == 0):
                    pyttsx3.speak("Camera should be dead now...")
                else:
                    pyttsx3.speak("Error executing taskkill command!!!")

            elif("paint" in p):
                result = os.system(
                    "taskkill /im mspaint.exe /f")
                if (result == 0):
                    pyttsx3.speak("Paint should be dead now...")
                else:
                    pyttsx3.speak("Error executing taskkill command!!!")

            elif("powerpoint" in p):
                result = os.system(
                    "taskkill /im POWERPNT.exe /f")
                if (result == 0):
                    pyttsx3.speak("Powerpoint should be dead now...")
                else:
                    pyttsx3.speak("Error executing taskkill command!!!")

            elif (("ms word" in p) or ("word" in p)):
                result = os.system("taskkill /im winword.exe /f")
                if (result == 0):
                    pyttsx3.speak("Ms-word should be dead now...")
                else:
                    pyttsx3.speak("Error executing taskkill command!!!")

            elif("excel" in p):
                result = os.system(
                    "taskkill /im EXCEL.exe /f")
                if (result == 0):
                    pyttsx3.speak("excel should be dead now...")
                else:
                    pyttsx3.speak("Error executing taskkill command!!!")

        elif(kill.lower() == "no"):
            pyttsx3.speak("SORRY!!! Plz close Application manually.")
  else: 
    print("Sorry I am Still Learning.., Try Something else")
    pyttsx3.speak("Sorry I am Still Learning.., Try Something else")
   