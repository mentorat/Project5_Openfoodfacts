"""Main_page controller."""


from app.views.main_page import MainPageView


class MainPage:
    """Manage the application."""

    def __init__(self):
        """Initialise."""
        self.main_page_view = MainPageView()

    def get_input(self) -> int:
        """Return user's interface choice."""
        user_choice = self.main_page_view.select_interface()
        return user_choice
