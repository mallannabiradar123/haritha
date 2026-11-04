import logging
def test_logging():
    logging.basicConfig(level=logging.INFO)
    logging.info("Test automation started")
    logging.basicConfig(level=logging.DEBUG)
    logging.debug("Test New changes")
    assert True
