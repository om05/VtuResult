fi=['2kd','2ke','2kl','2gi','2mb','2mm','2rh','2bu','2sr','2sa','2ha','2ka','2tg','2vs','2vd','3ae','3bk','3br','3gf']
import os
for i in fi:
  os.system("sudo rm -r "+i)
  os.system("sudo rm "+i+".csv")