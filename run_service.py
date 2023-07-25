import os
import uvicorn

# START_COMMAND = "uvicorn app.main:app --host 0.0.0.0 --port8080"
# os.system(START_COMMAND)

if __name__ == '__main__':
	uvicorn.run("app.main:app", host="localhost", port=4000)