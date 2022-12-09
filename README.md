# Practica-Sockets
Práctica 1 Arquitecturas Avanzadas.

El objetivo de esta práctica es simular comunicación asíncrona entre agentes a través de un canal compartido.
La idea es implementar 4 agentes. Donde 3 de ellos ayudan a un cuarto que pide ayuda.
Se considerara que ese agente ha sido ayudado cuando 2 de los otros le han dado ayuda.

Para utilizar el proyecto se deberá ejecutar en una terminal el programa server.py, que será el agente que pide ayuda, y en otras 3 terminales se deberá ejecutar el programa client.py, que serán los agentes que brindan ayuda.
Una vez lanzados, el servidor enviará 20 mensajes de ayuda y, una vez terminada la ejecución, por terminal obtendremos el grado de ayuda recibido por parte de los clientes.
