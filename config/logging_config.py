import os 
import logging

def get_logger(name: str) -> logging.Logger:
    """
    Create and configure a logger instance.

    Args:
        name (str): The name of the logger.
    Returns:
        logging.Logger: Configured logger instance.
    """

    # Create logs directory if it doesn't exist
    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger(name)

    # prevent adding multiple handlers to the logger if it already has handlers
    if logger.hasHandlers():
        return logger
    
    logger.setLevel(logging.DEBUG)

    # Extract module name from the logger name
    module_name = name.split('.')[-1]

    # Log file path 
    log_file_path = os.path.join("logs", f"{module_name}.log")

    # File Handler 
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setLevel(logging.DEBUG)

    # Console Handler 
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Log Format 
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add Handlers to Logger 
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger