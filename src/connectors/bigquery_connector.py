"""GCP BigQuery connector."""
import logging,time
from typing import Dict
logger=logging.getLogger(__name__)
class BigQueryConnector:
    name="GCP_BIGQUERY"
    def __init__(self,project:str):
        try:
            from google.cloud import bigquery
            self.client=bigquery.Client(project=project)
            self._available=True
        except Exception as e:
            logger.warning(f"BigQuery unavailable: {e}")
            self._available=False
    def execute(self,sql:str)->Dict:
        if not self._available: return {"rows":[],"cols":[],"count":0,"ms":0,"source":self.name+"_MOCK"}
        t=time.perf_counter()
        results=list(self.client.query(sql).result())
        ms=(time.perf_counter()-t)*1000
        rows=[dict(r) for r in results]
        return {"rows":rows,"cols":list(rows[0].keys()) if rows else [],"count":len(rows),"ms":round(ms,2),"source":self.name}
    def get_cost_estimate(self,sql:str)->float: return len(sql)*0.000003
