import logging

logging.basicConfig(filename='app.log', format='%(levelname)s - %(threadName)s - %(asctime)s - [%(pathname)s.%(module)s:%(lineno)d]: %(message)s', level=logging.DEBUG)

n = 100
logging.error('n = %d' % n)
logging.warning('n = %d' % n)
logging.info('n = %d' % n)
logging.debug('n = %d' % n)
