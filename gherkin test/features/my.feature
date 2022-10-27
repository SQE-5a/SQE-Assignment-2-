Feature: login the megento website
    
    Scenario Outline: Scenario Outline name
         Given Chrome is launched
         And   magento url is open
         When  I enter email as "<email>" and password as "<password>"
         And   I click on signin button
        Then  I should be logged in
    Examples:
        | email | password     |  
        |shapito|shapitoltd786$|
        |shapito|shapitoltd    |
        |       |              |
        |shapito|              |
        |       |shapitoltd786$|