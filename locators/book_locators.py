class BookLocators:
    """
    Locators for an item in the HTML page.

    This allows us to easily see what our code will be looking at
    as well as change it quickly if we notice it is now different.
    """
    NAME_LOCATOR = 'article.product_pod h3 a' 
    LINK_LOCATOR = 'article.product_pod h3 a'
    RATING_LOCATOR = 'article.product_pod p.star-rating'
    PRICE_LOCATOR = 'article.product_pod p.price_color'
    AVAILABILITY_LOCATOR = 'div.product_price p.instock'