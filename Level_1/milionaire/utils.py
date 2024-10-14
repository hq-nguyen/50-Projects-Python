def format_money(amount):
    """Formats the money value with commas for better readability."""
    return f"${amount:,}"

def is_milestone_reached(current_money, milestones):
    """Checks if the player's current money is a milestone."""
    return current_money in milestones
