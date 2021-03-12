"""Console view."""


# One view per controller / same name


class ConsoleView:
    """ConsoleView class."""

    @staticmethod
    def select_product() -> int:
        """Prompt the user to select a product."""
        return int(input("Sélectionnez le produit : "))

    @staticmethod
    def select_category() -> int:
        """Prompt the user to select a category."""
        return int(input("Sélectionnez la catégorie : "))

    @staticmethod
    def display_choice(key, value):
        """Display the index related to the product / category."""
        print(f"{key} : {value}")

    @staticmethod
    def jump_line():
        """Line jump."""
        print()
