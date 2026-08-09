import pytest

from VolatilitySurface.NewtonRaphson.NewtonRaphson import (
    normal_pdf,
    vega,
    price_error,
    step,
    NewtonRaphson
)

def test_normal_pdf():
    assert normal_pdf(0) == pytest.approx(0.39894228, abs=1e-6)
    assert normal_pdf(1) == pytest.approx(0.24197072, abs=1e-6)


def test_vega():
    result = vega(100, 0.35, 1)

    assert result == pytest.approx(37.57, abs=0.1)


def test_price_error():
    assert price_error(12, 10) == 2
    assert price_error(8, 10) == -2
    assert price_error(10, 10) == 0


def test_step():
    result = step(0.20, 1.0, 50.0)

    assert result == pytest.approx(0.18)


def test_newton_raphson_atm():
    result = NewtonRaphson(
        S=100,
        K=100,
        T=1,
        r=0.05,
        Cm=10.4506
    )

    assert result == pytest.approx(0.20, abs=1e-4)


def test_newton_raphson_high_volatility():
    result = NewtonRaphson(
        S=100,
        K=100,
        T=1,
        r=0.05,
        Cm=18.0229
    )

    assert result == pytest.approx(0.40, abs=1e-4)


def test_newton_raphson_itm():
    result = NewtonRaphson(
        S=120,
        K=100,
        T=1,
        r=0.05,
        Cm=26.1690
    )

    assert result == pytest.approx(0.20, abs=1e-4)

def test_newton_raphson_low_vol():
    result = NewtonRaphson(
        S=100,
        K=100,
        T=1,
        r=0.05,
        Cm=6.80496
    )

    assert result == pytest.approx(0.10, abs=1e-4)

    assert result == pytest.approx(0.10, abs=1e-4)

def test_newton_raphson_starting_guess_not_result():
    result = NewtonRaphson(
        S=100,
        K=100,
        T=1,
        r=0.05,
        Cm=14.2313
    )

    assert result == pytest.approx(0.30, abs=1e-4)
    assert result != pytest.approx(0.20)


def test_newton_raphson_high_vol():
    result = NewtonRaphson(
        S=100,
        K=100,
        T=1,
        r=0.05,
        Cm=18.0229
    )

    assert result == pytest.approx(0.40, abs=1e-4)
