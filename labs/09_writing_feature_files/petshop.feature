Feature: Search for pets by category
	As a path customer
	I need to be able to search for a pet by category
	So that I only see the category of pet I'm interested in buying

	Background:
		Given the following  pets
			| name  | category | available |
			| Fido  | dog      | True      |
			| Kitty | cat      | True      |
			| Leo   | lion     | True      |

	Scenario: Search for dogs
		Given I am on the "Home Page"
		When I set the "Category" to "dog"
		And I click the "Search" button
		Then I should see the message "Success"
		And I should see the "Fido" in the results