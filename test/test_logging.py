import logging
def test_logging():
    logging.basicConfig(level=logging.INFO)
    logging.info("Test automation started")
    assert True
    