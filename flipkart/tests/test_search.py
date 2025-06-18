import pytest

from Pom.searchpage import FlipkartSearchPage


@pytest.mark.usefixtures("setup")
class TestSearch:

    def test_search_item(self,setup):
        flipkart_search_page = FlipkartSearchPage()
        item_to_search = "Your Item Name"
        flipkart_search_page.search_for_item(item_to_search)