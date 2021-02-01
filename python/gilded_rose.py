# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality_before_sellin(self):
        # Update Quality (called whether in date or not)
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        # For normal items, system lowers the quality by 1 after each day
                        # Sulfuras doesn't decrease in quality
                        self.decrease_quality(item)
            else:
                if item.quality < 50:
                    # For Aged Brie & Backstage passes the quality increases by 1 each day
                    self.increase_quality(item)
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                # For Backstage passes, if SellIn less than 11 and Quality less than 50, quality
                                # increases by 1
                                self.increase_quality(item)
                        if item.sell_in < 6:
                            # Not redundant - used in BP passes case to add quality for 5 days or less case
                            if item.quality < 50:
                                self.increase_quality(item)

            # Update SellIn
            self.update_sellin(item)

            # Update Quality if out of date
            self.update_quality_after_sellin(item)

    def increase_quality(self, item):
        item.quality = item.quality + 1

    def decrease_quality(self, item):
        item.quality = item.quality - 1

    def update_quality_after_sellin(self, item):
        if item.sell_in < 0:
            if item.name != "Aged Brie":
                if item.name != "Backstage passes to a TAFKAL80ETC concert":
                    if item.quality > 0:
                        if item.name != "Sulfuras, Hand of Ragnaros":
                            # Items not AB, BP, and Sulf: if quality > 0, quality decreases by an extra 1 each
                            # day after sellin date ( in addition to -1 on line 16)
                            self.decrease_quality(item)
                else:
                    # For BP, item quality is zero after sellin date
                    item.quality = 0
            else:
                if item.quality < 50:
                    # For AB when quality is less than 50, quality increases by an extra 1 each day after sellin date
                    self.increase_quality(item)

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
