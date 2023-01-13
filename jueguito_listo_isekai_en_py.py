from random import randint

class Champ:
        def __init__ (self,name,hp,strength,defense,artfulness): ##atributos##
            self.name = name
            self.hp = hp
            self.strength = strength
            self.defense = defense
            self.artfulness = artfulness

        def its_alive(self):
            return self.hp>0

        def death(self):
            self.hp=0
            print(self.name,"Ha muerto")

        def attack(self,e):
            damage = self.damage(e)
            e.hp = e.hp - damage
            print(self.name, "ha realizado",damage,"puntos de hp a", e.name)
            if e.its_alive():
                print("hp restante de", e.name, "es:", e.hp)
            else:
                e.death()

class Hero(Champ):
    def __init__(self, name,hp,strength,defense,artfulness,sword):
        self.name = "Heroe" 
        super().__init__(name,hp,strength,defense,artfulness) 
        self.sword = sword
        self.weapon = "Espada básica"
        self.turns = 0
    def get_name(self):
        return self.name

    def heal(self, amount,enemy,number):
        amount = randint(10,30)
        self.hp += amount
        number = randint(1,10)
        if number>=1 and number < 5: 
            enemy.attack(self)
        else:
            print("Has esquivado el ataque")
            print("Te has curado", amount,"puntos de vida")
            print("Tienes:",self.hp, "puntos de vida")

    def mission(self):
        print("Tienes la mision de ser un heroe y salvar este mundo del Rey demonio")

    def change_weapon(self, weapon):
        self.weapon = weapon
    def damage(self,e):
        if self.weapon == "Espada básica":
            return self.artfulness - e.defense
        elif self.weapon == "Espada de fuego":
            return self.artfulness*1.5 - e.defense
        elif self.weapon == "Espada de hielo":
            return self.artfulness*0.8 - e.defense

    def special_attack(self,e):
        print("A costa de un poco de tus puntos de vida, canalizas tu fuerza en un punto")
        damage = self.damage(e)*1.8
        self.hp -= 8
        e.hp = e.hp - damage
        print(self.name, "ha realizado",damage,"puntos de hp a", e.name)
        if e.its_alive():
            print("hp restante de", e.name, "es:", e.hp)
        else:
            e.death()

class Enemy(Champ):
    def __init__(self,name,hp,strength,defense,artfulness):
        super().__init__(name,hp,strength,defense,artfulness)
        self.turns = 0
        
    def damage(self, p):
        return self.artfulness + self.strength - p.defense

    def name_enemy(self, enemy_name):
        self.name = enemy_name

e = Enemy(name= "Rey demonio",hp = randint(80,150),strength=randint(30,60),defense=randint(10,20),artfulness=randint(10,30))
p = Hero(input("Ingresa tu nombre heroe: "),hp=150,strength=10,defense=10,artfulness=50,sword=5)

def menu_stats(p,e):
    print("Estadísticas del jugador")
    print("*****************")
    print(f"Tu eres el heroe {p.get_name()}")
    print(f"\nHp: {p.hp}")
    print(f"\nDaño: {p.damage(e)}")
    print(f"\nFuerza: {p.strength}")  
    print(f"\nDefensa: {p.defense}") 
    input("Presione Enter para continuar.")

def battle(hero, enemy):
    hero.attack(enemy)
    enemy.attack(hero)
    if hero.hp <= 0:
        print("Has sucumbido a las fuerzas del rey demonio, ahora el mundo sera governado por su raza creando una nueva raza para su reino.")
    elif enemy.hp <= 0:
        print("Felicidades, has logrado oprimir a toda una raza a la fuerza, ahora los demonios seran tratados como esclavos gracias a ti :).")
    elif hero.hp <= 0 and enemy.hp <= 0:
        print("Al caer los 2 en combate, tanto los humanos como los demonios se vieron obligados a convivir entre si creando una era de paz.")

def special_battle(hero, enemy):
    hero.special_attack(enemy)
    enemy.attack(hero)
    if hero.hp <= 0:
        print("Has sucumbido a las fuerzas del rey demonio, ahora el mundo sera governado por su raza creando una nueva raza para su reino.")
    elif enemy.hp <= 0:
        print("Felicidades, has logrado oprimir a toda una raza a la fuerza, ahora los demonios seran tratados como esclavos gracias a ti :).")
    elif hero.hp <= 0 and enemy.hp <= 0:
        print("Al caer los 2 en combate, tanto los humanos como los demonios se vieron obligados a convivir entre si creando una era de paz.")

def menu_weapon(self):
        option = 0
        while option != 1 and option != 2:
            print("Elige tu espada:")
            option = int(input("1) Espada de fuego: Daño+ Defensa++ |2)Espada de hielo: Daño+++ hp-\n"))
            if option == 1:
                self.change_weapon("Espada de fuego")
                self.defense += 10
                print("se han cambiado tus datos\n Arma: Espada de fuego, Defensa: +10")
            elif option == 2:
                self.change_weapon("Espada de hielo")
                self.hp -= 5
                print("se han cambiado tus datos\n Arma: Espada de hielo, HP: -5")
            else:
                print("Opción no valida, ingresa un numero entre 1 y 2.")

def menu_battle(p,e):
    while p.hp > 0 and e.hp > 0:
        print("*****************")
        print("1) Atacar")
        print("2) Curarse")
        print("3) Ataque especial")
        choice = input("Seleccione una opción: ")
        print("*****************")

        if choice == "1":
            battle(p, e)
        elif choice == "2":
            p.heal(1,e,0)
        elif choice == "3":
            special_battle(p, e)


def menu():
    while True:
        print("Menu principal:")
        print("1) Ver estadísticas del jugador")
        print("2) Cambiar arma")
        print("3) Iniciar batalla")
        print("4) Salir")
        option = int(input("Elije una opción: "))
        if option == 1:
            menu_stats(p,e)
        elif option == 2:
            menu_weapon(p)
        elif option == 3:
            menu_battle(p, e)
            break
        elif option == 4:
            print("Hasta luego!")
            break
        else:
            print("Opción no valida, ingresa un numero entre 1 y 4.")

print("*********Bienvenido a este mundo Isekai,donde cuenta la profecia de que eres el Heroe que matara al Rey Demonio*********")
menu()