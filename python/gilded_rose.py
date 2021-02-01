# -*- coding: utf-8 -*-
from update_quality import increase_quality, decrease_quality


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality_before_sellin(self):
        # Update Quality (called whether in date or not)
        for item in self.items:
            if 0 < item.quality < 50:
                if item.name == "Aged Brie":
                    self.update_brie_quality(item)
                elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                    self.update_backstage_passes_quality(item)
                elif item.name == "Sulfuras, Hand of Ragnaros":
                    pass
                else:
                    decrease_quality(item)

            self.update_sellin(item)
            self.update_quality_after_sellin(item)

    def update_backstage_passes_quality(self, item):
        increase_quality(item)
        if item.sell_in < 6:
            increase_quality(item)
            increase_quality(item)
        else:
            increase_quality(item)

    def update_brie_quality(self, item):
        increase_quality(item)

    def update_quality_after_sellin(self, item):
        if item.sell_in < 0:
            if item.name != "Aged Brie":
                if item.name != "Backstage passes to a TAFKAL80ETC concert":
                    if item.quality > 0:
                        if item.name != "Sulfuras, Hand of Ragnaros":
                            # Items not AB, BP, and Sulf: if quality > 0, quality decreases by an extra 1 each
                            # day after sellin date ( in addition to -1 on line 16)
                            decrease_quality(item)
                else:
                    # For BP, item quality is zero after sellin date
                    item.quality = 0
            else:
                if item.quality < 50:
                    # For AB when quality is less than 50, quality increases by an extra 1 each day after sellin date
                    increase_quality(item)

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
