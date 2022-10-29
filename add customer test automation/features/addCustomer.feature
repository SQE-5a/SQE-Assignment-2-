Feature: login the megento and add customer
    

    Background: login
         Given Chrome is launched
         And   magento url is open
         When  I enter email as "shapito" and password as "shapitoltd786$"
         And   I click on signin button
         Then  I should be logged in

    Scenario Outline: add customer
        Given I am on dashboard
        When  I click on customers logo
        And   I click all customers
        And   I click on all add new customer button
        And   I select group as "retailer" 
        And   I enter name prefix as "<prefix>"
        And   I enter first name as "<Fname>"
        And   I enter middle name as "<initial>"
        And   I enter Last name as "<Lname>"
        And   I enter name suffix as "<suffix>"
        And   I enter email as "<email>"
        And   I enter DOB as "<DOB>"
        And   I enter tax as "<taxNo>"
        And   I select gender as "<gender>"
        And   I select welcome email as "<welEmail>"  
        And   I click on save customer button
        Then  New customer will be added

    Examples:
        | group    | prefix   | Fname    | initial | Lname   | suffix | email            |   DOB        | taxNo | gender |   welEmail   |
        | Wholesale | irt      | irtaza   |  o     | zulfiqar|  zul   | irtaza@gmail.com | 10/12/2001   |  001  | Male   |  Main Website|


        
  