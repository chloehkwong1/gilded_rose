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

@pytest.mark.parametrize("name, sell_in, quality, expected_value",
 [
    ("testitem1", -1, 20, 18),
    ("testitem2", -1, 15, 13)
])

def test_quality_degrades_twice_as_fast_one_day_after_sellin_date(name, sell_in, quality, expected_value):
    items = [Item(name, sell_in, quality)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == expected_value

@pytest.mark.parametrize("name, sell_in, quality, expected_value",
 [
    ("testitem1", -2, 20, 16),
    ("testitem2", -2, 15, 11)
])


def test_quality_degrades_twice_as_fast_two_days_after_sellin_date(name, sell_in, quality, expected_value):
    items = [Item(name, sell_in, quality)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    gilded_rose.update_quality()
    assert items[0].quality == expected_value




