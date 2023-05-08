from fastapi import FastAPI
import uvicorn
from fastapi.responses import JSONResponse
import boto3
from aws_session import get_session
import uuid
from botocore.exceptions import ClientError

session = get_session()
s3_client = session.client('s3')

app = FastAPI(
    title="API de gestión de buckets de Amazon S3",
    description="Esta API permite crear y eliminar buckets en Amazon S3 utilizando Boto3 y FastAPI",
    version="1.0.0",
    openapi_url="/api/v1/openapi.json",
    docs_url="/api/v1/docs",
    redoc_url="/api/v1/redoc"
)


@app.post("/create_s3_bucket")
def create_s3_bucket():
    region_name = session.region_name # Obtiene la región del objeto session
    s3 = boto3.resource('s3', region_name=region_name) # Crea un recurso S3 en la región especificada
    bucket_name = f"my-bucket-{str(uuid.uuid4())[:8]}" # Genera un nombre de bucket aleatorio
    try:
        s3.meta.client.head_bucket(Bucket=bucket_name) # Comprueba si el bucket ya existe
        return JSONResponse(content={"message": f"S3 bucket {bucket_name} already exists"})
    except ClientError:
        s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={
            'LocationConstraint': region_name # Especifica la región en la que se debe crear el bucket
        }) # Si no existe, crea el bucket en la región especificada
        return JSONResponse(content={"message": f"S3 bucket {bucket_name} created successfully in {region_name}"})
    

@app.delete("/delete_all_s3_buckets")
def delete_all_s3_buckets():
    response = s3_client.list_buckets()
    buckets = [bucket['Name'] for bucket in response['Buckets']]
    for bucket in buckets:
        try:
            s3 = boto3.resource('s3')
            bucket_to_delete = s3.Bucket(bucket)
            bucket_to_delete.objects.all().delete()
            bucket_to_delete.delete()
            print(f"Bucket {bucket} eliminado correctamente")
        except Exception as e:
            print(f"Error al eliminar el bucket {bucket}: {e}")
    return JSONResponse(content={"message": "Todos los buckets de S3 han sido eliminados correctamente"})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
