from utils.logger import setup_logger
from agents.household import Household
from agents.base_agent import BaseAgent

def main():
    # Create a dummy agent for testing
    logger = setup_logger("macro_ai_abm")
    logger.info("Starting simulation...")
    
    dummy_agent = BaseAgent(1, None)
    household_dummy = Household(2, None)
    
    logger.info("Simulation completed.")

if __name__ == "__main__":
    main()

