import sys
sys.path.append('../Drivers/Rotary-Encoder/')
from rotary_encoder import r_encoder

from pant import pantallas
from images import img

img = img()
img.pan_ini()
p = pantallas()
re = r_encoder()

# Imprimo menu inicial
sel = 1
p.imp_menu('Comenzar a Trabajar', 'Descargar Registros','Configurar','Apagar', sel)

#si presionamos el boton pasamos al siguiente menu, si giramos el rotary encoder seleccionamos la linea indicada
while True:
  btn = False
  rot = 0
  print('antes del while btn,rot',btn,rot)
  while not btn and rot==0:
    btn = re.btn_state()
    #print(btn)
    rot = re.rot_encod()[0]
  print('Saldgo del wihle de boton o rotary',btn,rot)
  if btn:
    #presionamos el boton siguiente menu
    if sel==1:
      #Menu Comenzar a trabajar - Pide seleccionar datos a registrar; Lotes a identificar; y luego la pantalla de lectura de caravanas
      sel1=1
      e1='A'
      e2=''
      e3='M'
      e4='A'
      
      while sel1 != 5 or sel1 !=6 and btn1:
        btn1=False
        p.pant_select('Datos a registrar', sel1, [('Lectura',e1), ('Aftosa', e2), ('Vientre vacio',e3), ('Antiarasitario',e4)], 'Siguiente', 'Cancelar')
        while not btn1 and rot1==0:
          btn1 = re.btn_state()
          #print(btn)
          rot1 = re.rot_encod()[0]
  
        if btn1:
          if sel1==1:
            if e1=='':
              e1='A'
            elif e1=='A':
              e1='M'
            elif e1=='M':
              e1='' 
          elif sel1==2:
            if e2=='':
              e2='A'
            elif e2=='A':
              e2='M'
            elif e2=='M':
              e2=''
          elif sel1==3:
            if e3=='':
              e3='A'
            elif e3=='A':
              e3='M'
            elif e3=='M':
              e3=''
          elif sel1==4:
            if e4=='':
              e4='A'
            elif e4=='A':
              e4='M'
            elif e4=='M':
              e4=''  
        #p.imp_menu('Lectura', 'Aftosa','Prenez','Antiparasitario')
        if rot1!=0:
          sel1=sel1+rot1
          if sel1==0:
            sel1 = 6
          elif sel1 == 7:
            sel1 = 1
      if sel1 == 5:
        #Pantalla siguiente Lotes a identificar
    elif sel==2:
      p.imp_menu('Descargar datos', 'Borrar registros','','Prueba 2')
    elif sel==3:
      #Codigo
      print('opcion 3')
    elif sel==4:
      # Apagar Ver de meter pantallita de apagado
      break
    else:
      print('No es una opcion seleccionada') 
      break
      
  if rot!=0:
    sel=sel+rot
    if sel==0:
      sel = 4
    elif sel == 5:
      sel = 1
    p.imp_menu('Comenzar a Trabajar', 'Descargar Registros','Configurar','Apagar', sel)
