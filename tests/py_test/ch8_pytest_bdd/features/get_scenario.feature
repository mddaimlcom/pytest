Feature: Get Companies
    Get the companies present in the db

    Scenario: On a rest db
        Given There are 3 records in the db

        When I perform simple get request

        Then I get exactly 3 records
        And the records are as follows [{"id":  1, "name":  "Company 1", "reg_num":  1234567891}, {"id":  2, "name":  "Company 2", "reg_num":  1234567892}, {"id":  3, "name":  "Company 3", "reg_num":  1234567893}]