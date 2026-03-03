"""Intelligent query router — picks cheapest/fastest warehouse."""
import logging
from typing import Dict,Optional,List
logger=logging.getLogger(__name__)
class QueryRouter:
    def __init__(self,connectors:Dict):
        self.connectors=connectors
        self.stats={name:{"queries":0,"total_ms":0} for name in connectors}
    def route(self,sql:str,hint:Optional[str]=None)->str:
        if hint and hint in self.connectors: return hint
        costs={name:c.get_cost_estimate(sql) for name,c in self.connectors.items() if hasattr(c,"_available") and c._available}
        if not costs: return list(self.connectors.keys())[0]
        best=min(costs,key=costs.get)
        logger.info(f"Routing to {best} (estimated costs: {costs})")
        return best
    def execute(self,sql:str,target:Optional[str]=None)->Dict:
        name=self.route(sql,hint=target)
        result=self.connectors[name].execute(sql)
        self.stats[name]["queries"]+=1
        self.stats[name]["total_ms"]+=result.get("ms",0)
        return result
    def get_stats(self)->Dict: return self.stats
