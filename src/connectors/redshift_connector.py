"""AWS Redshift connector."""
import logging,time
from typing import Dict,List
logger=logging.getLogger(__name__)
class RedshiftConnector:
    name="AWS_REDSHIFT"
    def __init__(self,config:dict):
        try:
            import redshift_connector
            self.conn=redshift_connector.connect(**config)
            self._available=True
        except Exception as e:
            logger.warning(f"Redshift unavailable: {e}")
            self._available=False
    def execute(self,sql:str)->Dict:
        if not self._available: return self._mock(sql)
        t=time.perf_counter()
        cur=self.conn.cursor()
        cur.execute(sql)
        cols=[d[0] for d in cur.description]
        rows=[dict(zip(cols,r)) for r in cur.fetchall()]
        ms=(time.perf_counter()-t)*1000
        return {"rows":rows,"cols":cols,"count":len(rows),"ms":round(ms,2),"source":self.name}
    def get_cost_estimate(self,sql:str)->float: return len(sql.split())*0.000005
    def _mock(self,sql): return {"rows":[],"cols":[],"count":0,"ms":0,"source":self.name+"_MOCK"}
