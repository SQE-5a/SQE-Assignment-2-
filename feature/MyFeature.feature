
Feature: A Valid User is able to remove added products from the cart

Background:User is already registered , knows his valid login Pass

Scenario Outline: 
  Given chrome is opened
  And magento website is opened  
  When I click on sign in 
  And I enter email as "<email>"
  And I enter password as "<Pass>"
  And I click sign in button  
  And I click on cart
  And I click on remove button of product named as "<productName>"
  And I click on ok
  Then product named as "<removedProduct>" should not be in the cart

  Examples:

|email|Pass|productName|removedProduct|
|roni_cost@example.com|roni_cost3@example.com|Voyage Yoga Bag|Voyage Yoga Bag|