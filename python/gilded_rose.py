# -*- coding: utf-8 -*-
from update_quality_items import update_backstage_passes_quality, update_brie_quality, update_normal_quality


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def main(self):
        for item in self.items:
            if 0 < item.quality < 50:
                self.update_quality(item)
                self.update_sellin(item)


    def update_quality(self, item):
            if item.name == "Aged Brie":
                update_brie_quality(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                update_backstage_passes_quality(item)
            elif item.name == "Sulfuras, Hand of Ragnaros":
                pass
            else:
                update_normal_quality(item)

    def update_sellin(self, item):
        if item.name != "Sulfuras, Hand of Ragnaros":
            # For all items (except Sulfuras), SellIn decreases by 1 each day
            item.sell_in = item.sell_in - 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
