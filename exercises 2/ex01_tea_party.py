"""Tea Party Program"""

__author__: str = "730822339"


def main_planner(guests: int) -> None:
    """Entry point function to calculate and print tea party details."""
    tea_count = tea_bags(people=guests)
    treat_count = treats(people=guests)
    total_cost = cost(tea_count=tea_count, treat_count=treat_count)

    print(f"A Cozy Tea Party for {guests} People")
    print(f"Tea Bags: {tea_count}")
    print(f"Treats: {treat_count}")
    print(f"Cost: ${total_cost}")


def tea_bags(people: int) -> int:
    """Calculates number of tea bags needed."""
    return people * 2


def treats(people: int) -> int:
    """
    Calculates the number of treats needed for a tea party.
    Each tea a guest drinks requires 1.5 treats on average.
    """
    tea_count = tea_bags(people=people)
    return int(tea_count * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculate the total cost of tea bags and treats for a tea party
    Each tea bag costs 0.50, and each treeat costs 0.75.
    """
    tea_cost = tea_count * 0.50
    treat_cost = treat_count * 0.75
    return tea_cost + treat_cost


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party")))
