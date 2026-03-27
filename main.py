import sys
import psutil
from PySide6.QtCore import QTimer 
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QFrame, QLabel, QProgressBar
from PySide6.QtGui import QIcon # imports program icon
from widget import Widget 
from PySide6.QtGui import QIcon

app = QApplication(sys.argv) #for command lines
window = Widget()  # creates the window
cpulist = [] # cpu list
######## WINDOW TITLE AND ICON DOWN ####

window.setWindowTitle("taskmanager++")
if sys.platform.startswith("win"):
    window.setWindowIcon(QIcon("icon.ico"))   # icon for windows Windows
else:
    window.setWindowIcon(QIcon("icon.png")) #icon for linux
    

def RAM():
    
    mem = psutil.virtual_memory() # define a memória
    used_ram_percent = mem.percent
    free_ram = mem.available / (1024*1024) # define a memoria ram livre
    usedram = window.ui.rambar # 
    usedram.setValue(int(used_ram_percent)) # faz a barra de ram usada ficar no value
    freembnumber = window.ui.freemb
    
    rammborgb = window.ui.rammborgb # mb or gb ram label
    if free_ram >= 1024: #se free_ram for maior que 1024
        free_ram = free_ram / 1024 # divide por 1028
        gbormbram = "GB" # label vira gb
    else:
        gbormbram = "mb"
    freembnumber.display(free_ram)
    rammborgb.setText(f"free {gbormbram} RAM")

def CPU():
   cpu_percemt = psutil.cpu_percent(interval=None, percpu=False) #pega a porcentagem do cpu
   CPUBAR = window.ui.CPUbar
   CPUBAR.setValue(int(cpu_percemt))

def cpubar():
    global cpulist
    num_cores = psutil.cpu_count(logical=True)
    layout = window.ui.cpulay
    
    for cpu in range(psutil.cpu_count()):
        corebar = QProgressBar()
        window.ui.cpulay.addWidget(QLabel(f"CPU {cpu + 1}"))
        window.ui.cpulay.addWidget(corebar)
        cpulist.append(corebar)

    
    
cpubar()
def Networking():
    pass #vou deixar pra depois
    
def updatedata():
    usepercore = psutil.cpu_percent(percpu=True)
    for i, barra in enumerate(cpulist):
        value = usepercore[i]
        barra.setValue(int(value))       

timer = QTimer()
timer.timeout.connect(updatedata)
timer.timeout.connect(RAM)
timer.timeout.connect(CPU)
timer.timeout.connect(Networking)
timer.start(200)

window.show()  
sys.exit(app.exec())
