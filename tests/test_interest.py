import pytest
from part1 import calculate_interest

def test_check_string():
    with pytest.raises(ValueError):
        calculate_interest("231213")

def tst_int_float():
    with pytest.raises(ValueError):
        calculate_interest(number)

def test_bool():
    with pytest.raises(ValueError):
        calculate_interest(True)

def test_value_0():
    with pytest.raises(ValueError):
        calculate_interest(-23)
    

def test_deposit_tier_1(monkeypatch):
    inputs = iter([800,0.03,24])
    monkeypatch.setattr('builtins.input',lambda _: next(inputs))
    outputs=[]
    monkeypatch.setattr('builtins.print', lambda x: outputs.append(x))

    calculate_interest(800)
    assert outputs == ["Tier 1: Deposit: 800, Amount in Tier 1: 800, Interest from Tier 1: 24.00"]

def test_deposit_tier_2(monkeypatch):
    inputs = iter([5000,0.035,175])
    monkeypatch.setattr('builtins.input',lambda _: next(inputs))
    outputs=[]
    monkeypatch.setattr('builtins.print', lambda x: outputs.append(x))

    calculate_interest(5000)
    assert outputs == ['Tier 1: Deposit: 5000, Amount in Tier 1: 1000, Interest from Tier 1: ''30.00',"Tier 2: Deposit: 5000, Amount in Tier 2: 4000, Interest from Tier 2: 140.00"]

def test_deposit_tier_3(monkeypatch):
    inputs = iter([50000,0.04])
    monkeypatch.setattr('builtins.input',lambda _: next(inputs))
    outputs=[]
    monkeypatch.setattr('builtins.print', lambda x: outputs.append(x))

    calculate_interest(50000)
    assert outputs == ['Tier 1: Deposit: 50000, Amount in Tier 1: 1000, Interest from Tier 1: ''30.00',"Tier 2: Deposit: 50000, Amount in Tier 2: 10000, Interest from Tier 2: 350.00", 'Tier 3: Deposit: 50000, Amount in Tier 3: 50000, Interest from Tier 3: 1560.00']

def test_deposit_tier_4(monkeypatch):
    inputs = iter([101000,0.045,4545])
    monkeypatch.setattr('builtins.input',lambda _: next(inputs))
    outputs=[]
    monkeypatch.setattr('builtins.print', lambda x: outputs.append(x))

    calculate_interest(101000)
    assert outputs == ['Tier 1: Deposit: 101000, Amount in Tier 1: 1000, Interest from Tier 1: ''30.00',"Tier 2: Deposit: 101000, Amount in Tier 2: 50000, Interest from Tier 2: 350.00", 'Tier 3: Deposit: 101000, Amount in Tier 3: 50000, Interest from Tier 3: 1560.00', ]