import paho.mqtt.client as mqtt
import statistics, time, json, sys, traceback, queue, math

queue = queue.Queue(4)

def handle_over_200(client, actual_reading):
    if actual_reading > 200:
        client.publish("iot/alarm", "over 200 degrees")

def handle_avg(client, actual_reading):
    queue.put(actual_reading)

    if queue.full():
        firstAvg = statistics.mean(list(queue.queue)[0:2])
        secondAvg = statistics.mean(list(queue.queue)[2:4])
        queue.get()
        queue.get()
        if abs(firstAvg - secondAvg) > 5:
            client.publish("iot/alarm", "Median temperature: {0} diverges over 5 degrees".format(round(firstAvg - secondAvg, 2)))

def temp_handle(client, msg):
    print(msg.topic+" "+str(msg.payload))
    actual_reading = float(msg.payload)
    handle_avg(client, actual_reading)
    handle_over_200(client, actual_reading)

# The callback for when a PUBLISH message is received from the server.
def __on_message(client, userdata, msg):
    # Trata o topico temperature
    if msg.topic == "iot/temperature":
        temp_handle(client, msg)


# The callback for when the client receives a CONNACK response from the server.
def __on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Aassim que a conexao ocorre assina o topico no padrao iot/#
    # Esse padrao comporta qualquer topico no formato iot/(qualquer valor)
    client.subscribe("iot/#")

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
    print("initializing monitor ...")

    for i in range(5):
        try:
            subscribe()
        except:
            pass
        time.sleep(5)