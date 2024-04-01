class ParserFindTagException(Exception):
    """Вызывается, когда парсер не может найти тег."""
    pass


class ParserNotFoundPrice(Exception):
    """Вызывается когда у товара отсутствует цена."""
    pass
