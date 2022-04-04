import time
from xyz import *

l_home = L_Homepage()

for i in range(2):
    img = "E:\1. College\SE\Sem 4\proj materials" + i
    l_home.label_21.setPixmap(qtg.QPixmap(img))
    time.sleep(2.4)