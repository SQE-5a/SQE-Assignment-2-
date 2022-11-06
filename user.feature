Feature: Add to cart


    Background: Chrome
         Given Chrome is launched


    Scenario: add to cart
        Given I am on my account
        When  I click on whats new
        And   I click on jackets
        And   I choose the jacket
        And   I select size
        And   I select color
        And   I click add to cart
        Then  Product will get added
