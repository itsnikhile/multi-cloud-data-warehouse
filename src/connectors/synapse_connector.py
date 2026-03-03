"""Azure Synapse connector."""
import logging,time
from typing import Dict
logger=logging.getLogger(__name__)
class SynapseConnector:
    name="AZURE_SYNAPSE"
    def __init__(self,connection_string:str):
        try:
            import pyodbc
            self.conn=pyodbc.connect(connection_string)
            self._available=True
        except Exception as e:
            logger.warning(f"Synapse unavailable: {e}")
            self._available=False
    def execute(self,sql:str)->Dict:
        if not self._available: return {"rows":[],"cols":[],"count":0,"ms":0,"source":self.name+"_MOCK"}
        t=time.perf_counter()
        cur=self.conn.cursor()
        cur.execute(sql)
        cols=[d[0] for d in cur.description]
        rows=[dict(zip(cols,r)) for r in cur.fetchall()]
        ms=(time.perf_counter()-t)*1000
        return {"rows":rows,"cols":cols,"count":len(rows),"ms":round(ms,2),"source":self.name}
    def get_cost_estimate(self,sql:str)->float: return len(sql)*0.000004
