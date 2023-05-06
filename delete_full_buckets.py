import boto3
from aws_session import get_session

session = get_session()

# Creación de un cliente de servicio
s3 = session.client('s3')

# Obtener la lista de buckets
response = s3.list_buckets()
buckets = [bucket['Name'] for bucket in response['Buckets']]

# Eliminación de los buckets con contenido
for bucket in buckets:
    try:
        objects = s3.list_objects(Bucket=bucket)
        if 'Contents' in objects:
            delete_keys = {'Objects': []}
            for obj in objects['Contents']:
                delete_keys['Objects'].append({'Key': obj['Key']})
            s3.delete_objects(Bucket=bucket, Delete=delete_keys)
            print(f"Contenido del bucket {bucket} eliminado correctamente")
        else:
            print(f"El bucket {bucket} está vacío, se procederá a eliminar")
        s3.delete_bucket(Bucket=bucket)
        print(f"Bucket {bucket} eliminado correctamente")
    except s3.exceptions.BucketNotEmpty:
        print(f"El bucket {bucket} no está vacío, no se puede eliminar")