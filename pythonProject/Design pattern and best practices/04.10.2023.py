# region 1. DP behavioural

"""
Command
Chain of responsability
Interpreter
Mediator
Observer
State
Strategy
Template
Visitor
Memento
Iterator
"""
import pickle
# endregion

# region 2. Command
from abc import ABC, abstractmethod

"""
 - adauga un intermediar intre cel care face o cerere si cel care satisface aceasta cerinta
 - ex: telecomanda ca intermediar intre privitor si tv
"""

class Command(ABC):

    @abstractmethod
    def execute(self):
        pass

class SimpleCommand(Command):

    def __init__(self, string_to_print):
        self.string_to_print = string_to_print

    def execute(self):
        print(f"Simple command: printing {self.string_to_print}")

class Receiver:   # clasa auxiliara pt clasa ComplexCommand

    def do_something(self, task):
        print(f"Receiver works on {task}")

    def do_something_else(self, task):
        print(f"Receiver works harder on {task}")

class ComplexCommand(Command):

    def __init__(self, receiver, step1, step2):
        self.receiver = receiver
        self.step1 = step1
        self.step2 = step2

    def execute(self):
        print("Complex command is executed by receiver")
        self.receiver.do_something(self.step1)
        self.receiver.do_something_else(self.step2)

class Invoker:
    def __init__(self, command):
        self.command = command

    def invoke(self):
        self.command.execute()

simple = SimpleCommand("Grupa 52")
invoker = Invoker(simple)
invoker.invoke()

complex = ComplexCommand(Receiver(), "step1: send mail", "step2: save work")
invoker2 = Invoker(complex)
invoker2.invoke()

# endregion

# region 3. DP behavioural discutate teoretic

"""
CHAIN OF RESPONSABILITY
 - se creeaza un lant de potentiale raspunsuri la requestul clientului
 - cererea trece prin aceasta lista pana cand gaseste raspunsul potrivit
 
INTERPRETER
 - folosit in arhitecturi care cer recunoasterea unui limbaj de programare
 - se incearca clasificarrea unei expresii in terminala (recunoscuta ca apartinand unui limbaj de programare) sau
non-terminala (avem nevoie ca expresia sa fie impartita in expresii mai mici care vor fi analizate

MEDIATOR
 - simplifica comunicarea intre obiecte
 - reduce nr de dependinte dintre obiecte, acestea fiind independente unele de altele, insa comunica permanent
 
OBSERVER
 - observerul reactioneaza la un state change al observabilului
 
STATE
 - un obiect reactioneaza cand propria stare se schimba
 - ex: bubble gum machine (bagi o moneda ca sa iti elibereze guma)
 
STRATEGY
 - folosit in luarea deciziilor la runtime
 - noi definim setul de strategii, insa decizia finala va fi aleasa la runtime, nu putem intui noi rezultatul
 - ex: joc de hartie - piatra - foarfeca  https://auth0.com/blog/strategy-design-pattern-in-python/
 
TEMPLATE
 - ofera scheletul unui proces
 - clase copil mostenesc o clasa abstracta, unde avem metode abstracte si metode normale; metodele abstracte vor fi
mereu suprascrise de clasele copil, iar metodele normale pot fi suprascrise sau nu
 - ex: https://refactoring.guru/design-patterns/template-method/python/example
 
VISITOR
 - folosit in scenariul in care vizitatorul are nevoie de ceva de la o alta componenta a aplicatiei
 - viitatorul trebuie sa fie validat de metoda accept() al componentei respective
"""

# endregion

# region 4. ITERATOR - sirul lui Fibonacci

"""
- folosit pt a crea structuri iterabile, adica care pot fi parcurse elemenet cu element printr-un FOR
- in implementare vom avea in vedere:
1. metodele __iter__ si __next__
2. declansarea exceptiei StopIteration care stopeaza iterarea
- acest DP este implementat by default de liste, tupluri, stringuri
"""

# sirul lui Fibonacii = fiecare nr este suma celor doua nr anterioare:0,1,1,2,3,5,8,13 etc

class FibonacciIterator:

    def __init__(self, n):
        self.counter = n # cate nr generam
        self.current_number = 0 # nr Fibonacci pt iteratia curenta
        self.next_number = 1 # nr Fibonacci care urmeaza

    def __iter__(self):
        return self  # self reprezinta structura pe care o vom itera

    def __next__(self):
        if self.counter == 0:
            raise StopIteration  # am generat deja numerele fibonacci dorite

        self.counter -= 1
        new = self.current_number + self.next_number
        self.current_number = self.next_number
        self.next_number = new

        return self.current_number

""""
exemplu dry-run (adica am scris de mana codul asa cum se genereaza el)
1,1,2,
self.current_number = 1
self.next_number = 1

new = 1 + 1 = 2
self.current_number = 1
self.next_number = 2
"""

fib_50 = FibonacciIterator(50)  # generez primele 50 nr fibonacci
for fib in fib_50:
    print(fib)

# endregion

# region 5. Memento

"""
 - gestioneaza memento objects (snapshots) ale unui obiect
 - pentru implementare folosim:
 1. serializarea - pt a crea snapshot
 2. deserializarea - pt a ne intoarce la un snapshot din trecut
 - librarie: pickle
 
 Serializarea inseamna transformarea unui obiect python in secventa de bytes (stream)
 Deserializarea este citirea unui stream si recrearea obiectului python
"""
import pickle

class Person:

    def __init__(self, name = '', age = 0):  # dam valori default pt cele doua atribute
        self.name = name
        self.age = age

    def __str__(self):
        return f" Person {self.name} is {self.age} years old"

    def create_snapshot(self):
        print(f"Rezultatul din __dict__: {self.__dict__}")  # dict pastreaza toate atributele de instanta
        return pickle.dumps(self.__dict__)  # dumps() serializeazaa

    def return_to_snapshot(self, snapshot):
        self.__dict__.update(pickle.loads(snapshot))  # loads() deserializeaza
        # update actualizeaza valorile din __dict__ cu cele din snapshotul din trecut

p = Person()
p2 = Person("Anca", 36)
print(p, p2, sep = "\n")

memento1 = p2.create_snapshot()
p2.age = 40
print(p2)

p2.return_to_snapshot(memento1)
print(p2)


# endregion

# region 6. MEMENTO varianta cu fisier

class Person:

    filename = "f.pickle"

    def __init__(self, name = '', age = 0):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person {self.name} is {self.age} years ols"

    def create_snapshot(self):
        with open(Person.filename, "wb") as f:   # deschidem fisierul in modul wb = write bytes
            pickle.dump(self.__dict__, f)  # folosim dump pt serializare in fisier

    def return_to_snapshot(self):
        with open(Person.filename, "rb") as f:
            snapshot = pickle.load(f)  # folosim load pt deserializare din fisier
            self.__dict__.update(snapshot)

p = Person("Anca", 36)

memento = p.create_snapshot()
p.age = 40
print(p)

# endregion

# region 7. exercitiu fisiere induviduale pt snapshot

class Person:

    def __init__(self, name = '', age = 0):
        self.name = name
        self.age = age
        self.filename = f"{self.name}.pickle"

    def __str__(self):
        return f"Person {self.name} is {self.age} years ols"

    def create_snapshot(self):
        with open(self.filename, "wb") as f:   # deschidem fisierul in modul wb = write bytes
            pickle.dump(self.__dict__, f)  # folosim dump pt serializare in fisier

    def return_to_snapshot(self):
        with open(self.filename, "rb") as f:
            snapshot = pickle.load(f)  # folosim load pt deserializare din fisier
            self.__dict__.update(snapshot)


p = Person("Anca", 36)
p1 = Person("Ioana", 30)

memento = p.create_snapshot()
p.age = 40
print(p)

memento1 = p1.create_snapshot()
p1.age = 35
print(p1)

# endregion
