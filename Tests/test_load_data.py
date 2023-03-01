from simulator_main import Exchange
import pytest


@pytest.fixture
def exchange_class():
    return Exchange(r"demo_test_data.json")


def test_load_data(exchange_class):
    assert exchange_class.portfolio == {"TEST": 1, "MSFT": 2}
    assert exchange_class.data == {"portfolio": {"TEST": 1, "MSFT": 2}, "balance": 1000}
    assert exchange_class.data['balance'] == 1000


def test_file_not_found():
    with pytest.raises(FileNotFoundError) as fnf:
        error_class = Exchange("wrong_dir/wrong_file.json")
    assert "[Errno 2] No such file or directory: 'wrong_dir/wrong_file.json'" == str(fnf.value)
