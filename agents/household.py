from .base_agent import BaseAgent
import logging

logger = logging.getLogger(__name__)

## Base class for agents which represent households in the economy
class Household(BaseAgent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.name = "Household"
        
        logger.debug(f"Created agent {self.name} with ID {self.unique_id}")
        
    def step(self):
        raise NotImplementedError()
