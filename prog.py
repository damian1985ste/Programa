from pant import pantallas
import sys
sys.path.append('../Drivers/Rotary-Encoder/')
from rotary_encoder import r_encoder


p = pantallas()
re = r_encoder()

# Imprimo menu inicial
sel = 1
p.imp_menu('Trabajar con animales en manga', 'Identificar animales','Apagar', sel)

#si presionamos el boton pasamos al siguiente menu, si giramos el rotary encoder seleccionamos la linea indicada
while True:
  btn = false
  rot = 0
  while not btn or rot==0:
    btn = re.btn_state()
    rot = re.rot_encod()[0]
  
  if btn:
    #presionamos el boton siguiente menu
    if sel==1:
      p.imp_menu('Lectura', 'Aftosa','Preñez','Antiparasitario')
    elif sel==2:
      p.imp_menu('Vacias', 'Prueba','Prueba 1','Prueba 2')
    elif sel==3:
      # Apagar Ver de meter pantallita de apagado
      break
    else:
      print('Error: opcion seleccionada no existe')
      break
      
  if rot!=0:
    sel=sel+rot
    if sel==0:
      sel = 3
    elif sel == 4:
      sel = 1
    p.imp_menu('Trabajar con animales en manga', 'Identificar animales','Apagar', sel)
