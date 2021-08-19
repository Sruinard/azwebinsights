from marketplace.domain import model

def test_charger_in_region():
    charger = model.ElectricCharger(sku='random1', location='west-europe')
    assert charger.location == 'west-europe'