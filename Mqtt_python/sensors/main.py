from threading import ExceptHookArgs
from time import sleep
import random
import paho.mqtt.client as mqtt
import sys

def connect_broker(host="", port=1883, topic=""):

    client = mqtt.Client(client_id="monitor", clean_session=True, userdata=None, protocol=mqtt.MQTTv311, transport="tcp")

    try:        
        client.connect(host, port)
        client.loop_start()

        while True:
            temperature = random.triangular(165., 171.) * random.uniform(1.1, 1.2)
            client.publish(topic, temperature)
            sleep(2)
    except Exception as e:
        print(e)
        exit(-1)

if __name__ == "__main__":    
    host = sys.argv[1]
    port = sys.argv[2]
    topic = sys.argv[3]

    print("initializing sensor ...")

    for i in range(5):
        try:
            connect_broker(host=host, port=int(port), topic=topic)
        except:
            pass
        sleep(5)

