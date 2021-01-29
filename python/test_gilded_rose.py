# -*- coding: utf-8 -*-
import pytest
from gilded_rose import Item, GildedRose

@pytest.mark.parametrize("name, sell_in, quality", [
    ("+5 Dexterity Vest", 10, 20)
])


def test_foo(name, sell_in, quality):
    items = [Item(name, sell_in, quality)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert "+5 Dexterity Vest" == items[0].name

def test_quality_degrades_twice_as_fast_passed_sell_by_date():
    pass



