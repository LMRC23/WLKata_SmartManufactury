##########  Librerias  ##########
from time import sleep
import lib.paho.mqtt.client as mqtt
from wlkata_mirobot import WlkataMirobot
import datetime;

print("connecting...")
arm = WlkataMirobot(portname='COM5')
print("connected... OK")

sleep(1)
print("Starting home routine...")

arm.home()
print("Home routine Done...")


##########  MQTT Parameters  ##########
broker_address = "35.232.221.19"
broker_port = 1883


##########  MQTT Topics  ##########      
topic1 = "/home"           
topic2 = "/zero"                  
topic3 = "/TRG_dejar"
topic4 = "/TRG_recoger"
topic5 = "/TNM_dejar"
topic6 = "/TNM_recoger"


def routine_home():
    arm.home()
    

def routine_zero():
    arm.go_to_axis(0,0,0,0,0,0,0)
    arm.pump_off()


def routine_TRG_dejar():
    arm.set_speed(1000)
    arm.go_to_axis(0,0,0,0,0,0) #INICIO
    sleep(1)
    arm.set_slider_posi(0,speed=1000)
    arm.go_to_axis(-70,70,-18,0,-62,7.5) #Recoger pieza
    sleep(10)
    arm.set_speed(100)
    arm.go_to_axis(-58,14,45,-5.5,-68,-10) #Acercar al WLKata
    sleep(1)
    arm.set_slider_posi(0,speed=500)
    arm.go_to_axis(-58,13.9,45,-5.5,-67.9,-10) #Mover riel
    sleep(1)
    arm.go_to_axis(22,-17,6,3,2,-5) #Subir pieza
    sleep(1)
    arm.go_to_axis(95.3,63.1,288.4,8.7,-8.6,82.4) #Posicionar efector
    sleep(1)
    arm.set_slider_posi(-15,speed=500)
    arm.go_to_axis(68.2,-8.8,-18,1.2,20.1,12.9) #Acercar efector
    sleep(1)
    arm.set_speed(2000)
    arm.go_to_axis(57.8,146.5,303.6,-0.4,-1.9,86.6) #Posicionamiento mejorado
    sleep(1)
    arm.set_speed(100)
    arm.go_to_axis(70.3,20,-53.8,3.6,34.9,14.3) #Colocar pieza
    sleep(1)
    arm.go_to_axis(70,4.7,-21.2,5.8,8.9,15.8) #Dejar pieza
    sleep(1)
    arm.go_to_axis(55.5,-34.1,13.5,7.7,15.1,28.9) #Retirar efector
    sleep(1)
    arm.go_to_axis(44,-40,24,7.5,4,17) #Acercar efector-WLK
    sleep(1)
    arm.go_to_axis(0,-40,24,7.5,4,17) #Rotar a P0
    sleep(1)
    arm.go_to_axis(0,0,0,0,0,0) #P0

def routine_TRG_recoger():
    arm.set_speed(2000)
    arm.set_slider_posi(0,speed=500)
    arm.go_to_axis(0,0,0,0,0,0) #INICIO
    sleep(1)
    arm.go_to_axis(0,-40,24,7.5,4,17) #Rotar a P0
    sleep(1)
    arm.go_to_axis(44,-40,24,7.5,4,17) #Acercar efector-WLK
    sleep(1)
    arm.go_to_axis(55.5,-34.1,13.5,7.7,15.1,28.9) #Colocar efector
    sleep(1)
    arm.set_slider_posi(-10,speed=500)
    arm.go_to_axis(70,4.7,-21.2,5.8,8.9,15.8) #Recoger pieza
    sleep(1)
    arm.go_to_axis(70.3,20,-53.8,3.6,34.9,14.3) #Subir pieza
    sleep(1)
    arm.set_slider_posi(-15,speed=500)
    arm.go_to_axis(68.2,-8.8,-18,1.2,20.1,12.9) #Retirar efector
    sleep(1)
    arm.go_to_axis(22,-17,6,3,2,-5) #Bajar pieza
    sleep(1)
    arm.set_slider_posi(0,speed=500)
    arm.go_to_axis(-58,13.9,45,-5.5,-67.9,-10) #Mover riel
    sleep(1)
    arm.go_to_axis(-58,14,45,-5.5,-68,-10) #Retirar del WLK
    sleep(1)
    arm.set_slider_posi(0,speed=500)
    arm.go_to_axis(-70,70,-18,0,-62,7.5) #RFID
    sleep(1)
    arm.go_to_axis(0,0,0,0,0,0) #FIN

def routine_TNM_dejar():
    arm.set_speed(2000)
    arm.set_slider_posi(0,speed=500)
    arm.go_to_axis(0,0,0,0,0,0) #INICIO
    sleep(1)
    arm.set_slider_posi(0,speed=500)
    arm.go_to_axis(-74,60.7,-8.4,0,-52.2,14.1) #Recoger pieza
    sleep(1)
    arm.set_slider_posi(0,speed=500)
    arm.go_to_axis(-64.3,8.1,48.8,0,-56.9,4.4) #Acercar al brazo
    sleep(1)
    arm.go_to_axis(-64.2,-24.7,37.3,0,-12.5,4.4) #Subir pieza
    sleep(1)
    arm.go_to_axis(34.4,-38.3,46.5,0,-8.1,5.9) #Rotar WLK
    sleep(1)
    arm.set_slider_posi(-114,speed=500)
    arm.go_to_axis(84.3,-36.2,31.8,0,4.4,5.9) #Seguir rotando
    sleep(1)
    arm.go_to_axis(86.1,-2.1,4.7,0.3,-7.6,4) #Calibrar efector
    sleep(1)
    arm.go_to_axis(85.3,-2,4.7,0.4,-7.7,4.8) #Colocar efector
    sleep(1)
    arm.go_to_axis(85.3,-1.9,13.2,0.4,-16.2,4.8) #Dejar pieza
    sleep(1)
    arm.go_to_axis(83,-39.3,42.5,0.5,-8,6.9) #Retirar efector
    sleep(1)
    arm.go_to_axis(0,-39.3,42.5,0.5,-8,6.9) #Rotar WLK
    sleep(1)
    arm.set_slider_posi(0,speed=500)
    arm.go_to_axis(0,0,0,0,0,0) #FIN

def routine_TNM_recoger():
    arm.set_speed(2000)
    arm.set_slider_posi(0,speed=500)
    arm.go_to_axis(0,0,0,0,0,0) #INICIO
    sleep(1)
    arm.go_to_axis(0,-39.3,42.5,0.5,-8,6.9) #Rotar WLK
    sleep(1)
    arm.set_slider_posi(-114,speed=500)
    arm.go_to_axis(83,-39.3,42.5,0.5,-8,6.9) #Mover riel
    sleep(1)
    arm.go_to_axis(85.3,-1.9,13.2,0.4,-16.2,4.8) #Posicionar efector
    sleep(1)
    arm.go_to_axis(85.3,-2,4.9,0.4,-7.8,4.7) #Subir efector
    sleep(1)
    arm.go_to_axis(83,-37.4,32.9,0.5,-0.4,6.9) #Retirar efector
    sleep(1)
    arm.go_to_axis(84.3,-36.2,31.8,0,4.4,5.9) #Seguir
    sleep(1)
    arm.go_to_axis(34.3,-38.3,46.5,0,-8.1,5.9) #Rotar WLK
    sleep(1)
    arm.go_to_axis(-64.2,-24.7,37.3,0,-12.5,4.4) #Subir pieza
    sleep(1)
    arm.go_to_axis(-64.3,8.1,48.8,0,-56.9,4.4) #Retirar
    sleep(1)
    arm.set_slider_posi(0,speed=500)
    arm.go_to_axis(-74,60.7,-8.4,0,-52.2,14.1) #RFID
    sleep(1)
    arm.go_to_axis(0,0,0,0,0,0) #FIN
    
##########  Funciones  ##########
def on_message_msgs(client, userdata, message):      
    if message.topic == topic1:
        var1 =  message.payload.decode("utf-8")
        print(var1)
        routine_home()

    if message.topic == topic2:
        var1 =  message.payload.decode("utf-8")
        print(var1)
        routine_zero()

    if message.topic == topic3:
        var1 =  message.payload.decode("utf-8")
        print(var1)
        routine_TRG_dejar()
    
    if message.topic == topic4:
        var1 =  message.payload.decode("utf-8")
        print(var1)
        routine_TRG_recoger()

    if message.topic == topic5:
        var1 =  message.payload.decode("utf-8")
        print(var1)
        routine_TNM_dejar()
    
    if message.topic == topic6:
        var1 =  message.payload.decode("utf-8")
        print(var1)
        routine_TNM_recoger()

        
        #routine_BC(var1)
    


##########  Funcion main (Loop)  ##########
if __name__ == '__main__':
    while (True):
        client = mqtt.Client('Robot2') 
        client.on_message = on_message_msgs
        client.connect(broker_address, broker_port, 60) 
        client.subscribe(topic1)
        client.subscribe(topic2)
        client.subscribe(topic3)
        client.subscribe(topic4)
        client.subscribe(topic5)
        client.subscribe(topic6)

        client.message_callback_add(topic1, on_message_msgs)
        client.message_callback_add(topic2, on_message_msgs)
        client.message_callback_add(topic3, on_message_msgs)
        client.message_callback_add(topic4, on_message_msgs)
        client.message_callback_add(topic5, on_message_msgs)
        client.message_callback_add(topic6, on_message_msgs)
        client.loop_forever()