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
      p.imp_menu('Lectura', 'Aftosa','Prenez','Antiparasitario')
    elif sel==2:
      p.imp_menu('Vacias', 'Prueba','Prueba 1','Prueba 2')
    elif sel==3:
      # Apagar Ver de meter pantallita de apagado
      break
    else:
      print('No es una opcion seleccionada') 
      break
      
  if rot!=0:
    sel=sel+rot
    if sel==0:
      sel = 3
    elif sel == 4:
      sel = 1
    p.imp_menu('Comenzar a Trabajar', 'Descargar Registros','Configurar','Apagar', sel)
