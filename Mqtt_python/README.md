# MQTT

Temos uma stack rodando via docker-compose com:

- eclipse-mosquitto broker
- python clients

Essa solucao contem 4 servicos:

- broker
- alarm (detecta e dispara alarms para o monitor)
- cat (calcula a media temeperatura dos sensores a cada 60 seg)
- sensor (coleta a temperatura dos senores)

### Para executar

```
docker-compose up
```