import logging
import os

class Log_Maker:
    @staticmethod
    def log_gen():
        # Ensure the 'logs' directory exists
        os.makedirs('./logs', exist_ok=True)

        logging.basicConfig(
            filename='./logs/nopcommerce.log',
            filemode='a',  # Append mode
            format='%(asctime)s: %(levelname)s: %(message)s',
            datefmt='%m/%d/%Y %I:%M:%S %p',
            level=logging.INFO,
            force=True  # <-- Important!
        )
        logger = logging.getLogger()
        return logger
