#!/usr/bin/python
import sys
sys.path.append('../Drivers/display/')
from st7920 import ST7920
import time

class img:
	def __init__(self):
		self.p=ST7920() 
	
  def pan_ini(self)
    self.churr = [0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X07, 0X80, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,0X00, 0X00, 0X1F, 0XC0, 0X30, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0XC0, 0X00, 0X00, 0X00, 0X00, 0X3C, 0XC0, 0X78, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X01, 0XE0, 0X00, 0X00, 0X00, 0X00, 0XF0, 0XC0, 0XE0, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X03, 0X80, 0X00, 0X00, 0X00, 0X01, 0XE0, 0XC1, 0XE0, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X07, 0X80, 0X00, 0X00, 0X00, 0X03, 0XC1, 0XC1, 0XC0, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X07, 0X00, 0X00, 0X00, 0X00, 0X07, 0X83, 0X83, 0X80, 0X00, 0X00, 0X00, 0X00, 0X60, 0X00, 0X00, 0X0E, 0X00, 0X00, 0X00, 0X00, 0X0F, 0X03, 0X87, 0X80, 0X00, 0X00, 0X00, 0X00, 0XE0, 0X00, 0X00, 0X1E, 0X00, 0X00, 0X00, 0X00, 0X0E, 0X07, 0X0F, 0X00, 0X00, 0X00, 0X00, 0X00, 0XC0, 0X00, 0X00, 0X3C, 0X00, 0X00, 0X00,0X00, 0X1C, 0X2E, 0X1E, 0X00, 0X00, 0X10, 0X08, 0X00, 0X00, 0X00, 0X00, 0X78, 0X00, 0X00, 0X00, 0X00, 0X3C, 0X7E, 0X1C, 0X60, 0XE1, 0XAF, 0X97, 0XC3, 0X80, 0X30, 0X1C, 0X71, 0X81, 0XE0, 0X00, 0X00, 0X78, 0X7C, 0X39, 0XE1, 0XC3, 0XFF, 0XBF, 0XC7, 0X0C, 0X70, 0X7C, 0XE7, 0X83, 0XE0, 0X00, 0X00, 0X70, 0XF8, 0X73, 0XC3, 0XC7, 0X7F, 0XBF, 0XCF, 0X1C, 0XF0, 0XFD, 0XCF, 0X0F, 0X60, 0X00, 0X00, 0XF1, 0XF0, 0X76, 0XC7, 0X8E, 0XFB, 0X7D, 0X9E, 0X39, 0XE1, 0XF9, 0XDB, 0X1C, 0XC0, 0X00, 0X00, 0XE1, 0XE0, 0XED, 0X87, 0X1E, 0X66, 0X33, 0X3C, 0X33, 0X63, 0X93, 0XB6, 0X1C, 0X80, 0X00, 0X01, 0XE1, 0X80, 0XDB, 0X8E, 0X3C, 0X4C, 0X26, 0X38, 0X66, 0XC7, 0X03, 0X6E, 0X3B, 0X00, 0X00, 0X01, 0XC0, 0X00, 0XD3, 0X1C, 0X78, 0X88, 0X44, 0X30, 0X6D, 0X8E, 0X03, 0X4C, 0X7C, 0X20, 0X00,0X03, 0XC0, 0X01, 0XF7, 0X2D, 0XD8, 0X98, 0XCC, 0X71, 0XF9, 0X96, 0X1F, 0XDC, 0XB8, 0X20, 0X00, 0X03, 0XC0, 0X02, 0XE7, 0XCF, 0XBF, 0X1F, 0X8F, 0XFF, 0XF3, 0XE7, 0XFB, 0X9F, 0X38, 0XC0, 0X00, 0X03, 0XC0, 0X04, 0XC7, 0X8F, 0X3E, 0X1E, 0X0F, 0X1F, 0X73, 0XC3, 0XF3, 0X1E, 0X3F, 0X80, 0X00, 0X03, 0XC0, 0X18, 0X07, 0X06, 0X3C, 0X0C, 0X06, 0X1C, 0X23, 0X81, 0XC0, 0X1C, 0X1E, 0X00, 0X00, 0X03, 0XE0, 0X30, 0X00, 0X00, 0X10, 0X00, 0X00, 0X00, 0X01, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X03, 0XE0, 0XE0, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X01, 0XFF, 0XC0, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X01, 0XFF, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,0X00, 0X7C, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X10, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X30, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X1F, 0XC0, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X1F, 0XE0, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0XE3, 0XF0, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0XC1, 0XFC, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X03, 0X00, 0X67, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X06, 0X00, 0X3C, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X1C, 0X03, 0XF8, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X30, 0X03, 0XF8, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X40, 0X01, 0XF8, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0XC0, 0X01, 0XF0, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X03, 0X00, 0X03, 0XF0, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X02, 0X00, 0X07, 0XE0, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,0X00, 0X00, 0X00, 0X00, 0X00, 0X0C, 0X00, 0X3F, 0XC0, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X08, 0X00, 0XFF, 0XC0, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X10, 0X3F, 0XFF, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X33, 0XFF, 0XFE, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X7F, 0X83, 0XF0, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X7F, 0X01, 0XD0, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0XFC, 0X00, 0XFC, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X01, 0XE8, 0X00, 0XFC, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00,0X00, 0X00, 0X00, 0X00, 0X07, 0X30, 0X00, 0X3C, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X02, 0XE0, 0X00, 0X74, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X07, 0X80, 0X00, 0XF8, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X78, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00, 0X00]

		#print(len(self.churr))
		for i in range(0, 64):
			self.p.send(0,0,[0x80 + i%32, 0x80 + ((8 if i>=32 else 0))]) # set address
			lista=[]
			for k in range(i*16,i*16+16):
			  lista.append(self.churr[k])
			self.p.send(1,0,lista)
		time.sleep(0.6)
      #print(lista)
      #print(1,0,self.churr[(i//16)*8:(i//16+1)*16])

	def wifi_icon(self,x,y):
    		self.wifi_ico = ['0011111100','0100000010','1000000001','0001111000','0010000100','0100000010','0000110000','0001001000','0000000000','0000110000']
    		for y1 in range(len(self.wifi_ico)):
      			for x1 in range(len(self.wifi_ico[y1])):
	        		self.p.plot(x1+x,y1+y,int(self.wifi_ico[y1][x1]))
    		return 1
    
  	def BT_icon(self,x,y):
    		self.BT_ico = ['0001000000','0001100000','1001010010','0101010001','0011100101','0011100101','0101010001','1001010010','0001100000','0001000000']
    		for y2 in range(len(self.BT_ico)):
      			for x2 in range(len(self.BT_ico[y2])):
        			self.p.plot(x2+x,y2+y,int(self.BT_ico[y2][x2]))
    		return 1 
