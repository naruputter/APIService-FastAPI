from ..helper import *

router = APIRouter(prefix="")

@router.get("/")
async def get_local_api():

	return_data = { 'code' : 200 , 'data' : "get" , 'desc' : "success"}

	return return_data