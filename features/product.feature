Feature: Product management

Scenario: Reading a product from the system
    Given the following products exist in the system
      | id  | name        | category  | available |
      | 1   | Product 1   | Category A| True      |
      | 2   | Product 2   | Category B| False     |
    When I search for product with id 1
    Then I should see the product details
      | id  | name        | category  | available |
      | 1   | Product 1   | Category A| True      |

Scenario: Updating a product in the system
    Given the following products exist in the system
      | id  | name        | category  | available |
      | 1   | Product 1   | Category A| True      |
      | 2   | Product 2   | Category B| False     |
    When I search for product with id 1
    Then I should see the product details
      | id  | name        | category  | available |
      | 1   | Product 1   | Category A| True      |
    When I update the product with id 1 to change the name to "Updated Product 1" and availability to False
    Then I should see the success message
    When I retrieve the product with id 1
    Then I should see the updated details
      | id  | name            | category  | available |
      | 1   | Updated Product 1| Category A| False     |
    When I search for product with id 1
    Then I should see the updated details
      | id  | name            | category  | available |
      | 1   | Updated Product 1| Category A| False     |

Scenario: Deleting a product from the system
    Given the following products exist in the system
      | id  | name        | category  | available |
      | 1   | Product 1   | Category A| True      |
      | 2   | Product 2   | Category B| False     |
    When I search for product with id 1
    Then I should see the product details
      | id  | name        | category  | available |
      | 1   | Product 1   | Category A| True      |
    When I delete the product with id 1
    Then I should see the message "Product has been Deleted!"
    When I search for product with id 1
    Then I should not see the product details

Scenario: Listing all products in the system
    Given the following products exist in the system
      | id  | name      | category  | available |
      | 1   | Hat       | Category A| True      |
      | 2   | Shoes     | Category B| True      |
      | 3   | Big Mac   | Category C| False     |
      | 4   | Sheets    | Category D| True      |
    When I press the Clear button to clear previous entries
    And I press the Search button
    Then I should see the message "Success"
    And I should see the following products in the results:
      | name      | category  | available |
      | Hat       | Category A| True      |
      | Shoes     | Category B| True      |
      | Big Mac   | Category C| False     |
      | Sheets    | Category D| True      |

Scenario: Searching a product by category
    Given the following products exist in the system
      | id  | name      | category  | available |
      | 1   | Hat       | Category A| True      |
      | 2   | Shoes     | Category B| True      |
      | 3   | Big Mac   | Food      | False     |
      | 4   | Sheets    | Category D| True      |
    When I press the Clear button to clear previous entries
    And I select the "Food" category from the dropdown
    And I press the Search button
    Then I should see the message "Success"
    And I should see "Big Mac" in the results
    And I should not see the following products in the results:
      | name  | category  | available |
      | Hat    | Category A| True      |
      | Shoes  | Category B| True      |
      | Sheets | Category D| True      |

Scenario: Searching a product by availability
    Given the following products exist in the system
      | id  | name      | category  | available |
      | 1   | Hat       | Category A| True      |
      | 2   | Shoes     | Category B| False     |
      | 3   | Big Mac   | Food      | True      |
      | 4   | Sheets    | Category D| False     |
    When I set the "Available" dropdown to "True"
    And I press the Search button
    Then I should see the message "Success"
    And I should see the following available products in the results:
      | name    | category   | available |
      | Hat     | Category A | True      |
      | Big Mac | Food       | True      |
    And I should not see the following unavailable products in the results:
      | name    | category   | available |
      | Shoes   | Category B | False     |
      | Sheets  | Category D | False     |

Scenario: Searching a product by name
    Given the following products exist in the system
      | id  | name      | category  | available |
      | 1   | Hat       | Category A| True      |
      | 2   | Shoes     | Category B| False     |
      | 3   | Big Mac   | Food      | True      |
      | 4   | Sheets    | Category D| False     |
    When I enter "Hat" in the Name field
    And I press the Search button
    Then I should see the message "Success"
    And I should see the following product in the results:
      | name    | category   | available |
      | Hat     | Category A | True      |
    And I should not see any other products in the results