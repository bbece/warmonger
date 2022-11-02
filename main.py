class Faction():
    first_enemy = None
    second_enemy = None
    number_of_units = None
    attack_point = None
    health_point = None
    total_health = None
    unit_regeneration_point = 0
    is_alive = None

    def __init__(self, name, number_of_units, attack_point, health_point, unit_regeneration_point):
        self.name = name
        self.number_of_units = number_of_units
        self.attack_point = attack_point
        self.health_point = health_point
        self.total_health = number_of_units * health_point

        self.is_alive = True
        self.unit_regeneration_point = unit_regeneration_point

    def assgnEnemies(self, first_enemy, second_enemy):  # main de manuel düşman atayacaksın
        self.first_enemy = first_enemy
        self.second_enemy = second_enemy

    def performAttack(self):
        pass
    def receiveAttack(self,attacking_faction):
        pass

    def purchaseWeapon(self, purchased_weapons_point):
        pass

    def purchaseArmors(self, purchased_armors_point):
        pass

    def endTurn(self):
        if self.number_of_units <= 0:
            self.is_alive=False



    def print(self):
        print(" Faction Name:", self.name, sep="       ")
        if self.is_alive:
            print(" Status:", "Alive", sep="       ")
        else:
            print(" Status:", "Defeated", sep="       ")
        print(" Number of Units:", self.number_of_units, sep="       ")
        print(" Attack Point:", self.attack_point, sep="      ")
        print(" Health Point:", self.health_point, sep="      ")
        print(" Unit Regen Number:", self.unit_regeneration_point, sep="       ")
        print(" Total Faction Health:", self.total_health, sep="      ")


class Orcs(Faction):

    def performAttack(self):
        if not self.is_alive:
            return

        if not self.first_enemy.is_alive and self.second_enemy.is_alive:
            attack_point1 = self.number_of_units * self.attack_point
            self.second_enemy.receiveAttack(self, attack_point1)

        elif not self.second_enemy.is_alive and self.first_enemy.is_alive:
            attack_point1 = self.number_of_units * self.attack_point
            self.first_enemy.receiveAttack(self, attack_point1)



        else:
            if self.first_enemy.name == "Elves":
                attack_point1 = ((self.number_of_units) * 7 / 10) * self.attack_point
                attack_point2 = ((self.number_of_units) * 3 / 10) * self.attack_point
                self.first_enemy.receiveAttack( self,attack_point1)
                self.second_enemy.receiveAttack(self,attack_point2)

            else:
                attack_point2 = ((self.number_of_units) * 7 / 10) * self.attack_point
                attack_point1 = ((self.number_of_units) * 3 / 10) * self.attack_point
                self.first_enemy.receiveAttack(self,attack_point1)
                self.second_enemy.receiveAttack(self,attack_point2)

    def receiveAttack(self,attacking_faction, receive_attack_point):

        if attacking_faction.name == "Elves":
            receive_attack = (receive_attack_point * 75) / 100

        else:
            receive_attack = (receive_attack_point * 80) / 100
        receive_attack_point -= receive_attack
        self.number_of_units -= receive_attack_point / self.health_point
        if self.number_of_units<=0:
            self.number_of_units=0

    def purchaseWeapon(self, purchased_weapon_point):
        self.attack_point += 2 * purchased_weapon_point
        return 20 * purchased_weapon_point

    def purchaseArmors(self, purchased_armors_point):
        self.health_point += 3 * purchased_armors_point
        return purchased_armors_point

    def print(self):
        super().print()
        print("Stop running, you’ll only die tired!")


class Dwarves(Faction):
    def performAttack(self):
        if not self.is_alive:
            return
        if not self.first_enemy.is_alive and self.second_enemy.is_alive:
            attack_point1 = self.number_of_units * self.attack_point
            self.second_enemy.receiveAttack(self,attack_point1)

        elif not self.second_enemy.is_alive and self.first_enemy.is_alive:
            attack_point1 = self.number_of_units * self.attack_point
            self.first_enemy.receiveAttack(self,attack_point1)

        elif self.first_enemy.is_alive and self.second_enemy.is_alive:
            attack_point1 = self.attack_point / 2
            self.first_enemy.receiveAttack(self,attack_point1)
            self.second_enemy.receiveAttack(self,attack_point1)

    def receiveAttack(self,attacking_faction ,receive_attack_point):
        self.number_of_units -= receive_attack_point / self.health_point
        if self.number_of_units<=0:
            self.number_of_units=0

    def purchaseWeapon(self, purchased_weapon_point):
        self.attack_point += purchased_weapon_point
        return 10 * purchased_weapon_point

    def purchaseArmors(self, purchased_armors_point):
        self.health_point += 2 * purchased_armors_point
        return 3 * purchased_armors_point

    def print(self):
        super().print()
        print("Taste the power of our axes")


class Elves(Faction):
    def performAttack(self):
        if not self.is_alive:
            return
        if self.first_enemy.is_alive and not self.second_enemy.is_alive:
            attack_point1 = self.number_of_units * self.attack_point
            if self.first_enemy.name=="Dwarves":
                attack_point1=self.attack_point*1.5*self.number_of_units
            self.first_enemy.receiveAttack(self,attack_point1)

        elif self.second_enemy.is_alive and not self.first_enemy.is_alive:
            attack_point1 = self.number_of_units * self.attack_point
            if self.second_enemy.name=="Dwarves":
                attack_point1=self.attack_point*1.5*self.number_of_units
            self.second_enemy.receiveAttack(self,attack_point1)

        elif self.first_enemy.is_alive and self.second_enemy.is_alive:
            attack_pointOrcs = self.attack_point * (self.number_of_units * 6 / 10)
            attack_pointDwarves = self.attack_point*1.5 * (self.number_of_units * 4 / 10)

            if self.first_enemy.name == "Orcs" and self.second_enemy.name == "Dwarves":  # else i firstün dwarves secondın orc olduğu mu

                self.first_enemy.receiveAttack(self,attack_pointOrcs)
                self.second_enemy.receiveAttack(self,attack_pointDwarves)

            else:
                self.first_enemy.receiveAttack(self,attack_pointDwarves)
                self.second_enemy.receiveAttack(self,attack_pointOrcs)

    def receiveAttack(self, attacking_faction,attack_point):
        if attacking_faction.name == "Orcs":
            attack_point += attack_point * 125 / 100
        elif attacking_faction.name == "Dwarves":
            attack_point -= attack_point * 75 / 100
        self.number_of_units -= attack_point / self.health_point
        if self.number_of_units<=0:
            self.number_of_units=0

    def purchaseWeapon(self, purchased_weapon_point):
        self.attack_point += 2 * purchased_weapon_point
        return 15 * purchased_weapon_point  # altın döndürüyor(murchant için)

    def purchaseArmors(self, purchased_armors_point):
        self.attack_point += 4 * purchased_armors_point
        return 5 * purchased_armors_point

    def print(self):
        super().print()
        print("You cannot reach our elegance.")


class Merchant:
    starting_weapon_point, starting_armor_point = None, None
    revenue = None
    weapon_point, armor_point = None, None

    def __init__(self, starting_weapon_point, starting_armor_point, weapon_point, armor_point):
        self.armor_point = armor_point
        self.weapon_point = weapon_point
        self.starting_armor_point = starting_armor_point
        self.starting_weapon_point = starting_weapon_point
        self.revenue = 0

    def sellWeapons(self, faction, received_weapon_point):
        if not faction.is_alive:
            print("The faction you want to sell weapons is dead!")
            return False
        else:
            if self.weapon_point < received_weapon_point:
                print("You try to sell more weapons than you have in possession.")
                return False

            else:
                self.weapon_point -= received_weapon_point
                self.revenue += faction.purchaseWeapon(received_weapon_point)
                print("Weapons sold!”")
                return True

    def sellArmors(self, faction, received_armors_point):
        if not faction.is_alive:
            print("The faction you want to sell armors is dead!")
            return False
        else:
            if self.armor_point < received_armors_point:
                print("You try to sell more armors than you have in possession.")
                return False
            else:
                self.armor_point -= received_armors_point
                self.revenue += faction.purchaseArmors(received_armors_point)
                print("Armors sold!")
                return True

    def endTurn(self):
        self.weapon_point = self.starting_weapon_point
        self.armor_point = self.starting_armor_point


def main():
    print("Oyuna Hoşgeldiniz")
    print("Lütfen Aşağıdan Açıklamalara Göre Oyuna Devam Ediniz.")

    while True:
        orcs = Orcs("Orcs", 12, 1, 30, 1)
        elves = Elves("Elves", 15, 5, 20,  3)
        dwarves = Dwarves("Dwarves", 18, 2, 15, 3)
        merchant = Merchant(10, 10, 10, 10)
        orcs.assgnEnemies(elves,dwarves)
        elves.assgnEnemies(orcs,dwarves)
        dwarves.assgnEnemies(elves,orcs)

        while True:

            print("Faction Bilgilerini yazdırmak için-1")
            print("Savaştaki bütün Factionlara mühimmat satmak için-2")
            print("Günü Bitirmek için-3")
            print("Şu anki oyunu bitirmek için - 4")
            print("Oyundan Tamamen Çıkmak için-5")
            case = int(input("Lütfen Devam Etmek İstediğiniz Durumu seçiniz."))
            if case == 1:
                orcs.print()
                elves.print()
                dwarves.print()

            elif case == 2:
                print("Lütfen hangi Factiona  kaç tane weapon ve armors satmak istediğinizi sırayla giriniz")
                faction_name = str(input())
                received_weapon_point = int(input())
                received_armors_point = int(input())
                faction = None
                if faction_name=="Elves":
                    faction = elves
                elif faction_name=="Orcs":
                    faction=orcs
                elif faction_name=="Dwarves":
                    faction=dwarves
                else:
                    print("Olmayan faction belirttiniz, lütfen tekrar giriniz")
                    continue
                merchant.sellWeapons(faction, received_weapon_point)
                merchant.sellArmors(faction, received_armors_point)
            elif case == 3:
                merchant.endTurn()
                orcs.performAttack()
                elves.performAttack()
                dwarves.performAttack()
                orcs.endTurn()
                elves.endTurn()
                dwarves.endTurn()
                continue
            elif case == 4:
                break
            elif case == 5:
                return



main()
