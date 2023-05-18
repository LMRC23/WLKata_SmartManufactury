# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print('connecting')
from time import sleep
import paho.mqtt.client as mqtt
from wlkata_mirobot import WlkataMirobot
import datetime;

arm = WlkataMirobot(portname='/dev/ttyUSB0')
print('connected')
#arm.home()
#print('home rutine executed')
arm.home_7axis()
print('home2 rutine executed')

x = 1



def Primera_rutina_TRG_Dejar_Pieza():
    #INICIO
    arm.go_to_axis(0,0,0,0,0,0) 
    #Mover riel
    arm.set_slider_posi(400)
    #Rotar para evitar colición
    arm.go_to_axis(-65,0,0,0,0,0)
    #Recoger pieza NFC
    arm.go_to_axis(-70,64,-15.5,-1,-55,6.6)
    sleep(5)
    #Acercar al WLKata
    arm.go_to_axis(-58,14,45,-5.5,-68,-10)
    #Subir pieza
    arm.go_to_axis(22,-17,6,3,2,-5)
    #Pocisionar efector
    arm.go_to_axis(74.3,-12,-19.3,0.4,29.6,11.9)
    #Acercar efector
    arm.go_to_axis(76.9,15,-46.8,0.3,30,9.1)
    #Pocisionamiento mejorado
    arm.go_to_axis(77,12.6,-35.7,0.3,21.3,8.8)
    #Colocar pieza
    arm.go_to_axis(69.4,-27,4.6,0.5,20.8,16.2)
    #Retirar efector
    arm.go_to_axis(44,-40,24,7.5,4,17)
    #Rotar a P0
    arm.go_to_axis(0,-40,24,7.5,4,17)
    #FIN
    arm.go_to_axis(0,0,0,0,0,0)

def Primera_rutina_TRG_Recoger_Pieza():
    #INICIO
    arm.go_to_axis(0,0,0,0,0,0) 
    arm.set_slider_posi(400)
    #Rotar 
    arm.go_to_axis(60,-37.6,30,0,7.6,0)
    #Subir
    arm.go_to_axis(60,-27.7,5.7,0,21.9,0)
    #Posicionar
    arm.go_to_axis(73.4,-8.7,-12.5,5,22.7,16.6)
    #Meter efector
    arm.go_to_axis(75.6,15.8,-38.1,5,23.5,14.2)
    #Subir
    arm.go_to_axis(77.7,30.9,-66.5,0,35.4,5.1)
    #Sacar pieza
    arm.go_to_axis(71,-14.4,-15.6,0,30.1,11.7)
    #Rotar
    arm.go_to_axis(0,0,0,0,0,0)
    #Rotar NFC
    arm.go_to_axis(-60,0,0,0,0,0)
    #NFC
    arm.go_to_axis(-71.1,61,-9.6,0,-51.4,11)
    sleep(51)
    #Subir
    arm.go_to_axis(-60,0,0,0,0,0)
    #FIN
    arm.go_to_axis(0,0,0,0,0,0)
    
def Segunda_rutina_TNM_Dejar_Pieza():
    arm.go_to_axis(10,3,3,10,3,3)
    arm.set_slider_posi(150)

def Segunda_rutina_TNM_Recoger_Pieza():
    arm.go_to_axis(3,3,3,3,3,3)
    arm.set_slider_posi(200)




while x <= 6:
    x = int(input('Selecciona una rutina: '))
    
    if x == 1:
        Primera_rutina_TRG_Dejar_Pieza()
    elif x == 2:
        Primera_rutina_TRG_Recoger_Pieza()
    elif x == 3:
        Segunda_rutina_TNM_Dejar_Pieza()
    elif x == 4:
        Segunda_rutina_TNM_Recoger_Pieza()
    elif x == 5:
        arm.home_7axis()





    