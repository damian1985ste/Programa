import time
import sys
sys.path.append('../Drivers/Rotary-Encoder/')
from rotary_encoder import r_encoder
sys.path.append('../Drivers/beeper/')
from beeper import beeper
sys.path.append('../Drivers/RFID/')
from RI_STU_MRD2 import rfid

from pant import pantallas
from images import img

img = img()
img.pan_ini()
p = pantallas()
re = r_encoder()
beep = beeper()
rfid = rfid()

def DaRopc(opc):
  if opc==' ':
    opc='A'
  elif opc=='A':
    opc='M'
  elif opc=='M':
    opc=' '
  return(opc) 
  
def selct(s):
	if s==' ':
		s='X'
	elif s=='X':
		s=' ' 
	return(s)


# Imprimo menu inicial
sel = 1
p.imp_menu('Comenzar a Trabajar', 'Descargar Registros','Configurar','Apagar', sel)

#si presionamos el boton pasamos al siguiente menu, si giramos el rotary encoder seleccionamos la linea indicada
while True:
  btn = False
  rot = 0
  p.imp_menu('Comenzar a Trabajar', 'Descargar Registros','Configurar','Apagar', sel)
  print('prog.py - linea 40 -> antes del while menu inicial btn,rot',btn,rot)
  while not btn and rot==0:
    btn = re.btn_state()
    #print(btn)
    rot = re.rot_encod()[0]
  print('prog.py - linea 45 -> Salgo del wihle menu inicial de boton o rotary',btn,rot)
  if btn:
  
    if sel==1:
      #Menu Comenzar a trabajar - Pide seleccionar datos a registrar; Lotes a identificar; y luego la pantalla de lectura de caravanas
      sel1,e1,e2,e3,e4=1,'A',' ','M','A'
      btn1=False
      while sel1!='X': #and not btn1:
        print('prog.py - linea 53 -> Menu comenzar a trabjar - datos a registrar boton: '+str(btn1)+'  rotary sel1: '+str(sel1))
        btn1=False
        rot1=0
        p.pant_select('Datos a registrar', sel1, [('Lectura',e1), ('Aftosa', e2), ('Vientre vacio',e3), ('Antiparasitario',e4)], 'Siguiente', 'Cancelar')
        while not btn1 and rot1==0:
          btn1 = re.btn_state()
          #print(btn)
          rot1 = re.rot_encod()[0]
  
        if btn1:
          if sel1==1:
            e1=DaRopc(e1)
          elif sel1==2:
            e2=DaRopc(e2)
          elif sel1==3:
            e3=DaRopc(e3)
          elif sel1==4:
            e4=DaRopc(e4)
          elif sel1==5:
            #Pantalla siguiente Lotes a identificar
            print('prog.py - linea 73 -> Comenzar a trabajar - Lotes  a identificar')
            sel11, e11, e12, e13, e14 = 1 , 'X' , ' ' , ' ' , ' '
            btn11=False
            while sel11!='X': #and not btn11:
				print('prog.py - linea 77 -> Menu comenzar a trabjar - lotes a identificar: boton'+str(btn11)+'  rotary sel11: '+str(sel11))
				btn11=False
				rot11=0
				p.pant_select('Datos a registrar', sel11, [('Vacias',e11), ('Lote A', e12), ('Lote B',e13), ('Tratamiento x',e14)], 'Comenzar', 'Cancelar')
				while not btn11 and rot11==0:
				  btn11 = re.btn_state()
				  #print(btn)
				  rot11 = re.rot_encod()[0]
		  
				if btn11:
				  if sel11==1:
					e11=selct(e11)
				  elif sel11==2:
					e12=selct(e12)
				  elif sel11==3:
					e13=selct(e13)
				  elif sel11==4:
					e14=selct(e14)
				  elif sel11==5:
					#Pantalla siguiente Lotes a identificar
					print('prog.py - linea 97 -> Comenzar a trabajar - Lotes  a identificar - Comenzar')
					sel12=''
					btn12=False
					btnsel=False
					carav=('000','000000000')
					while sel12!='X':
						print('prog.py - linea 77 -> Menu comenzar a trabjar - Lee caravanas: boton'+str(btn12)+'  rotary sel11: '+str(sel12))
						btn12=False
						rot12=0
						p.pant_lect_carav('Nro caravana:', '0'+str(carav[1]),'Terminar',btnsel, 'Peso: ','250 Kg')
						while not btn12 and rot12==0:
							btn12 = re.btn_state()
							rot12 = re.rot_encod()[0]
						
						if btn12:
							if sel12==1:
								sel12='X'
								sel11='X'
								sel1='X'
							else:
								#LEER CARAVANA.
								carav=rfid.readTag()
								beep.beep(0.3)
							
						if rot12!=0:
							sel12=1
							btnsel=True
						else:
							btnsel=False
					print('prog.py - linea 120 -> Salgo de la pantalla de lectura')	
						
				  elif sel11==6:
					#print('prog.py - linea 99 -> Opcion de salida Comenzar a trabajar - Datos a Registrar')
					sel11='X'

				if rot11!=0:
				  sel11=sel11+rot11
				  if sel11==0:
					sel11=6
				  elif sel11==7:
					sel11=1
            print('prog.py - linea 108 -> Salgo del menu Comenzar a trabajar - Lotes a identificar')
            time.sleep(0.2)
            btn1=False
          elif sel1==6:
            #print('prog.py - linea 112 -> Opcion de salida Comenzar a trabajar - Datos a Registrar')
            sel1='X'
             
        #p.imp_menu('Lectura', 'Aftosa','Prenez','Antiparasitario')
        if rot1!=0:
          sel1=sel1+rot1
          if sel1==0:
            sel1 = 6
          elif sel1 == 7:
            sel1 = 1
      print('prog.py - linea 122 -> Salgo del menu Comenzar a trabajar - Datos a Registrar')
      time.sleep(0.2)
      btn=False
    elif sel==2:
      p.imp_menu('Descargar datos', 'Borrar registros','','Prueba 2')
    elif sel==3:
      #Codigo
      print('opcion 3')
    elif sel==4:
      # Apagar Ver de meter pantallita de apagado
      break
    else:
      print('prog.py - linea 134 -> No es una opcion seleccionada') 
      break
      
  if rot!=0:
    sel=sel+rot
    if sel==0:
      sel = 4
    elif sel == 5:
      sel = 1
    #p.imp_menu('Comenzar a Trabajar', 'Descargar Registros','Configurar','Apagar', sel)
