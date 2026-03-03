"""Multi-Cloud Data Warehouse
Usage: python main.py [query|sync|demo]
"""
import sys,logging
logging.basicConfig(level=logging.INFO,format="%(asctime)s [%(levelname)s] %(message)s")
logger=logging.getLogger(__name__)
def run_demo():
    from src.connectors.redshift_connector import RedshiftConnector
    from src.connectors.bigquery_connector import BigQueryConnector
    from src.router.query_router import QueryRouter
    connectors={"redshift":RedshiftConnector({}),"bigquery":BigQueryConnector("demo-project")}
    router=QueryRouter(connectors)
    queries=["SELECT COUNT(*) FROM transactions WHERE created_at>=CURRENT_DATE","SELECT user_id,SUM(amount) FROM transactions GROUP BY user_id ORDER BY 2 DESC LIMIT 10"]
    for q in queries:
        result=router.execute(q)
        logger.info(f"Query → {result['source']}: {result['count']} rows in {result['ms']}ms")
    logger.info(f"Routing stats: {router.get_stats()}")
if __name__=="__main__":
    {"demo":run_demo,"query":run_demo}.get(sys.argv[1] if len(sys.argv)>1 else "demo",run_demo)()
