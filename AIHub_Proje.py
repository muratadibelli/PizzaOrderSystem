import csv
from datetime import *
import time
# Sınıfları tanımlayalım.
class Pizza:
    def __init__(self, description, price):
        self._description = description
        self._price = price

    def get_description(self):
        return self._description

    def get_cost(self):
        return self._price


class ClassicPizza(Pizza):
    def __init__(self):
        super().__init__("Klasik Pizza", 120.0)

class MargheritaPizza(Pizza):
    def __init__(self):
        super().__init__("Margarita Pizza", 130.0)

class TurkishPizza(Pizza):
    def __init__(self):
        super().__init__("Türk Pizza", 135.0)

class SadePizza(Pizza):
    def __init__(self):
        super().__init__("Sade Pizza", 100.0)

        
# Decorator sınıfı
class Decorator(Pizza):
    def __init__(self, component):
        super().__init__(component.get_description(), component.get_cost())
        self.component = component

    def get_cost(self):
        return self.component.get_cost() + super().get_cost()

    def get_description(self):
        return self.component.get_description() + ' ' + super().get_description()


class Zeytin(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self._description = "ve Zeytin"
        self._price = 10.0


class Mantar(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self._description = "ve Mantar"
        self._price = 14.0


class KeciPeyniri(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self._description = "ve Keçi Peyniri"
        self._price = 16.0

class Et(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self._description = "ve Et"
        self._price = 22.0

class Sogan(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self._description = "ve Soğan"
        self._price = 11.0

class Misir(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self._description = "ve Mısır"
        self._price= 10.0

def print_menu():
    with open('Menu.txt', 'r', encoding='utf-8') as menu_file:
        menu = menu_file.read()
    print(menu)

print("""\tMerhaba! Pizza Sipariş Sistemine Hoş Geldiniz. Menü Aşağıda Sunulmuştur.
-------------------------------------------------------------------------------""")
time.sleep(0.4)
print_menu()
global pizza
global sos

while True:
    # Kullanıcıdan pizza seçimini isteyelim.
    pizza_choice = input("Lütfen Pizza Tabanı Seçimi Yapınız: ")

    if pizza_choice == "1":
        pizza = ClassicPizza()
        break
    elif pizza_choice == "2":
        pizza = MargheritaPizza()
        break
    elif pizza_choice == "3":
        pizza = TurkishPizza()
        break
    elif pizza_choice == "4":
        pizza = SadePizza()
        break
    else:
        print("Geçersiz bir pizza seçimi yaptınız.")
        continue

time.sleep(0.4)
# Kullanıcıdan sos seçimini isteyelim.
while True:
    sos_choice = input("Lütfen Bir Sos Seçimi Yapınız: ")

    if sos_choice == "11":
        sos = Zeytin(pizza)
        break
    elif sos_choice == "12":
        sos = Mantar(pizza)
        break
    elif sos_choice == "13":
        sos = KeciPeyniri(pizza)
        break
    elif sos_choice == "14":
        sos = Et(pizza)
        break
    elif sos_choice == "15":
        sos = Sogan(pizza)
        break
    elif sos_choice == "16":
        sos = Misir(pizza)
        break
    else:
        print("Geçersiz bir sos seçimi yaptınız.")
        continue
# Sipariş Özeti
time.sleep(0.4)
print("---------------------------------------------------")
print(f"Sipariş Özeti: {sos.get_description()}")
total_price = sos.get_cost()
time.sleep(0.4)
# Toplam fiyatı hesapla ve ekrana yazdır
print(f"Toplam fiyat: ₺{total_price}")
print("---------------------------------------------------")
# Kullanıcı bilgileri.
def get_user_info():
    while True:
        name = input("İsim: ")
        if any(char.isdigit() for char in name):
            print("İsimde sayı kullanılamaz. Tekrar deneyin.")
            continue
        else:
            break

    while True:
        tc = input("TC Kimlik Numarası: ")
        if len(tc) != 11 and tc.isdigit():
            print("TC Kimlik Numarası 11 Haneden Oluşmalıdır.")
            continue
        elif not tc.isdigit():
            print("TC Kimlik Numarası Sadece Sayılardan Oluşmalıdır.")
        else:
            break

    while True:
        card_number = input("Kredi Kartı Numarası: ")
        if not card_number.isdigit() or len(card_number) != 16:
            print("Kredi kartı numarası 16 haneli olmalıdır ve sadece sayılardan oluşmalıdır.")
            continue
        else:
            break

    while True:
        card_pw = input("Kredi Kartı Şifresi: ")
        if len(card_pw) != 4 or not card_pw.isdigit():
            print("Kredi kartı şifresi 4 haneli olmalıdır ve sadece sayılardan oluşmalıdır.")
            continue
        else:
            break

    return name, tc, card_number, card_pw

name, tc, card_number, card_pw = get_user_info()
order_time = datetime.now()
order_time = datetime.ctime(order_time)

with open("Siparis_veritabani.csv", mode="a", newline="") as orders_file:
    orders_writer = csv.writer(orders_file, delimiter="|", quotechar='"', quoting=csv.QUOTE_MINIMAL)
    orders_writer.writerow(
        [f"İsim: {name} | TC: {tc} | Kart Numarası: {card_number} | Kart Şifresi: {card_pw} | Sipariş Zamanı: {order_time} | Sipariş İçeriği: {sos.get_description()} | Tutar: ₺{total_price}"])
print("Siparişiniz başarıyla oluşturuldu. Teşekkür ederiz!")
