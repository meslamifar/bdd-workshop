# feature files written by non-technical people
# use space or tab for indentation,
# put comment anywhere

@wip
Feature: New numbers
 This is a phone book application. Add new numbers

 Scenario: add a new number
 # Scenarios describe the discrete behaviours being tested, put the system in a known state
 # Steps take a line each and begin with a keyword - one of “given”, “when”, “then”, “and” or “but”
 # Steps should not include that much details
    Given Phone number "222" is not added before to the phone book
 # no user interaction, things that happened before is alright
     When I add first name "mahshad" and last name "eslamifar" with phone number "222" to the phone book
     Then "222" is successfully added to the phone book

  #Scenario: do not duplicate a phone number
     #Given Phone number "333" is already in the phone book
     #When I add first name "Sally" and last name "Kim" with phone number "333"
     #Then It is not added to the phone book