import logging


def run_with_log(func):
    logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
    try:
        func()
    except Exception as e:
        logging.error("Exception occurred", exc_info=True)


def call_exception():
    raise UnicodeError


run_with_log(call_exception)
