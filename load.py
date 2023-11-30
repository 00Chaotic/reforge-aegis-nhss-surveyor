import logging
import os

from config import appname
from typing import Any, Dict, Optional

# Must be the name of the folder
PLUGIN_NAME = os.path.basename(os.path.dirname(__file__))

logger = logging.getLogger(f'{appname}.{PLUGIN_NAME}')

# Needed for EDMC versions older than 4.1.0-beta
if not logger.hasHandlers():
    logger.setLevel(logging.INFO)
    logger_channel = logging.StreamHandler()
    logger_formatter = logging.Formatter(f'%(asctime)s - %(name)s - %(levelname)s - %(module)s:%(lineno)d:%(funcName)s: %(message)s')
    logger_formatter.default_time_format = '%Y-%m-%d %H:%M:%S'
    logger_formatter.default_msec_format = '%s.%03d'
    logger_channel.setFormatter(logger_formatter)
    logger.addHandler(logger_channel)

# Main plugin function
def plugin_start3(plugin_dir: str) -> str:
  return PLUGIN_NAME

# Hook for new journal entries
def journal_entry(
    cmdr: str, is_beta: bool, system: str, station: str, entry: Dict[str, Any], state: Dict[str, Any]
) -> Optional[str]:
  if entry['event'] == 'FSSSignalDiscovered' and entry['SignalName'] == '$USS_NonHumanSignalSource;':
    # TODO: replace with code to update spreadsheet
    logger.info("An NHSS was scanned!")

  return
