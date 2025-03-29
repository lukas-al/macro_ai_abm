import logging

logger = logging.getLogger(__name__)

class BaseAgent:
    def __init__(self, unique_id, model):
        self.unique_id = unique_id
        self.name = None
        self.model = model
        self.schedule = None
        
        logger.debug(f"Created agent {self.name} with ID {self.unique_id}")
        
    def step(self):
        raise NotImplementedError("Subclasses must implement this method.")
    
    def __repr__(self):
        return f"Agent of type {self.name}. Unique ID: {self.unique_id}"