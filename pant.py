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
    
  def cadena_cent(self,cad):
    if len(cad)>=21:
      return(cad[0:21])
    else:
      esp = (21-len(cad))//2
      cadena = ''
      for x in range(esp):
        cadena = cadena+' '
      cadena = cadena+cad
      return(cadena)
    
  def imp_encab(self, wifi, BT):
    '''Esta funcion imprime el ecabezado que muestra fecha y hora del 
    dispositivo y si tiene habilitado y o conectado el bluetooth y el 
    wifi'''
    hora = time.strftime("%H:%M")
    fecha = time.strftime("%d/%m/%Y")
    self.img.p.clear()
    self.img.p.redraw()
    self.img.p.rect(0,0,127,12)
    self.img.p.put_text(fecha+'-'+hora,2,3)
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
    return self.img.p.redraw(0,0,127,12)     
        
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
    self.imp_encab(True,True)
    y0 = 15
    if sel == 1:
      self.disp.rect(0,y0,127,y0+9)
      self.disp.put_textB(lin1[0],1,y0+1)
    else:
      self.disp.put_text(lin1[0],1,y0+1)
    #self.disp.redraw()
    if sel==2:
      self.disp.rect(0,y0+10,127,y0+19)
      self.disp.put_textB(lin2[0],1,y0+11)
    else:
      self.disp.put_text(lin2[0],1,y0+11)
    #self.disp.redraw()
    if sel==3:
      self.disp.rect(0,y0+20,127,y0+29)
      self.disp.put_textB(lin3[0],1,y0+21)
    else:
      self.disp.put_text(lin3[0],1,y0+21)
    #self.disp.redraw()
    if sel==4:
      self.disp.rect(0,y0+30,127,y0+39)
      self.disp.put_textB(lin4[0],1,y0+31)
    else:
      self.disp.put_text(lin4[0],1,y0+31)
    self.disp.redraw(0,y0,127,y0+39)
    time.sleep(0.01)
    return 1
    
  def pant_select(self, title, sel, lineas):
    '''Esta funcion imprime la pantalla de seleccion a partir de los datos 
    que recibe como parametros: title el titulo de la pantalla, sel la opcion
    seleccionada, lineas una lista de 4 tuplas con el par parametro opcion'''
    self.img.p.clear()
    self.img.p.redraw()
    self.img.p.rect(0,0,127,12)
    titu=self.cadena_cent(title)
    self.img.p.put_text(titu,3,3)
    lin =[]
    for k in range(len(lineas)):
      lin.append(self.cadena_l_21(lineas[k][0])[0][0:20]+lineas[k][1])
    for t in range(4-len(lineas)):
      lin.append('')  
    print lin[0]
    y0 = 13
    if sel == 1:
      self.img.p.rect(0,y0,127,y0+9)
      self.img.p.put_textB(lin[0],1,y0+1)
    else:
      self.img.p.put_text(lin[0],1,y0+1)
    #self.disp.redraw()
    if sel==2:
      self.img.p.rect(0,y0+10,127,y0+19)
      self.img.p.put_textB(lin[1],1,y0+11)
    else:
      self.img.p.put_text(lin[1],1,y0+11)
    #self.disp.redraw()
    if sel==3:
      self.img.p.rect(0,y0+20,127,y0+29)
      self.img.p.put_textB(lin[2],1,y0+21)
    else:
      self.img.p.put_text(lin[2],1,y0+21)
    #self.disp.redraw()
    if sel==4:
      self.img.p.rect(0,y0+30,127,y0+39)
      self.img.p.put_textB(lin[3],1,y0+31)
    else:
      self.img.p.put_text(lin[3],1,y0+31)
    self.img.p.redraw()
    
  def pant_lect_carav(self, nroCarText, nCaravana, cmd, sel=False,pesoTexto='', peso ='', pais = 'UY'):
    '''Esta funcion imprime la pantalla de lectura de la caravana recibe el
    texto (Nro de caravana u en otro idioma), nCaravana (texto), cmd comando 
    del boton(Terminar), sel estado del boton, pesoTexto referecia al peso, 
    peso valor del peso y unidad y Pais del valor de la caravana'''
    nCarav5 = nCaravana[0:5]
    nCarav4 = nCaravana[5:9]
    self.img.p.put_text(nroCarText+pais+' '+nCarav5,1,3)
    self.img.p.put_textG(nCarav4,41,20)
    if peso != '':
      self.img.p.put_text(pesoTexto+peso,1,44)
    self.img.p.rect(0,54,127,63)
    coman = self.cadena_l_21(self.cadena_cent(cmd))
    if sel:
      self.img.p.put_textB(coman[0],1,55)
    else:
      self.img.p.put_text(coman[0],1,55)
    self.img.p.redraw()
