Feature: shop order

  Scenario: Order T-Shirt
    Given Open site
    And Open "T-shirts" category
    When Add item to cart and proceed
    And Go to the second cart step
    And Register new account
    And Finish order after registration
    And Open profile orders page
    Then Check at least 1 order present