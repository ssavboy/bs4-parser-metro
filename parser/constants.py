from pathlib import Path

BASE_DIR = Path(__file__).parent
MAIN_URL = 'https://online.metro-cc.ru/category/'
DT_FORMAT = '%d.%m.%Y %H:%M:%S'
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
LOG_FORMAT = '"%(asctime)s - [%(levelname)s] - %(message)s"'
ENCODING_UTF8 = 'utf-8'
RESULTS = 'results'
DOWNLOADS = 'downloads'
PRETTY_FORMAT = 'pretty'
FILE_FORMAT = 'file'
LOGS = 'logs'
PARSER_FILE = 'parser.log'
DEFAULT_FORMAT = None
GOODS = {
    'coffee': 'chaj-kofe-kakao/kofe?page=1'
}
