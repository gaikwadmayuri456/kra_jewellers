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
        query = f"""select t1.product_name as product_name,t1.updated_at as updated,
       t1.amount as sale_amount, t2.amount as purchase_amount from
(select  product_name,amount,updated_at
        from kra_jio_integration.public.rates_live
        where rate_type = 'sale'
        --ORDER BY "product_name" ASC
group by product_name, amount,updated_at) as t1 left join
(select  product_name,amount,updated_at
        from kra_jio_integration.public.rates_live
        where rate_type = 'purchase'
        --ORDER BY "product_name" ASC
group by product_name, amount,updated_at
) as t2 on t1.product_name= t2.product_name
        """
        cursor.execute(query)
        session_details = cursor.fetchall()
        return session_details
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.debug(f"{e}")
        raise HTTPException(status_code=500, detail=f"{e}")
