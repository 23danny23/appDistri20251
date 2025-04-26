import pika

# Configuración de conexión a RabbitMQ  uvicorn app.main:app --reload
RABBITMQ_CONFIG = {
    "username": "admin",
    "password": "admin",
    "virtualHost": "/",
    "port": 5672,
    "hostname": "localhost"
}

def get_rabbitmq_connection():
    credentials = pika.PlainCredentials(
        username=RABBITMQ_CONFIG["username"],
        password=RABBITMQ_CONFIG["password"]
    )
    parameters = pika.ConnectionParameters(
        host=RABBITMQ_CONFIG["hostname"],
        port=RABBITMQ_CONFIG["port"],
        virtual_host=RABBITMQ_CONFIG["virtualHost"],
        credentials=credentials
    )
    return pika.BlockingConnection(parameters)

def callback(ch, method, properties, body):
    print("Mensaje recibido:")
    print(body.decode())  # Aquí puedes hacer procesamiento adicional
    ch.basic_ack(delivery_tag=method.delivery_tag)

def consume_messages(queue_name='facturaMensaje'):
    connection = get_rabbitmq_connection()
    channel = connection.channel()

    # Declarar la cola en caso de que no exista
    channel.queue_declare(queue=queue_name, durable=True)

    print(f"🔄 Esperando mensajes en la cola '{queue_name}'... Presiona CTRL+C para salir")
    channel.basic_consume(queue=queue_name, on_message_callback=callback)

    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        print("Finalizado por el usuario.")
        channel.stop_consuming()
        connection.close()


if __name__ == '__main__':
    consume_messages()
