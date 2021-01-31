# -*- coding: utf-8 -*-
import pytest
from gilded_rose import Item, GildedRose


@pytest.mark.parametrize("name, sell_in, quality, expected_value",
                         [
                             ("testitem1", 10, 10, 9),
                             ("testitem2", 5, 15, 14)
                         ])
def test_quality_normal_items_decrease_daily(name, sell_in, quality, expected_value):
    items = [Item(name, sell_in, quality)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == expected_value


@pytest.mark.parametrize("name, sell_in, quality, expected_value",
                         [
                             ("testitem1", 10, 10, 9),
                             ("testitem2", 5, 15, 4)
                         ])
def test_sellin_normal_items_decreases_daily(name, sell_in, quality, expected_value):
    items = [Item(name, sell_in, quality)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == expected_value


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


def test_quality_is_never_negative():
    items = [Item("testitem1", -1, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality >= 0


def test_brie_and_BP_passes_quality_increases_daily_before_sellin():
    items = [Item("Aged Brie", 10, 20)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 21


def test_brie_quality_increases_double_after_sellin():
    items = [Item("Aged Brie", -2, 15)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 17


def test_quality_never_more_than_50():
    items = [Item("Aged Brie", 20, 50)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 50


# Should these next two sulfuras tests be in one test?
def test_sulfuras_quality_constant():
    items = [Item("Sulfuras, Hand of Ragnaros", 20, 20)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 20


def test_sulfuras_sellin_constant():
    items = [Item("Sulfuras, Hand of Ragnaros", 20, 20)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == 20

# Is it okay to combine all the backstage pass qualities into one test?
@pytest.mark.parametrize("name, sell_in, quality, expected_value",
                         [
                             ("Backstage passes to a TAFKAL80ETC concert", 10, 10, 12),
                             ("Backstage passes to a TAFKAL80ETC concert", 5, 10, 13),
                             ("Backstage passes to a TAFKAL80ETC concert", -1, 10, 0),
                         ])
def test_backstage_passes_quality(name, sell_in, quality, expected_value):
    items = [Item(name, sell_in, quality)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == expected_value
