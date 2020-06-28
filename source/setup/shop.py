from .text import centerprint, line, enter_select
from ..item.create_item import *
from ..skill import cooldown, CooldownException


class aksesBlackMarker:
    def __init__(self):
        self.countdown = 120
        self.cooldown = cooldown(self.countdown)

    def BlackMarket(self, hero):
        try:
            with self.cooldown:
                blackMarket(hero)
        except CooldownException as e:
            print('=' * 30)
            centerprint("Black Market Tutup, Tunggu")
            print(e)
            enter_select()
            shop(hero)


Shop = aksesBlackMarker()


def shop(hero):
    line()
    centerprint("== Toko ==")
    line()
    print("[1]Senjata\n"
          "[2]Armor\n"
          "[3]Black Market\n"
          "[4]Keluar")
    index = input('>>> ')
    if index == '1':
        shop_weapons(hero)
    elif index == '2':
        shop_armor(hero)
    elif index == '3':
        Shop.BlackMarket(hero)
    elif index == '4':
        from source.stargame import gameLoop
        gameLoop()
    else:
        shop(hero)


def shop_weapons(player):
    if player.type_hero == typeHero.Mage:
        line()
        centerprint("perlengkapan Mage")
        line()
        print(
            "[1]{}    : {} {}\n"
            "[2]{}  : {} {}\n"
            "[3]{}      : {} {}\n"
            "[4]{}      : {} {}\n"
            "[5]{} : {} {}".format(
                weapons_mage(1).qualty, weapons_mage(1).shape, weapons_mage(1).nama,
                weapons_mage(2).qualty, weapons_mage(2).shape, weapons_mage(2).nama,
                weapons_mage(3).qualty, weapons_mage(3).shape, weapons_mage(3).nama,
                weapons_mage(4).qualty, weapons_mage(4).shape, weapons_mage(4).nama,
                weapons_mage(5).qualty, weapons_mage(5).shape, weapons_mage(5).nama
            )
        )
    elif player.type_hero == typeHero.Warrior:
        line()
        centerprint("perlengkapan warrior")
        line()
        print(
            "[1]{}    : {} {}\n"
            "[2]{}  : {} {}\n"
            "[3]{}      : {} {}\n"
            "[4]{}      : {} {}\n"
            "[5]{} : {} {}".format(
                weapons_warrior(1).qualty, weapons_warrior(1).shape, weapons_warrior(1).nama,
                weapons_warrior(2).qualty, weapons_warrior(2).shape, weapons_warrior(2).nama,
                weapons_warrior(3).qualty, weapons_warrior(3).shape, weapons_warrior(3).nama,
                weapons_warrior(4).qualty, weapons_warrior(4).shape, weapons_warrior(4).nama,
                weapons_warrior(5).qualty, weapons_warrior(5).shape, weapons_warrior(5).nama
            )
        )
    elif player.type_hero == typeHero.Archer:
        line()
        centerprint("perlengkapan Archer")
        line()
        print(
            "[1]{}    : {} {}\n"
            "[2]{}  : {} {}\n"
            "[3]{}      : {} {}\n"
            "[4]{}      : {} {}\n"
            "[5]{} : {} {}".format(
                weapons_archer(1).qualty, weapons_archer(1).shape, weapons_archer(1).nama,
                weapons_archer(2).qualty, weapons_archer(2).shape, weapons_archer(2).nama,
                weapons_archer(3).qualty, weapons_archer(3).shape, weapons_archer(3).nama,
                weapons_archer(4).qualty, weapons_archer(4).shape, weapons_archer(4).nama,
                weapons_archer(5).qualty, weapons_archer(5).shape, weapons_archer(5).nama
            )
        )
    print('[6]Keluar')
    index = input('>>> ')
    if player.type_hero == typeHero.Mage and '5' >= index >= '0':
        systemShop(weapons_mage(int(index)), player)
    elif player.type_hero == typeHero.Warrior and '5' >= index >= '0':
        systemShop(weapons_warrior(int(index)), player)
    elif player.type_hero == typeHero.Archer and '5' >= index >= '0':
        systemShop(weapons_archer(int(index)), player)
    else:
        shop(player)


def shop_armor(player):
    line()
    centerprint("Armor")
    line()
    print(
        "[1]{}    : {} {}\n"
        "[2]{}  : {} {}\n"
        "[3]{}      : {} {}\n"
        "[4]{}      : {} {}\n"
        "[5]{} : {} {}".format(
            createArmor(1).qualty, createArmor(1).type, createArmor(1).nama,
            createArmor(2).qualty, createArmor(2).type, createArmor(2).nama,
            createArmor(3).qualty, createArmor(3).type, createArmor(3).nama,
            createArmor(4).qualty, createArmor(4).type, createArmor(4).nama,
            createArmor(5).qualty, createArmor(5).type, createArmor(5).nama
        )
    )
    print('[6]keluar')
    index = input(">>> ")
    if '5' >= index >= '0':
        systemShop(createArmor(int(index)), player)
    else:
        shop(player)


def systemShop(item, player):
    line()
    if item.type == 'Armor':
        print(item.show_armor())
    elif item.type == 'Weapons':
        print(item.show_weapons())
    line()
    print('Coin player :', player.coin)
    index = input('Harga {} {} : {} \nBeli [y/n]>>> '.format(item.type, item.nama, item.coin)).lower()
    if index == 'y':
        if player.coin >= item.coin:
            player.coin -= item.coin
            line()
            player.add_inv(item)
            centerprint("{} {} telah terbeli".format(item.type, item.nama))
            line()
            print('[1]Pakai \n[2]Shop')
            choose = input('>>> ')
            if item.type == 'Armor' and choose == '1':
                try:
                    player.system_Armor()
                    player.use_item(item)
                except IndexError:
                    player.use_item(item)
                line()
                print("{} {} telah terpakai".format(item.type, item.nama))
                enter_select()
                shop(player)
            elif item.type == 'Weapons' and choose == '1':
                try:
                    player.system_Weapone()
                    player.use_item(item)
                except IndexError:
                    player.use_item(item)
                line()
                centerprint("{} {} telah terpakai".format(item.type, item.nama))
                enter_select()
                shop(player)
            else:
                shop(player)
        else:
            limit_coin = item.coin - player.coin
            line()
            centerprint("Maap :(")
            centerprint(" coin Anda kurang {}".format(limit_coin))
            enter_select()
            shop(player)
    else:
        shop(player)


def blackMarket(player):
    import random
    coin = random.randint(10, 30)
    amount = random.randint(1, 5)

    # Pemilihan item untuk Black market
    itemWeapons = random.choice(
        [
            weapons_warrior(random.randint(3, 6)),
            weapons_mage(random.randint(3, 6)),
            weapons_archer(random.randint(3, 6))
        ]
    )
    itemFoodPotion = random.choice(
        [
            mana, health, seblak, candy
        ]
    )

    # system untuk discount
    disFoodPotion = round(amount * diskon(itemFoodPotion, coin))
    disWeapons = round(1 * diskon(itemWeapons, coin))
    itemFoodPotion.amount = amount

    line()
    centerprint("Black Market")
    line()
    centerprint("== Diskon {}% ==".format(coin))
    print('[1]{}x |{} {} | {} Coin'.format(itemWeapons.amount, itemWeapons.shape, itemWeapons.nama, disWeapons))
    print('[2]{}x | {}| {} Coin '.format(itemFoodPotion.amount, itemFoodPotion.nama, disFoodPotion))
    print('[3]Shop')
    line()
    index = input(">>> ")
    if index == '1':
        systemBC(player=player, items=itemWeapons, coin=disWeapons)
    elif index == '2':
        systemBC(player=player, items=itemFoodPotion, coin=disFoodPotion)
    elif index == '3':
        shop(player)
    else:
        blackMarket(player)


def diskon(items, coin):
    a = items.coin - (items.coin * (coin / 100))
    return a


def systemBC(player, items, coin):
    line()
    print('Coin player :', player.coin)
    index = input('Harga {} Coin| {}x \nBeli [y/n]>>> '.format(coin, items.amount)).lower()
    if index == 'y':
        if player.coin >= coin:
            player.coin -= coin
            player.add_inv(items)
            # print(amount)
            line()
            centerprint('{} Telah Dibeli, cek di "inventory"'.format(items.nama))
            enter_select()
            shop(player)
        else:
            limit_coin = coin - player.coin
            line()
            centerprint("Maap :(")
            centerprint(" coin Anda kurang {}".format(limit_coin))
            enter_select()
            shop(player)
    else:
        shop(player)
