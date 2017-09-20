import sys
sys.path.append('../Drivers/display/')
from st7920 import ST7920
import time

class pantallas:
  def __init__(self):
    #codigo de inicializacion
    self.disp = ST7920()
    
  def cadena_l_21(cadena):
    res = [cadena]
    if len(cadena) <21:
      for k in range(len(cadena),21):
        res[0] = res[0]+" "
    elif len(cadena)>21:
      div = len(cadena)//21
      resto = len(cadena%21)
      for t in range(div)
        res[t]= cadena[k:21+k]
    ###FALTA TERMINAR VER SI METER TUPLAS O LISTAS###
      
        
  def imp_menu(self,linea1,linea2,linea3, linea4):
      self.disp.clear()
      self.disp.redraw()
      self.disp.put_text(linea1,0,12)
      #self.disp.redraw()
      self.disp.put_textB(linea2,0,22)
      #self.disp.redraw()
      self.disp.put_text(linea3,0,32)
      #self.disp.redraw()
      self.disp.put_text(linea4,0,42)
      self.disp.redraw()
      time.sleep(0.01)