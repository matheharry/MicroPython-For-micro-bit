CHOCOLATE_CHOICES = {
    'dark': {
        'ingredients': {
            'sugar': 1,
            'butter': 1,
            'dark chocolate': 6,
            'light corn syrup': 1,
            'sweetened condensed milk': 1,
            'vanilla extract': 1,
        },
        'price': 2.75,
    },
    'mint': {
        'ingredients': {
            'sugar': 1,
            'butter': 1,
            'mint chocolate': 6,
            'light corn syrup': 1,
            'sweetened condensed milk': 1,
            'vanilla extract': 1,
        },
        'price': 2.50,
    },
    'caramel': {
        'ingredients': {
            'sugar': 1,
            'caramel': 3,
            'butter': 1,
            'milk chocolate': 6,
            'light corn syrup': 1,
            'sweetened condensed milk': 1,
            'vanilla extract': 1,
        },
        'price': 3.25,
    },
    'surprise': {
        'ingredients': {
            'sugar': 1,
            'Reese\'s Pieces': 3,
            'butter': 1,
            'milk chocolate': 6,
            'light corn syrup': 1,
            'sweetened condensed milk': 1,
            'vanilla extract': 1,
        },
        'price': 3.25,
    },
}

raw_materials = {
    'sugar': 5,
    'butter': 5,
    'caramel': 15,
    'dark chocolate': 30,
    'mint chocolate': 30,
    'milk chocolate': 30,
    'light corn syrup': 5,
    'sweetened condensed milk': 5,
    'vanilla extract': 5,
    'Reese\'s Pieces': 15,
}


class Machine:
    """
    Base class to represent a generic vending machine
    """
    def __init__(self):
        """
        Attrs:
            self.__money_collected: float
            self.__total_money_collected: float
            self.__price: float
        """
        self.__money_collected = 0
        self.__total_money_collected = 0
        self.__price = 0

    def stats(self):
        """
        Show machine statistics
        """
        return 'Total Money Collected: ${0:.2f}\n'.format(self.__total_money_collected)

    def collect_money(self, max_value):
        """
        Collects money into machine

        Params:
            max_value: float

        Returns:
            float or str
        """
        try:
            self.__money_collected = int(input('Quarters: ')) * 0.25
            self.__money_collected += int(input('Dimes: ')) * 0.10
            self.__money_collected += int(input('Nickels: ')) * 0.05
            if self.__money_collected <= 0.00:
                return 'Please enter coins...'
            elif self.__money_collected >= max_value:
                return 'Machine can\'t hold more than ${0:.2f}...\n'.format(max_value)
            else:
                return self.__money_collected
        except ValueError:
            return 'Please enter valid currency...  Dispensing any coins inserted.\n'

    def has_enough_money(self, price):
        """Check to see if customer put in enough money into the machine

        Params:
            price: float

        Returns:
            str
        """
        excess_money_collected = round(self.__money_collected - price, 2)
        if self.__money_collected >= price:
            self.__total_money_collected += price
            return 'Change: ${0:.2f}'.format(excess_money_collected)
        else:
            return 'Insufficient funds...  Dispensing coins inserted.\n'.format(excess_money_collected)

    @staticmethod
    def shutdown_machine(shutdown_password):
        """Shutdown machine

        Params:
            shutdown_password: str
        """
        entered_password = input('ENTER SHUTDOWN PASSWORD: ')
        if entered_password == shutdown_password:
            return False
        else:
            return 'YOU ARE NOT AUTHORIZED TO DISABLE THIS MACHINE!\n'


class ChocolateMachine(Machine):
    """
    Child class to represent a chocolate machine inheriting from the Machine base class
    """
    def __init__(self, choices):
        """
        Attrs:
            self.choices: str
        """
        super().__init__()
        self.choices = choices

    def stats(self):
        """
        Show machine statistics
        """
        cm_stats = 'sugar {0} tablespoons remaining\n'.format(raw_materials['sugar'])
        cm_stats += 'butter {0} teaspoons remaining\n'.format(raw_materials['butter'])
        cm_stats += 'dark chocolate {0} tablespoons remaining\n'.format(raw_materials['dark chocolate'])
        cm_stats += 'mint chocolate {0} tablespoons remaining\n'.format(raw_materials['mint chocolate'])
        cm_stats += 'milk chocolate {0} tablespoons remaining\n'.format(raw_materials['milk chocolate'])
        cm_stats += 'light corn syrup {0} teaspoons remaining\n'.format(raw_materials['light corn syrup'])
        cm_stats += 'sweetened condensed milk {0} teaspoons remaining\n'.format(raw_materials[
            'sweetened condensed milk'])
        cm_stats += 'vanilla extract {0} teaspoons remaining\n'.format(raw_materials['vanilla extract'])
        cm_stats += 'Reese\'s Pieces {0} tablespoons remaining\n'.format(raw_materials['Reese\'s Pieces'])
        cm_stats += super(ChocolateMachine, self).stats()
        return cm_stats

    @staticmethod
    def has_raw_materials():
        """Check if there are enough raw materials in the machine

        Returns:
            str or False
        """
        additional_resources_needed = ''
        for raw_material in raw_materials:
            if raw_materials[raw_material] > raw_materials[raw_material]:
                additional_resources_needed += 'Machine Needs Additional: {0}'.format(raw_material)
        if additional_resources_needed:
            return additional_resources_needed
        else:
            return False

    def bake_chocolate_bar(self):
        """
        Bake chocolate bar from raw materials

        Returns:
            str
        """
        for raw_material in raw_materials:
            raw_materials[raw_material] -= raw_materials[raw_material]
        return 'A {0} chocolate bar dispensed!\n'.format(self.choices)


chocolate_machine_active = True
CHOICES = ('dark', 'caramel', 'mint', 'surprise', 'stats', 'shutdown')

chocolate_machine = ChocolateMachine(CHOICES)

while chocolate_machine_active:
    valid_choice = False
    choice = input('ORDER [dark - caramel - mint - surprise]: ')
    if choice in CHOICES:
        valid_choice = True
    else:
        print('That is not a valid selection...\n')
    if choice == 'shutdown':
        not_authorized = chocolate_machine.shutdown_machine('8675309')
        if not_authorized:
            print(not_authorized)
    elif choice == 'stats':
        stats = chocolate_machine.stats()
        print(stats)
    elif valid_choice:
        selection = CHOCOLATE_CHOICES[choice]
        chocolate_machine.has_raw_materials()
        money = chocolate_machine.collect_money(100.00)
        if not isinstance(money, float):
            print(money)
        else:
            not_enough_money = chocolate_machine.has_enough_money(selection['price'])
            if not_enough_money:
                print(not_enough_money)
            else:
                chocolate_bar = chocolate_machine.bake_chocolate_bar()
                print(chocolate_bar)
    elif valid_choice:
        chocolate_machine_active = False

print('We are going down for maintenance...')
