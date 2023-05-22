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

arm = WlkataMirobot(portname='COM5')
print('connected')
#arm.home()
#print('home rutine executed')
arm.home_7axis()
print('home2 rutine executed')

x = 1



def R1_TRG_Dejar():
    arm.set_speed(1500)
    #INICIO
    arm.go_to_axis(0,0,0,0,0,0) 
    #Mover riel a entrada
    arm.set_slider_posi(407,2000)
    #Rotar para evitar colisión
    arm.go_to_axis(-65,0,0,0,0,0)
    #Recoger pieza NFC
    arm.go_to_axis(-70,64,-15.5,-1,-55,6.6)
    sleep(5)
    #Acercar al WLKata
    arm.go_to_axis(-58,14,45,-5.5,-68,-10)
    #Subir pieza
    arm.go_to_axis(22,-17,6,3,2,-5)
    #Posicionar efector
    arm.go_to_axis(74.3,-12,-19.3,0.4,29.6,11.9)
    #Acercar efector
    arm.go_to_axis(76.9,15,-46.8,0.3,30,9.1)
    #Posicionamiento mejorado
    arm.go_to_axis(77,12.6,-35.7,0.3,21.3,8.8)
    #Colocar pieza
    arm.go_to_axis(69.4,-27,4.6,0.5,20.8,16.2)
    #Retirar efector
    arm.go_to_axis(44,-40,24,7.5,4,17)
    #Rotar a P0
    arm.go_to_axis(0,-40,24,7.5,4,17)
    #FIN
    arm.go_to_axis(0,0,0,0,0,0)
    arm.set_slider_posi(50,2000)


def R1_TRG_Recoger():
    arm.set_speed(1500)
    #INICIO
    arm.go_to_axis(0,0,0,0,0,0) 
    arm.set_slider_posi(407,2000)
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
    sleep(5)
    #Subir
    arm.go_to_axis(-60,0,0,0,0,0)
    #FIN
    arm.go_to_axis(0,0,0,0,0,0)
    arm.set_slider_posi(50,2000)
    

def R2_TNM_Dejar():
    arm.set_speed(1500)
    #INICIO
    arm.go_to_axis(0,0,0,0,0,0)
    #Mover riel a entrada
    arm.set_slider_posi(407,2000)
    #Rotar para evitar colisión
    arm.go_to_axis(-65,0,0,0,0,0)
    #Recoger pieza NFC
    arm.go_to_axis(-70,64,-15.5,-1,-55,6.6)
    sleep(5)
    #Acercar al WLKata
    arm.go_to_axis(-58,14,45,-5.5,-68,-10)
    #Subir pieza
    arm.go_to_axis(0,0,0,0,0,0)
    #Mover riel
    arm.set_slider_posi(296,2000)
    #Acercar efector y posición
    arm.go_to_axis(90,-40,50,0,-10,0)
    #Meter efector
    arm.go_to_axis(90,12,0,0,-15,0)
    #Dejar pieza
    arm.go_to_axis(90,10,10,0,-22,0)
    #Retirar efector
    arm.go_to_axis(90,-35,52,0,-19,0)
    #Rotar brazo
    arm.go_to_axis(0,-35,52,0,-19,0)
    #FIN
    arm.go_to_axis(0,0,0,0,0,0)
    arm.set_slider_posi(50,2000)


def R2_TNM_Recoger():
    arm.set_speed(1500)
    #INICIO
    arm.go_to_axis(0,0,0,0,0,0)
    #Mover riel
    arm.set_slider_posi(296,2000)
    #Acercar efector y posición
    arm.go_to_axis(90,-35,52,0,-19,0)
    #Meter efector
    arm.go_to_axis(90,10,10,0,-22,0)
    #Recoger pieza
    arm.go_to_axis(90,12,0,0,-15,0)
    #Retirar efector
    arm.go_to_axis(90,-40,50,0,-10,0)
    #Rotar brazo
    arm.go_to_axis(0,-40,50,0,-10,0)
    #Posición P0
    arm.go_to_axis(0,0,0,0,0,0)
    #Mover riel
    arm.set_slider_posi(407,2000)
    #Rotar para evitar colisión
    arm.go_to_axis(-65,0,0,0,0,0)
    #Dejar pieza NFC
    arm.go_to_axis(-70,64,-15.5,-1,-55,6.6)
    sleep(5)
    #Acercar al WLKata
    arm.go_to_axis(-58,14,45,-5.5,-68,-10)
    #Regresar
    arm.go_to_axis(-60,0,0,0,0,0)
    #FIN
    arm.go_to_axis(0,0,0,0,0,0)
    arm.set_slider_posi(50,2000)




while True:
    valor = input('Selecciona una rutina: ')
    if valor.isdigit():
        x=int(valor)
        if x == 0:
            quit()
        elif x == 1:
            R1_TRG_Dejar()
        elif x == 2:
            R1_TRG_Recoger()
        elif x == 3:
            R2_TNM_Dejar()
        elif x == 4:
            R2_TNM_Recoger()
        elif x == 5:
            arm.home_7axis()
        else:
            print("Rutina no válida, intente de nuevo por favor")
    else:
        print("Comando no reconocido, intente de nuevo por favor")







    