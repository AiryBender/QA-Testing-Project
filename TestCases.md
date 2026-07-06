| Test ID | Scenario                    | Expected Result                         |
| ------- | --------------------------- | --------------------------------------- |
| TC-001  | Valid login                 | Login Successful                        |
| TC-002  | Blank username              | Username Required                       |
| TC-003  | Blank password              | Password Required                       |
| TC-004  | Unknown username            | User Not Found                          |
| TC-005  | Incorrect password          | Incorrect Password                      |
| TC-006  | Password under 8 characters | Password Too Short                      |
| TC-007  | Password over 32 characters | Password Too Long                       |
| TC-008  | Missing uppercase letter    | Password Must Contain Uppercase Letter  |
| TC-009  | Missing lowercase letter    | Password Must Contain Lowercase Letter  |
| TC-010  | Missing number              | Password Must Contain Number            |
| TC-011  | Missing special character   | Password Must Contain Special Character |
| TC-012  | Password contains spaces    | Password Cannot Contain Spaces          |
