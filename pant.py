import sys
sys.path.append('../Drivers/display/')
from st7920 import ST7920
import time

class pantallas:
  def __init__(self):
    #codigo de inicializacion
    self.disp = ST7920()
    
  def cadena_l_21(self, cadena):
    '''Esta funcion devuelve una lista con cadenas de largo 21
    a partir de una cadena original pasada como parametro'''
    res = []
    if len(cadena) <= 21:
      res = [cadena]
      for k in range(len(cadena),21):
        res[0] = res[0]+" "
    elif len(cadena)>21:
      div = len(cadena)//21
      resto = len(cadena)%21
      for t in range(div):
        res.append(cadena[21*t:21+21*t])
      res.append(cadena[21*div:21*div+resto])
      for w in range(resto,21):
        res[div] = res[div]+" "
    return res
    
      
        
  def imp_menu(self,linea1,linea2 ="",linea3="", linea4="", sel = 1):
    '''Esta funcion realiza la impresion en pantalla del menu de 
    acuerdo a los parametros linea1,linea2,linea3, linea4 que son
    las opciones del menu y se encontrara seleccionada la que 
    indique el parametro sel con valores de 1 a 4 (por defecto 1)'''
    lin1 = self.cadena_l_21(linea1)
    lin2 = self.cadena_l_21(linea2)
    lin3 = self.cadena_l_21(linea3)
    lin4 = self.cadena_l_21(linea4)   
    self.disp.clear()
    self.disp.redraw()
    if sel == 1:
      self.disp.rect(0,11,127,20)
      self.disp.put_textB(lin1[0],1,12)
    else:
      self.disp.put_text(lin1[0],1,12)
    #self.disp.redraw()
    if sel==2:
      self.disp.rect(0,21,127,30)
      self.disp.put_textB(lin2[0],1,22)
    else:
      self.disp.put_text(lin2[0],1,22)
    #self.disp.redraw()
    if sel==3:
      self.disp.rect(0,31,127,40)
      self.disp.put_textB(lin3[0],1,32)
    else:
      self.disp.put_text(lin3[0],1,32)
    #self.disp.redraw()
    if sel==4:
      self.disp.rect(0,41,127,50)
      self.disp.put_textB(lin4[0],1,42)
    else:
      self.disp.put_text(lin4[0],1,42)
    self.disp.redraw()
    time.sleep(0.01)