def update_backstage_passes_quality(item):
    item.quality = item.quality + 1
    if item.sell_in < 6:
        item.quality = item.quality + 1
        item.quality = item.quality + 1
    else:
        item.quality = item.quality + 1

    if item.sell_in < 0:
        item.quality = 0

def update_brie_quality(item):
    item.quality = item.quality + 1

    if item.sell_in < 0:
        item.quality = item.quality + 1

def update_conjured_quality(item):
    item.quality = item.quality - 2

def update_normal_quality(item):
    item.quality = item.quality - 1

    if item.sell_in < 0:
        item.quality = item.quality - 1