import pytest

from VolatilitySurface.BlackScholes_ import d1_, d2_, N, BlackScholes

def test_d1():
    result = d1_(100, 100, 1, 0.05, 0.20)

    assert result == pytest.approx(0.35, abs=1e-4)


def test_d2():
    d1 = d1_(100, 100, 1, 0.05, 0.20)

    result = d2_(d1, 0.20, 1)

    assert result == pytest.approx(0.15, abs=1e-4)


def test_normal_cdf():
    assert N(0) == pytest.approx(0.5)
    assert N(1) == pytest.approx(0.8413447, abs=1e-6)
    assert N(-1) == pytest.approx(0.1586553, abs=1e-6)


def test_black_scholes_atm():
    result = BlackScholes(100, 100, 1, 0.05, 0.20)

    assert result == pytest.approx(10.4506, abs=1e-4)


def test_black_scholes_itm():
    result = BlackScholes(120, 100, 1, 0.05, 0.20)

    assert result == pytest.approx(26.1690, abs=1e-4)


def test_black_scholes_otm():
    result = BlackScholes(100, 120, 1, 0.05, 0.20)

    assert result == pytest.approx(3.2475, abs=1e-4)


def test_higher_volatility_increases_call_price():
    low_vol = BlackScholes(100, 100, 1, 0.05, 0.20)
    high_vol = BlackScholes(100, 100, 1, 0.05, 0.40)

    assert high_vol > low_vol
