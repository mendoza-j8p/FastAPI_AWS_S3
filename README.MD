# Proyecto FastAPI con AWS S3

Este proyecto utiliza FastAPI y Boto3 para crear un bucket de AWS S3 en una región específica. El nombre del bucket se genera aleatoriamente y se comprueba si ya existe antes de crearlo.

## Configuración

1. Descargue el proyecto en su ordenador.
2. Configure sus credenciales de AWS en su entorno local para que Boto3 pueda acceder a su cuenta. Para hacerlo, siga las instrucciones en la **documentación oficial de AWS.**
3. Instale los paquetes necesarios utilizando el comando **pip install -r requirements.txt**

## Ejecución

- Ejecute el archivo **main.py** con el comando **python main.py**
- Envíe una solicitud POST al endpoint **http://localhost:8000/create_s3_bucket** con un body vacío.

## Estos los pasos para utilizar la API que creamos anteriormente para crear un bucket de AWS utilizando Postman

- Abre la aplicación de Postman.

- Crea una nueva solicitud haciendo clic en el botón "New" en la esquina superior izquierda y selecciona "Request".

- En la ventana que se abre, en la pestaña "General", establece el método en "POST".

- En la pestaña "Body", selecciona "raw" y establece el tipo de cuerpo en "JSON".

- En la sección de cuerpo, dejalo vací  o.

- En la pestaña "Headers", agrega un encabezado con la clave "Content-Type" y el valor "application/json".

- En la pestaña "Authorization", si es necesario, configura las credenciales de AWS para permitir que la solicitud de creación de instancia de EC2 se autorice correctamente. Puedes hacerlo seleccionando "AWS Signature" como el tipo de autorización y agregando tus credenciales de acceso y secretos de acceso.

- Haz clic en "Send" para enviar la solicitud.

- Si el bucket se crea exitosamente, recibirá una respuesta en formato JSON que indica que se creó el bucket satisfactoriamente en la región correspondiente. Si el bucket ya existe, recibirá una respuesta que indica que el bucket ya existe. Si hay algún error, recibirá una respuesta que indica el tipo de error que ocurrió.

Si la solicitud se procesa correctamente y se crea unun bucket, deberías ver una respuesta con un mensaje de éxito, el nombre del bucket y la region donde se ha creado. Si no se crea un bucket, recibirás un mensaje de error en la respuesta.
