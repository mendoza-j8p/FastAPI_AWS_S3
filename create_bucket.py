from fastapi import FastAPI
import uvicorn
from fastapi.responses import JSONResponse
import boto3
from aws_session import get_session
import uuid
from botocore.exceptions import ClientError

session = get_session()
s3_client = session.client('s3')

app = FastAPI()

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

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)






if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)