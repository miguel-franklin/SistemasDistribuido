from threading import ExceptHookArgs
from time import sleep
import paho.mqtt.client as mqtt


# The callback for when a PUBLISH message is received from the server.
def __on_message(client, userdata, msg):
    # Trata o topico temperature    
    print(str(msg.payload))

# The callback for when the client receives a CONNACK response from the server.
def __on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Aassim que a conexao ocorre assina o topico no padrao iot/#
    # Esse padrao comporta qualquer topico no formato iot/(qualquer valor)
    client.subscribe("iot/alarm")

def subscribe():
    data = []

    # instancia cliente
    client = mqtt.Client()

    # defini handle para conexao
    client.on_connect = __on_connect

    # defini handle para recebimento
    client.on_message = __on_message

    # conectar ao broker
    client.connect("broker", 1883, 60)

    # Blocking call that processes network traffic, dispatches callbacks and
    # handles reconnecting.
    # Other loop*() functions are available that give a threaded interface and a
    # manual interface.
    client.loop_forever()


if __name__ == "__main__":
    print("initializing alarm ...")

    for i in range(5):
        try:
            subscribe()
        except:
            pass
        sleep(5)