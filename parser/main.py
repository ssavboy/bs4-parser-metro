import logging

from urllib.parse import urljoin

from requests_cache import CachedSession
from tqdm import tqdm

from configs import configure_argument_parser, configure_logging
from constants import (MAIN_URL, GOODS)
from outputs import control_output
from utils import get_soup, Deferred, cleared_string

ARGUMENTS_CLI = 'Аргументы командной строки: {args}'
PARSER_ERROR = 'Ошибка в работе парсера: {error}'
STARTER_PARSER = 'Парсер запущен!'
ENDING_PARSER = 'Парсер завершил работу.'

def coffee(session):
    deffered = Deferred()
    results = [('Название', 'Цена со кидкой', 'Цена без скидки', 'Ссылка',)]
    pages = int(get_soup(session, urljoin(MAIN_URL, GOODS.get('coffee'))).select('.catalog-paginate > li')[-2].text)
    for page in range(1):
        coffee_url = urljoin(MAIN_URL, f'chaj-kofe-kakao/kofe?page={page + 1}')
        for section in tqdm(
            get_soup(
                session,
                coffee_url
            ).select(
                '#products-inner .product-card__content'
            )
        ):
            if section.find(attrs={'class': 'product-price__sum-rubles'}) is None: break
            name = section.find('a', attrs={'class': 'product-card-name'}).text
            url = urljoin(MAIN_URL, section.find('a', attrs={'class': 'product-card-name'})['href'])
            sale_price = section.find(attrs={'class': 'product-price__sum-rubles'}).text
            original_price = section.find(attrs={'class': 'product-unit-prices__old-wrapper'}).text
            # не хватило времени что бы разобраться с розничными ценами
            results.append(
                (name, cleared_string(sale_price), cleared_string(original_price), url)
            )
    deffered.log(logging.warning)
    return results


MODE_TO_FUNCTION = {
    'coffee': coffee,
}


def main():
    configure_logging()
    logging.info(STARTER_PARSER)
    arg_parser = configure_argument_parser(MODE_TO_FUNCTION.keys())
    args = arg_parser.parse_args()
    logging.info(ARGUMENTS_CLI.format(args=args))
    try:
        session = CachedSession()
        if args.clear_cache:
            session.cache.clear()
        parser_mode = args.mode
        results = MODE_TO_FUNCTION[parser_mode](session)
        if results is not None:
            control_output(results, args)
    except Exception as error:
        logging.exception(
            PARSER_ERROR.format(error=error)
        )
    logging.info(ENDING_PARSER)


if __name__ == '__main__':
    main()