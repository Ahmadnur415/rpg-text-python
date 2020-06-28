from .text import line, enter_select, centerprint, typeHero


# TODO: Inventory
def inventory(player):
    global jual
    line()
    centerprint("== Inventory ==")
    line()
    player.print_inventory()
    line()
    print("[c]Camp")
    index = input("pilih item: ")
    try:
        index = int(index) - 1
        items = player.inventory[index]
    except IndexError:
        line()
        centerprint("Tidak Ada item di inventory")
        enter_select()
        from source.stargame import camp
        return camp()
    except ValueError:
        from source.stargame import camp
        return camp()

    # TODO: ===========[Item Type Material]===========
    line()
    if items.type == "Mineral" or items.type == "Item":
        downCoin = items.coin * 10 / 100
        sell = int(items.coin - downCoin)
        print(items.show_item())
        line()
        print("[1]Jual 1 item = {} coin".format(sell))
        print("[2]Buang\n"
              "[3]Inventory")
        index = input("===> ")
        if index == "1":
            line()
            centerprint("Item {} Ada {}x \nMasukan jumlah item".format(items.nama, items.amount))
            try:
                jual = int(input("Yang ingin dijual : "))
            except ValueError:
                line()
                centerprint("Masukan Angka , Bukan Hurup / Symbol")
                inventory(player)

            if items.amount < jual:
                line()
                centerprint("Item hanya ada {} Anda Melebihi batas".format(items.amount))
                inventory(player)
            elif items.amount == jual:
                items.amount -= jual
                coin = sell * jual
                print("=" * 30)
                centerprint("Item terjual {}".format(jual))
                player.gainCoin = int(coin)
                line()
                centerprint("Item {} sudah tidak ada lagi diinventory".format(items.nama))
                player.inventory.remove(items)
                enter_select()
                inventory(player)
            elif items.amount > jual:
                items.amount -= jual
                coin = sell * jual
                print("=" * 30)
                centerprint("Item terjual {}".format(jual))
                player.gainCoin = int(coin)
                centerprint("{} item tersisa {}x".format(items.nama, items.amount))
                enter_select()
                inventory(player)
            else:
                line()
                centerprint("Masukan Angka Bukan Hurup")
                inventory(player)
        elif index == "2":
            line()
            centerprint("Item telah diBuang")
            player.inventory.remove(items)
            enter_select()
            inventory(player)
        else:
            inventory(player)

    # TODO: ===========[Item Type Armor]===========
    elif items.type == 'Armor':
        downCoin = items.coin * 10 / 100
        sell = int(items.coin - downCoin)
        print(items.show_armor())
        line()
        print("[1]Pakai\n"
              "[2]Jual 1 {} = {} coin\n"
              "[3]Buang\n"
              "[4]keluar".format(items.type,sell))
        line()
        armor = input("==> ")
        line()
        if armor == '1':
            try:
                player.system_Armor()
                player.use_item(items)
            except IndexError:
                player.use_item(items)
            centerprint("{} {} telah terpakai, cek di 'Perlengkapan' ".format(items.type, items.nama))
            enter_select()
            inventory(player)
        elif armor == '2':
            if items.equip:
                centerprint("Item Tidak Bisa Dijual, item sedang dipakai coba cek di 'Perlengkapan'")
                enter_select()
                inventory(player)
            else:
                centerprint("apakah anda ingin menjual {} {} sebesar {} Coin".format(items.type, items.nama, sell))
                jual = input("[y/n]>>> ")
                line()
                if jual == 'y' or jual == 'Y':
                    centerprint("{} {} telah diJual".format(items.type, items.nama))
                    player.gainCoin = int(sell)
                    enter_select()
                else:
                    inventory(player)

        elif armor == '3':
            if items.equip:
                centerprint("{} {} Tidak Bisa DiBuang, item sedang dipakai coba cek di 'Perlengkapan'".format(
                    items.type, items.nama))
                enter_select()
                inventory(player)
            else:
                line()
                centerprint("{} {} telah diBuang".format(items.type, items.nama))
                player.inventory.remove(items)
                enter_select()
                inventory(player)
        else:
            inventory(player)

    # TODO: ===========[Item Type Weapons]===========
    elif items.type == 'Weapons':
        downCoin = items.coin * (10 / 100)
        sell = int(items.coin - downCoin)
        print(items.show_weapons())
        line()
        print("[1]Pakai\n"
              "[2]Jual 1 {} = {} coin\n"
              "[3]Buang\n"
              "[4]keluar".format(items.type, sell))
        line()
        wpns = input("==> ")
        line()
        if wpns == "1":
            if items.type_hero == player.type_hero:
                try:
                    player.system_Weapone()
                    player.use_item(items)
                except IndexError:
                    player.use_item(items)
                centerprint("{} {} telah terpakai, cek di 'Perlengkapan'".format(items.shape, items.nama))
                enter_select()
                inventory(player)
            else:
                line()
                centerprint("Weapons ini hanya untuk Hero {}".format(items.type_hero))
                enter_select()
                inventory(player)

        elif wpns == "2":
            if items.equip:
                centerprint("Item Tidak Bisa Dijual, item sedang dipakai coba cek di 'Perlengkapan'")
                enter_select()
                inventory(player)
            else:
                centerprint("apakah anda ingin menjual {} {} sebesar {} Coin".format(items.shape, items.nama, sell))
                jual = input("[y/n]>>> ")
                if jual == 'y' or jual == 'Y':
                    centerprint("{} {} telah diJual".format(items.shape, items.nama))
                    player.inventory.remove(items)
                    player.gainCoin = int(sell)
                    enter_select()
                else:
                    inventory(player)

        elif wpns == "3":
            if items.equip:
                centerprint("{} {} Tidak Bisa DiBuang, item sedang dipakai coba cek di 'Show Armor dan weapons'".format(
                    items.shape, items.nama))
                enter_select()
                inventory(player)
            else:
                line()
                centerprint("{} {} telah diBuang".format(items.shape, items.nama))
                player.inventory.remove(items)
                enter_select()
                inventory(player)
        elif wpns == '4':
            inventory(player)
        else:
            inventory(player)

    # TODO: ===========[Item Type Potion]===========
    elif items.type == "Potion":
        print(items.show_potion())
        line()
        print("[1]Pakai\n"
              "[2]Buang\n"
              "[3]keluar")
        line()
        index = input("==> ")
        line()
        if index == '1':
            if items.use_hero == player.type_hero:
                player.regenMana = items.UP_mana
                items.value -= 1
                # player.mana += items.UP_mana
                player.manaMax += round(10 / 100 * items.UP_mana)
                line()
                print("Mana +{}".format(items.UP_mana))
                if items.amount <= 0:
                    print("potion sudah tidak ada ")
                    player.inventory.remove(items)
                    enter_select()
                    inventory(player)
                enter_select()
                inventory(player)

            elif items.use_hero == 'all':
                player.heal = items.Up_health
                player.healthMax += round(10 / 100 * items.Up_health)
                line()
                print("Health +{}".format(items.Up_health))
                items.amount -= 1
                if items.amount <= 0:
                    print("potion sudah tidak ada ")
                    player.inventory.remove(items)
                    enter_select()
                    inventory(player)
                enter_select()
                inventory(player)

            else:
                line()
                centerprint("potion {} hanya untuk hero type mage".format(items.nama))
                enter_select()
                inventory(player)
        elif index == '2':
            line()
            centerprint("Potion Sudah tidak ada inventory")
            player.inventory.remove(items)
            enter_select()
            inventory(player)
        else:
            inventory(player)

    # TODO: ===========[Item Type Food]===========
    elif items.type == "Food":
        line()
        print(items.show_Food())
        line()
        print("[1]Makan \n[2]Buang \n[3]Keluar")
        line()
        index = input("==> ")
        line()
        if index == '1':
            if player.type_hero == typeHero.Mage:
                print("Hp + {} \nMana + {} \nMagic + {}".format(items.Up_hp, items.Up_mana, items.Up_Atk))
                player.mana += items.Up_mana
                player.manaMax += items.Up_mana
                player.magic += items.Up_Atk
            else:
                print("Hp + {} \npower + {}".format(items.Up_hp, items.Up_Atk))
                player.attpower += items.Up_Atk
            player.health += items.Up_hp
            player.healthMax += items.Up_hp
            items.amount -= 1
            if items.amount <= 0:
                print("food {} sudah tidak ada ".format(items.nama))
                player.inventory.remove(items)
                enter_select()
                inventory(player)
            enter_select()
            inventory(player)
        elif index == '2':
            line()
            centerprint("food {} Sudah tidak ada inventory".format(items.nama))
            player.inventory.remove(items)
            enter_select()
            inventory(player)
        else:
            inventory(player)


def perlengkapan(player):
    line()
    player.print_Weapone_Armor()
    line()
    print("[1]lihat armor\n"
          "[2]lihat weapons\n"
          "[c]Camp")
    line()
    index = input('>>> ')
    if index == '1':
        try:
            items = player.use_armor[0]
            line()
            print(items.show_armor())
            line()
            choose = input('[1]Copot \n[2]Keluar \n>>> ')
            if choose == '1':
                centerprint('{} {} Telah dicopot'.format(items.type, items.nama))
                player.system_Armor()
                perlengkapan(player)
            else:
                perlengkapan(player)
        except IndexError:
            line()
            centerprint('Anda Belum memakai armor')
            enter_select()
            perlengkapan(player)

    elif index == '2':
        try:
            items = player.use_weapons[0]
            line()
            print(items.show_weapons())
            line()
            choose = input('[1]Copot \n[2]Keluar \n>>> ')
            if choose == '1':
                line()
                centerprint('{} {} Telah dicopot'.format(items.shape, items.nama))
                player.system_Weapone()
                perlengkapan(player)
            else:
                perlengkapan(player)
        except IndexError:
            line()
            centerprint('Anda Belum memakai Senjata')
            enter_select()
            perlengkapan(player)
    elif index == 'c':
        from source.stargame import camp
        return camp()
    else:
        perlengkapan(player)
