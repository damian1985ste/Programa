from images import img
import sys
sys.path.append('../Drivers/display/')
from st7920 import ST7920
import time


class pantallas:
  def __init__(self):
    #codigo de inicializacion
    self.disp = ST7920()
    self.img =img()
    
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
    
  def imp_encab(self, wifi, BT):
    '''Esta funcion imprime el ecabezado que muestra fecha y hora del 
    dispositivo y si tiene habilitado y o conectado el bluetooth y el 
    wifi'''
    hora = time.strftime("%H:%M")
    fecha = time.strftime("%d/%m/%Y")
    self.img.p.clear()
    self.img.p.redraw()
    self.img.p.rect(0,0,127,11)
    self.img.p.put_text(fecha+'-'+hora,2,2)
    #self.img.p.redraw(0,0,127,11)
    if wifi:
      #self.img.wifi_icon(102,2)# Mostramos el logo de wifi activado o conectado
      	wifi_ico = ['0011111100','0100000010','1000000001','0001111000','0010000100','0100000010','0000110000','0001001000','0000000000','0000110000']
	for y1 in range(len(wifi_ico)):
      			for x1 in range(len(wifi_ico[y1])):
	        		self.img.p.plot(x1+102,y1+2,int(wifi_ico[y1][x1]))
    if BT:
      #self.img.BT_icon(115,2)# Mostramos el logo de bluetooth activado o conectado 
      	BT_ico = ['0001000000','0001100000','1001010010','0101010001','0011100101','0011100101','0101010001','1001010010','0001100000','0001000000']
    	for y2 in range(len(BT_ico)):
      			for x2 in range(len(BT_ico[y2])):
        			self.img.p.plot(x2+115,y2+2,int(BT_ico[y2][x2]))     
    return self.img.p.redraw(0,0,127,11)     
        
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
    return 1
