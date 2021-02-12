total_money_collected = 0


def has_raw_materials(f_raw_materials, d_raw_materials):
    """Check if there are enough raw materials in the machine

    Params:
        f_raw_materials: dict
        d_raw_materials: dict

    Returns:
        str or bool
    """
    additional_resources_needed = ''
    for f_raw_material in f_raw_materials:
        if f_raw_materials[f_raw_material] > d_raw_materials[f_raw_material]:
            additional_resources_needed += 'Machine Needs Additional: {0}\n'.format(f_raw_material)
    if additional_resources_needed:
        return additional_resources_needed
    else:
        return True


def collect_money(f_max_value, m_quarters, m_dimes, m_nickels):
    """Collect money into the machine

    Params:
        f_max_value: float

    Returns:
        float or str
    """
    try:
        money_collected = int(m_quarters) * 0.25
        money_collected += int(m_dimes) * 0.10
        money_collected += int(m_nickels) * 0.05
        if money_collected <= 0.00:
            return 'Insufficient funds...  Dispensing coins inserted.'
        elif money_collected >= f_max_value:
            return 'Machine can\'t hold more than ${0:.2f}...  Dispensing coins inserted.'.format(f_max_value)
        else:
            return money_collected
    except ValueError:
        return 'Please enter valid currency.\n'


def has_enough_money(f_money_collected, f_chocolate_price):
    """Check to see if customer put in enough money into the machine

    Params:
        f_money_collected: float
        f_chocolate_price: float

    Returns:
        str
    """
    if f_money_collected >= f_chocolate_price:
        excess_money_collected = round(f_money_collected - f_chocolate_price, 2)
        global total_money_collected
        total_money_collected += f_chocolate_price
        return 'Change: ${0:.2f}\n'.format(excess_money_collected)
    else:
        return 'Insufficient funds...  Dispensing coins inserted.\n'


def bake_chocolate_bar(f_chocolate_choice, f_raw_materials, d_raw_materials):
    """Bake chocolate bar from raw materials

    Params:
        f_chocolate_choice: str
        f_raw_materials: dict
        d_raw_materials: dict

    Returns:
        str
    """
    for f_raw_material in f_raw_materials:
        d_raw_materials[f_raw_material] -= f_raw_materials[f_raw_material]
    return 'A {0} chocolate bar dispensed!'.format(f_chocolate_choice)


def stats(d_raw_materials):
    """
    Show machine statistics

    Params:
        d_raw_materials: dict

    Returns:
        str
    """
    cm_stats = 'sugar {0} tablespoons remaining\n'.format(d_raw_materials['sugar'])
    cm_stats += 'butter {0} teaspoons remaining\n'.format(d_raw_materials['butter'])
    cm_stats += 'dark chocolate {0} tablespoons remaining\n'.format(d_raw_materials['dark chocolate'])
    cm_stats += 'mint chocolate {0} tablespoons remaining\n'.format(d_raw_materials['mint chocolate'])
    cm_stats += 'milk chocolate {0} tablespoons remaining\n'.format(d_raw_materials['milk chocolate'])
    cm_stats += 'light corn syrup {0} teaspoons remaining\n'.format(d_raw_materials['light corn syrup'])
    cm_stats += 'sweetened condensed milk {0} teaspoons remaining\n'.format(d_raw_materials[
        'sweetened condensed milk'])
    cm_stats += 'vanilla extract {0} teaspoons remaining\n'.format(d_raw_materials['vanilla extract'])
    cm_stats += 'Reese\'s Pieces {0} tablespoons remaining\n'.format(d_raw_materials['Reese\'s Pieces'])
    cm_stats += 'Total Money Collected: ${0:.2f}\n'.format(total_money_collected)
    return cm_stats

