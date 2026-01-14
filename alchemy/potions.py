#!/usr/bin/python3


def healing_potion():
    from .elements import create_fire
    from .elements import create_water

    fire = create_fire()
    water = create_water()
    return f"Healing potion brewed with {fire} and {water}"


def strenght_potion():
    from .elements import create_fire
    from .elements import create_earth

    fire = create_fire()
    earth = create_earth()
    return f"Strenght potion brewed with {earth} and {fire}"


def invisibility_potion():
    from .elements import create_water
    from .elements import create_air

    air = create_air()
    water = create_water()
    return f"Invisibility portion brewed with {air} and {water}"


def wisdom_potion():
    from .elements import create_water
    from .elements import create_fire
    from .elements import create_earth
    from .elements import create_air
    
    earth = create_earth()
    air = create_air()
    fire = create_fire()
    water = create_water()
    return f"Wisdom potion brewed with all "\
           f".elements: {earth}, {air}, {fire}, {water}"
