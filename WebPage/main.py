from fastapi import FastAPI ,File,UploadFile
import uvicorn
import aiofiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():

    return {}


@app.post("/upload-file")#file kopyalama tek tek okunarak yapılıyormuş
async def upload_file(file : UploadFile = File(...)):
    print("file = ", file.filename)#getting filename
    destination="/home/"#Rasbery in içinde konumlanacağı yer
    async with aiofiles.open(destination, 'wb') as out_file:
        while content := await file.read(1024):  # async read file chunk
            await out_file.write(content)  # async write file chunk

    return {"Result" :"Başarıyla Yüklendi"}

