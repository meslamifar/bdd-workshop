Feature: different features for phone book
 search for existing ones
 add attachment

 Scenario: Search in phone book
    Given a set of phone numbers
        | number |  name |  last_name |  city     |
        | 111    |  Adam |  McLaurin  |  Toronto  |
        | 222    |  Matt |  Dalrymple |  Ottawa   |
        | 333    |  Adam |  Eslamifar |  Toronto  |
        | 444    |  Adam |  Bedi      |  Montreal |

     When we search for name "Adam"
     Then we will find two people in "Toronto"
      But we will find one person in "Montreal"
