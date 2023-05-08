
##########  Librerias  ##########
from time import sleep
import lib.paho.mqtt.client as mqtt
from wlkata_mirobot import WlkataMirobot
import datetime;

print("connecting...")
arm = WlkataMirobot(portname='COM6')
print("connected... OK")

sleep(1)
print("Starting home routine...")

arm.home()
print("Home routine Done...")


##########  MQTT Parameters  ##########
broker_address = "35.232.221.19"
broker_port = 1883


##########  MQTT Topics  ##########
topic1 = "/R0_flag"         #subscriber
topic2 = "/home"           #publisher
topic3 = "/zero"                  #publisher
topic0 = "/recepcion"
topic4 = "/pick_routine"
topic5 = "TRG_dejar"
topic6 = "TRG_recoger"
topic7 = "TNM_dejar"
topic8 = "TNM_recoger"

routine_list = [0]

positions_routine0 = [[0,0,0,0,0,0,0],[10,5,5,10,5,5,10],[20,15,0,15,10,20,20],[0,0,0,0,0,0,0]]
positions_routine1 = [[0,0,0,0,0,0,0],[-10,15,0,10,5,15,30],[-20,15,0,15,10,20,50],[0,0,0,0,0,0,0]]

def routine(routine_no):
    
    if routine_no == 0:
        positions = positions_routine0
        routine_list.append(1)

    if routine_no == 1:
        positions = positions_routine1
        routine_list.append(0)
    
    for i in positions:
        arm.go_to_axis(i[0],i[1],i[2],i[3],i[4],i[5],i[6])
        current_time = datetime.datetime.now()
        time_stamp = current_time + datetime.timedelta(hours=6)
        r1_information_t = "2,"+str(i[0]) + ","+str(i[1]) + ","+str(i[2]) + ","+str(i[3]) + ","+str(i[4]) + ","+str(i[5]) + ","+str(i[6]) + ","+str(routine_no) + "," + str(time_stamp)        
        #r1_information = "1,"+str(i[0]) + ","+str(i[1]) + ","+str(i[2]) + ","+str(i[3]) + ","+str(i[4]) + ","+str(i[5]) + ","+str(i[6]) + ","+str(routine_no)
        sleep(1)
        client.publish(topic2,r1_information_t)
        sleep(1)
        print(r1_information_t)
        client.publish(topic3,"R2")
        sleep(1)
        
def routine_BC(str1):
    vector1 = str1.split(",")
    Ro =int(vector1[0])
    J1=int(vector1[1])
    J2=int(vector1[2])
    J3=int(vector1[3])
    J4=int(vector1[4])
    J5=int(vector1[5])
    J6=int(vector1[6])
    J7=int(vector1[7])
        
    arm.go_to_axis(J1,J2,J3,J4,J5,J6,J7)
    current_time = datetime.datetime.now()
    current_time = current_time.replace(microsecond=0)
    print(current_time)
  

def routine_home():
    arm.home()
    

def routine_zero():
    arm.go_to_axis(0,0,0,0,0,0,0)
    arm.pump_off()

def routine_pick():
    arm.go_to_axis(0,0,0,0,0,0,0)
    arm.pump_off()
    sleep(1)
    arm.go_to_axis(-43.1,41,7.7,0,-53.7,-1.6,0)
    sleep(1)
    arm.pump_on()
    sleep(1)
    arm.go_to_axis(-43.1,14.6,-10.5,0,-9,-1.5,0)
    sleep(1)
    arm.go_to_axis(0,0,0,0,0,0,0)
    sleep(1)
    arm.go_to_axis(0,40.8,20.6,0,-61.5,0,0)
    sleep(1)
    arm.pump_off()
    sleep(1)
    arm.go_to_axis(0,0,0,0,0,0,0)
        
def routine_TRG_dejar():
    arm.set_speed(1000)
    arm.go_to_axis(0,0,0,0,0,0) #INICIO
    sleep(1)
    arm.go_to_axis(-70,70,-18,0,-62,7.5) #Recoger pieza
    arm.set_slider_posi(0,speed=1000)
    sleep(10)
    arm.set_speed(100)
    arm.go_to_axis(-58,14,45,-5.5,-68,-10) #Acercar al WLKata
    sleep(1)
    arm.go_to_axis(-58,13.9,45,-5.5,-67.9,-10) #Mover riel
    arm.set_slider_posi(0,speed=500)
    sleep(1)
    arm.go_to_axis(22,-17,6,3,2,-5) #Subir pieza
    sleep(1)
    arm.go_to_axis(95.3,63.1,288.4,8.7,-8.6,82.4) #Posicionar efector
    sleep(1)
    arm.go_to_axis(68.2,-8.8,-18,1.2,20.1,12.9) #Acercar efector
    arm.set_slider_posi(-15,speed=500)
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
    arm.go_to_axis(0,0,0,0,0,0) #INICIO
    arm.set_slider_posi(0,speed=500)
    sleep(1)
    arm.go_to_axis(0,-40,24,7.5,4,17) #Rotar a P0
    sleep(1)
    arm.go_to_axis(44,-40,24,7.5,4,17) #Acercar efector-WLK
    sleep(1)
    arm.go_to_axis(55.5,-34.1,13.5,7.7,15.1,28.9) #Colocar efector
    sleep(1)
    arm.go_to_axis(70,4.7,-21.2,5.8,8.9,15.8) #Recoger pieza
    arm.set_slider_posi(-10,speed=500)
    sleep(1)
    arm.go_to_axis(70.3,20,-53.8,3.6,34.9,14.3) #Subir pieza
    sleep(1)
    arm.go_to_axis(68.2,-8.8,-18,1.2,20.1,12.9) #Retirar efector
    arm.set_slider_posi(-15,speed=500)
    sleep(1)
    arm.go_to_axis(22,-17,6,3,2,-5) #Bajar pieza
    sleep(1)
    arm.go_to_axis(-58,13.9,45,-5.5,-67.9,-10) #Mover riel
    arm.set_slider_posi(0,speed=500)
    sleep(1)
    arm.go_to_axis(-58,14,45,-5.5,-68,-10) #Retirar del WLK
    sleep(1)
    arm.go_to_axis(-70,70,-18,0,-62,7.5) #RFID
    arm.set_slider_posi(0,speed=500)
    sleep(1)
    arm.go_to_axis(0,0,0,0,0,0) #FIN

def routine_TNM_dejar():
    arm.go_to_axis()
    sleep(1)
    arm.go_to_axis()
    sleep(1)
    arm.go_to_axis()
    sleep(1)
    arm.go_to_axis()
    sleep(1)
    arm.go_to_axis()
    sleep(1)
    arm.go_to_axis()
    sleep(1)
    arm.go_to_axis()
    sleep(1)
    arm.go_to_axis()
    sleep(1)
    arm.go_to_axis()
    sleep(1)
    arm.go_to_axis()
    sleep(1)
    arm.go_to_axis()
    sleep(1)
    arm.go_to_axis()

def routine_TNM_recoger():
    arm.go_to_axis()
    sleep(1)
    arm.go_to_axis()
    sleep(1)
    arm.go_to_axis()
    sleep(1)
    arm.go_to_axis()
    sleep(1)
    arm.go_to_axis()
    sleep(1)
    arm.go_to_axis()
    sleep(1)
    arm.go_to_axis()
    sleep(1)
    arm.go_to_axis()
    sleep(1)
    arm.go_to_axis()
    sleep(1)
    arm.go_to_axis()
    sleep(1)
    arm.go_to_axis()
    sleep(1)
    arm.go_to_axis()
    


##########  Funciones  ##########
def on_message_msgs(client, userdata, message):
    if message.topic == topic1:
        var1 =  message.payload.decode("utf-8")
        if var1 == "R1":
            print("Topico: " + topic1 +"; Payload: " + str(var1) +"\n")
            sleep(3)
            number = routine_list[-1]
            print("rutina numero: " + str(number))
            routine(number)
         

    if message.topic == topic0:
        var1 =  message.payload.decode("utf-8")
        
        print(var1)
        vector0 = var1.split(";")
        print(len(vector0))
        for i in vector0:
            print("Posiciones: ")
            print(i)
            print(" ")
            routine_BC(i)
            


    if message.topic == topic2:
        var1 =  message.payload.decode("utf-8")
        print(var1)
        routine_home()

    if message.topic == topic3:
        var1 =  message.payload.decode("utf-8")
        print(var1)
        routine_zero()

    if message.topic == topic4:
        var1 =  message.payload.decode("utf-8")
        print(var1)
        routine_pick()

    if message.topic == topic5:
        var1 =  message.payload.decode("utf-8")
        print(var1)
        routine_TRG_dejar()
    
    if message.topic == topic6:
        var1 =  message.payload.decode("utf-8")
        print(var1)
        routine_TRG_recoger()

    if message.topic == topic7:
        var1 =  message.payload.decode("utf-8")
        print(var1)
        routine_TNM_dejar()
    
    if message.topic == topic8:
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
        client.subscribe(topic0)
        client.subscribe(topic2)
        client.subscribe(topic3)
        client.subscribe(topic4)
        client.subscribe(topic5)
        client.subscribe(topic6)
        client.subscribe(topic7)
        client.subscribe(topic8)  
    
        client.message_callback_add(topic0, on_message_msgs)
        client.message_callback_add(topic1, on_message_msgs)
        client.message_callback_add(topic2, on_message_msgs)
        client.message_callback_add(topic3, on_message_msgs)
        client.message_callback_add(topic4, on_message_msgs)
        client.message_callback_add(topic5, on_message_msgs)
        client.message_callback_add(topic6, on_message_msgs)
        client.message_callback_add(topic7, on_message_msgs)
        client.message_callback_add(topic8, on_message_msgs)
      
        client.loop_forever()

