from ..helper import *

router = APIRouter(prefix="")

@router.get("/")
async def get_local_api():

	return_data = { 'code' : 200 , 'data' : None , 'desc' : "get"}

	return return_data

@router.post("/")
async def get_local_api(payload: Optional[dict] = None):

	return_data = { 'code' : 200 , 'data' : payload , 'desc' : "post"}

	return return_data

@router.put("/")
async def get_local_api(payload: Optional[dict] = None):

	return_data = { 'code' : 200 , 'data' : payload , 'desc' : "put"}

	return return_data