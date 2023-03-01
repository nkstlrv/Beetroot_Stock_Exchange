from simulator_main import Exchange
import pytest


@pytest.fixture
def exchange_class():
    return Exchange(r"demo_test_data.json")


def test_get_price(exchange_class):
    assert isinstance(exchange_class.get_price('aapl'), float)
    assert isinstance(exchange_class.get_price('AAPL'), float)
    assert isinstance(exchange_class.get_price('msft'), float)
    assert isinstance(exchange_class.get_price('MSFT'), float)
    assert isinstance(exchange_class.get_price('googl'), float)
    assert isinstance(exchange_class.get_price('GOOGL'), float)
    assert isinstance(exchange_class.get_price('tsla'), float)
    assert isinstance(exchange_class.get_price('TSLA'), float)


def test_get_price_non_existing_ticker(exchange_class):
    with pytest.raises(KeyError) as ke:
        exchange_class.get_price('non_existing_ticker')
    assert "'You are trying to find a non-existing ticker'" == str(ke.value)

    with pytest.raises(KeyError) as ke:
        exchange_class.get_price('another_non_existing_ticker')
    assert "'You are trying to find a non-existing ticker'" == str(ke.value)

    with pytest.raises(KeyError) as ke:
        exchange_class.get_price('and_one_more_non_existing_ticker')
    assert "'You are trying to find a non-existing ticker'" == str(ke.value)

    with pytest.raises(KeyError) as ke:
        exchange_class.get_price('')
    assert "'You are trying to find a non-existing ticker'" == str(ke.value)
