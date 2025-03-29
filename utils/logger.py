import logging
import sys
import os

def setup_logger(logger_name: str, log_file: str = "logs/app.log", level: int = logging.DEBUG) -> logging.Logger:
    """
    Sets up and returns a logger that outputs to both a file and stdout.
    
    Args:
        logger_name (str): Name of the logger.
        log_file (str): Path to the log file.
    
    Returns:
        logging.Logger: Configured logger instance.
    """
    # Create or get the logger
    logger = logging.getLogger()
    logger.setLevel(level)

    # Create handlers
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(logging.INFO)

    # Create a formatter and attach it to the handlers
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)
    
    # Avoid adding duplicate handlers
    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)
        
    logger.info(f"Logger configured successfully. Using log file: {log_file}")
    return logger

# Example usage:
if __name__ == "__main__":
    # Configure the logger
    logger = setup_logger("my_logger", "app.log")
    
    # Log sample messages
    logger.info("Logger configured successfully. This is an info message.")
    logger.error("This is an error message.")
