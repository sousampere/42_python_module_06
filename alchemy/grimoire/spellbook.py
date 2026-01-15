#!/usr/bin/python3

def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients # late import
    validation = validate_ingredients(ingredients)
    if ("INVALID" in validation[-7:]):
        return f"Spell rejected: {spell_name} ({validation})"
    return f"Spell recorded: {spell_name} ({validation})"
