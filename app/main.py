from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from .router import localAPI
import uvicorn

app = FastAPI()

# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # List your allowed origins here
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(localAPI.router)

if __name__ == '__main__':
	
	config = uvicorn.Config("main:app", port=3000, log_level="info")
	server = uvicorn.Server(config)
	server.run()
