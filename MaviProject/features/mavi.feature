Feature:Mavi Web Automation
  Scenario:Automation of adding a product to cart on Mavi site with Python BDD
    Given User is on homepage
    When Choose cookie settings
    When Click the search box and type "sweatshirt"
    When Click search button
    When Click on size filter
    When Apply size filter as XL
    When Click on the Fit filter
    When Apply fit filter as Oversize
    When Click on any product
    When Click on size selection
    When Choose size as XL
    When Click the Add to Cart button
    When Click the My Cart button
    Then Check that the product is in the cart
    And Close browser