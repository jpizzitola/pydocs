from datetime import datetime

def generateDocName(pref):
    now = datetime.now()
    dt_string = now.strftime("%m.%d.%Y")

    fileName = pref + "-" + dt_string + ".docx"
   
    return fileName