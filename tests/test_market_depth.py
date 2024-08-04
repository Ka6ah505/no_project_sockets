import pytest
from no_project_sockets.socket_server.market_depth import MarketDepth

@pytest.fixture
def raw_data_market():
    return {10:32,9:54,8:-65,7:-23}

def test_get_max_volumes(raw_data_market):
    # ДЕЙСТВИЕ
    market_depth = MarketDepth(raw_data_market)
    # УТВЕРЖДЕНИЕ
    assert market_depth.max_volume_ask() == {8:65}
    assert market_depth.max_volume_bid() == {9:54}

def test_get_ask(raw_data_market):
    market_depth = MarketDepth(raw_data_market)
    assert market_depth.ask == {8:65,7:23}

def test_get_bid(raw_data_market):
    market_depth = MarketDepth(raw_data_market)
    assert market_depth.bid == {9:54,10:32}
