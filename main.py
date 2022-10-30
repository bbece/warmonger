class Faction():
    first_enemy=None
    second_enemy=None
    number_of_units=None
    attack_point=None
    health_point=None
    total_health=None
    unit_regeneration_point=None
    is_alive=None




    def __init__(self, name, number_of_units, attack_point, health_point, is_alive):
        self.name = name
        self.number_of_units = number_of_units
        self.attack_point = attack_point
        self.health_point = health_point
        self.total_health = number_of_units * health_point
        if not is_alive:
            self.is_alive = True




    def assgnEnemies(self,first_enemy,second_enemy):#main de manule düşman atayacaksın
        self.first_enemy=first_enemy
        self.second_enemy=second_enemy




    def performAttack(self):
        pass

    def purchaseWeapon(self,purchased_weapons_point):
        pass

    def purchaseArmors(self,purchased_armors_point):
        pass

    def endTurn(self):
        if self.number_of_units < 0:
            return 0
        elif self.number_of_units == 0:
            self.is_alive = False


class Orcs(Faction):



    def performAttack(self):



        if not self.first_enemy.is_alive and self.second_enemy.is_alive:
            attack_point1 = self.number_of_units * self.attack_point
            self.second_enemy.receiveAttack(self, attack_point1)

        elif not self.second_enemy.is_alive and self.first_enemy.is_alive:
            attack_point1 = self.number_of_units * self.attack_point
            self.first_enemy.receiveAttack(self,attack_point1)



        else:
           if self.first_enemy.name=="Elves" :
               attack_point1=((self.number_of_units)*7/10)*self.attack_point
               attack_point2=((self.number_of_units)*3/10)*self.attack_point
               self.first_enemy.receiveAttack(self,attack_point1)
               self.second_enemy.receiveAttack(self,attack_point2)

           else:
               attack_point2 = ((self.number_of_units) * 7 / 10) * self.attack_point
               attack_point1 = ((self.number_of_units) * 3 / 10) * self.attack_point
               self.first_enemy.receiveAttack(self, attack_point1)
               self.second_enemy.receiveAttack(self, attack_point2)




    def receiveAttack(self,receive_attack_point):

        if self.first_enemy.name=="Elves" or self.second_enemy.name=="Elves":
             receive_attack = (receive_attack_point * 75) / 100

        else:
            receive_attack= (receive_attack_point * 80) / 100
        receive_attack_point -= receive_attack
        self.number_of_units -= receive_attack_point / self.health_point






    def purchaseWeapon(self,purchased_weapon_point):
        self.attack_point += 2*purchased_weapon_point
        return 20*purchased_weapon_point

            



    def purchaseArmors(self,purchased_armors_point):
        self.health_point += 3*purchased_armors_point
        return purchased_armors_point




class Dwarves(Faction):
    def performAttack(self):
        if not self.first_enemy.is_alive and self.second_enemy.is_alive:
            attack_point1 = self.number_of_units * self.attack_point
            self.second_enemy.receiveAttack(self, attack_point1)

        elif not self.second_enemy.is_alive and self.first_enemy.is_alive:
            attack_point1 = self.number_of_units * self.attack_point
            self.first_enemy.receiveAttack(self, attack_point1)

        elif self.first_enemy.is_alive and self.second_enemy.is_alive:
            attack_point1=self.attack_point/2
            self.first_enemy.receiveAttack(attack_point1)
            self.second_enemy.receiveAttack(attack_point1)



    def receiveAttack(self,receive_attack_point):
        self.number_of_units -= receive_attack_point / self.health_point

    def purchaseWeapon(self,purchased_weapon_point):
        self.attack_point += purchased_weapon_point
        return 10*purchased_weapon_point


    def purchaseArmors(self,purchased_armors_point):
        self.health_point += 2*purchased_armors_point
        return 3*purchased_armors_point



class Elves(Faction):
    def performAttack(self):
        if self.first_enemy.name=="Dwarves" or self.second_enemy.name=="Dwarves":
            self.attack_point += self.attack_point*15/10

        if self.first_enemy.is_alive and not self.second_enemy.is_alive:
            attack_point1=self.number_of_units*self.attack_point
            self.first_enemy.receiveAttack(attack_point1)

        elif self.second_enemy.is_alive and not self.first_enemy.is_alive:
            attack_point1 = self.number_of_units * self.attack_point
            self.second_enemy.receiveAttack(attack_point1)

        elif self.first_enemy.is_alive and self.second_enemy.is_alive:
            attack_pointOrcs = self.attack_point * (self.number_of_units * 6 / 10)
            attack_pointDwarves = self.attack_point * (self.number_of_units * 4 / 10)

            if self.first_enemy.name=="Orcs" and self.second_enemy.name=="Dwarves":#else i firstün dwarves secondın orc olduğu mu

                self.first_enemy.receiveAttack(attack_pointOrcs)
                self.second_enemy.receiveAttack(attack_pointDwarves)

            else:
                self.first_enemy.receiveAttack(attack_pointDwarves)
                self.second_enemy.receiveAttack(attack_pointOrcs)





    def receiveAttack(self,attack_point):
        if self.first_enemy.name=="Orcs" or self.second_enemy.name=="Orcs":
            attack_point += attack_point*125/100
        elif self.first_enemy.name=="Dwarves" or self.second_enemy.name=="Dwarves":
            attack_point -= attack_point*75/100
        self.number_of_units -= attack_point / self.health_point

    def purchaseWeapon(self,purchased_weapon_point):
        self.attack_point+=2*purchased_weapon_point
        return 15*purchased_weapon_point #altın döndürüyor(murchant için)




    def purchaseArmors(self,purchased_armors_point):
        self.attack_point += 4*purchased_armors_point
        return 5*purchased_armors_point




class Merchant:

    first_faction,second_faction=None
    starting_weapon_point,starting_armor_point=None
    revenue=None
    weapon_point,armor_point=None


    def __init__(self,starting_weapon_point,starting_armor_point,weapon_point,armor_point):
        self.armor_point=armor_point
        self.weapon_point=weapon_point
        self.starting_armor_point=starting_armor_point
        self.starting_weapon_point=starting_weapon_point
        self.revenue=0




    def sellWeapons(self,faction,received_weapon_point):
        if not faction.is_alive:
            print("The faction you want to sell weapons is dead!")
            return False
        else:
            if self.weapon_point<received_weapon_point:
                print("You try to sell more weapons than you have in possession.")
                return False

            else:
                self.weapon_point -= received_weapon_point
                print("Weapons sold!”")
                return True

    def sellArmors(self,faction,received_armors_point):
        if not faction.is_alive:
            print("The faction you want to sell armors is dead!")
            return False
        else:
            if self.armor_point<received_armors_point:
                print("You try to sell more armors than you have in possession.")
            else:
                self.armor_point -= received_armors_point
                print("Armors sold!")

    def endTurn(self):
        pass


def main():
    