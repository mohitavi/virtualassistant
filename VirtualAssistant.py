
while True:
    tts.speak("What can i do for you?")
    txt = input("\n What can i do for you? ").lower()

    if("do not" in txt) or ("don't" in txt) or ("dont" in txt):
        tts.speak("Not opening the application")
        time.sleep(1)
        continue

    elif (("thank you" in txt) or ("exit" in txt)):
        print("Thanks!!! See You Soon")
        tts.speak("Thanks!!! See You Soon")
        break
    

        elif("calendar" in txt):
            tts.speak("Opening Calendar")
            os.system("start outlookcal:")
            time.sleep(1)

        elif("camera" in txt):
            tts.speak("Starting Camera")
            os.system("start microsoft.windows.camera:")
            time.sleep(1)

        elif("clock" in txt):
            tts.speak("Opening clock")
            os.system("start ms-clock:")
            time.sleep(1)

        elif (("calculator" in txt) or ("calc" in txt)):
            tts.speak("Opening Calculator")
            os.system("start calculator:")
            time.sleep(1)

        elif("paint" in txt):
            tts.speak("Opening Paint")
            os.system("start mspaint")
            time.sleep(1)

        elif("photos" in txt):
            tts.speak("Opening Photos")
            os.system("start ms-photos:")
            time.sleep(1)

        elif("settings" in txt):
            tts.speak("Opening Settings")
            os.system("start ms-settings:")
            time.sleep(1)

        elif("weather" in txt):
            tts.speak("Opening Weather")
            os.system("start bingweather:")
            time.sleep(1)

        elif (("ms-powerpoint" in txt) or ("microsoft office powerpoint" in txt) or ("powerpoint" in txt)):
            tts.speak("Opening Microsoft Office Powerpoint")
            os.system("start powerpnt")
            time.sleep(1)

        elif (("ms-excel" in txt) or ("microsoft office excel" in txt) or ("excel" in txt)):
            tts.speak("Opening Microsoft Office Excel")
            os.system("start excel")
            time.sleep(1)

        elif (("visual studio code" in txt) or ("vs code" in txt)):
            tts.speak("Opening Visual Studio Code")
            os.system("start code")
            time.sleep(1)

    elif(("stop" in txt) or ("kill" in txt)):
        tts.speak("Do you want to kill a process ? ")
        kill = input("\n Do you want to kill a process ? ")

        if(kill.lower() == "yes"):
            if("notepad" in txt):
                result = os.system("taskkill /im notepad.exe /f")
                if (result == 0):
                    tts.speak("Notepad should be dead now...")
                else:
                    tts.speak("Error executing taskkill command!!!")

            elif("chrome" in txt):
                result = os.system("taskkill /im chrome.exe /f")
                if (result == 0):
                    tts.speak("Chrome browser should be dead now...")
                else:
                    tts.speak("Error executing taskkill command!!!")

            elif("firefox" in txt):
                result = os.system("taskkill /im firefox.exe /f")
                if (result == 0):
                    tts.speak("Firefox should be dead now...")
                else:
                    tts.speak("Error executing taskkill command!!!")

            elif("clock" in txt):
                result = os.system("taskkill /im msclock.exe /f")
                if (result == 0):
                    tts.speak("Clocks should be dead now...")
                else:
                    tts.speak("Error executing taskkill command!!!")

            elif("calulator" in txt):
                result = os.system("taskkill /im Calculator.exe /f")
                if (result == 0):
                    tts.speak("Calculators should be dead now...")
                else:
                    tts.speak("Error executing taskkill command!!!")

            elif("calendar" in txt):
                result = os.system("taskkill /im HxCalendarAppImm.exe /f")
                if (result == 0):
                    tts.speak("Calendar should be dead now...")
                else:
                    tts.speak("Error executing taskkill command!!!")

            elif("camera" in txt):
                result = os.system(
                    "taskkill /im WindowsCamera.exe /f")
                if (result == 0):
                    tts.speak("Camera should be dead now...")
                else:
                    tts.speak("Error executing taskkill command!!!")

            elif("paint" in txt):
                result = os.system(
                    "taskkill /im mspaint.exe /f")
                if (result == 0):
                    tts.speak("Paint should be dead now...")
                else:
                    tts.speak("Error executing taskkill command!!!")

            elif("powerpoint" in txt):
                result = os.system(
                    "taskkill /im POWERPNT.exe /f")
                if (result == 0):
                    tts.speak("Powerpoint should be dead now...")
                else:
                    tts.speak("Error executing taskkill command!!!")

            elif (("ms-word" in txt) or ("word" in txt)):
                result = os.system("taskkill /im winword.exe /f")
                if (result == 0):
                    tts.speak("Ms-word should be dead now...")
                else:
                    tts.speak("Error executing taskkill command!!!")

            elif("excel" in txt):
                result = os.system(
                    "taskkill /im EXCEL.exe /f")
                if (result == 0):
                    tts.speak("excel should be dead now...")
                else:
                    tts.speak("Error executing taskkill command!!!")

        elif(kill.lower() == "no"):
            tts.speak("SORRY!!! Plz close Application manually.")