from src.generate_map import get_map
from src.lagrance_smoothing import set_lagrance
from src.visualization import make_image
from config.constants import SIDE_LENGTH, MISSING_VALUES, TOLERANCE, STEP_LIMIT_MULTIPLIER
import logging

logging.basicConfig(
  level=logging.INFO,
  filename='src.log',
  filemode='a',
  format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)
logger.info("Package is initialized")


__version__ = "1.0.0"
__date__ = "22-07-2024"
__email__ = "kivancgordu@hotmail.com"
__status__ = "production"

__all__ = [
  'get_map', 'set_lagrance', 'make_image',
  'SIDE_LENGTH', 'MISSING_VALUES', 'TOLERANCE', 'STEP_LIMIT_MULTIPLIER'
  ]
