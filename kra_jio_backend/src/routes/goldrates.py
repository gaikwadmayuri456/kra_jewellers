from fastapi import APIRouter, Depends, HTTPException
import psycopg2.extras
from . import get_raw_db
from sqlalchemy.orm import Session
from loguru import logger

router = APIRouter()


@router.get("/goldrate", tags=["Rate"])
async def get_goldrate(rdb: Session = Depends(get_raw_db)):
    try:
        # myres = rdb.query(
        #     """select amount ,product_name from kra_jio_integration.public.rates_live where rate_type ='sale' group by product_name, amount""")
        # myres=rdb.fetchall()
        cursor = rdb.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        # query for session_details
        query = f"""select amount ,product_name 
        from kra_jio_integration.public.rates_live 
        where rate_type ='sale' 
        ORDER BY "product_name" ASC  
        """
        cursor.execute(query)
        session_details = cursor.fetchall()
        return session_details
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.debug(f"{e}")
        raise HTTPException(status_code=500, detail=f"{e}")
