# Lab 6: Code and Branch Coverage — Ski Resort Pass System

## 1. Overview

This lab focuses on testing the Ski Resort Pass application using Python, `pytest`, and `coverage.py`. The objective is to evaluate code coverage and branch coverage by executing test cases against the application's functions.

## 2. Objectives

- Test the functionality of the Ski Resort Pass application.
- Measure code coverage using `coverage.py`.
- Measure branch coverage using branch analysis.
- Test different booking scenarios, validation conditions, and chairlift safety conditions.
- Generate terminal reports and screenshots showing the coverage results.

## 3. Technologies Used

- **Python** — Application and test implementation
- **pytest** — Automated testing framework
- **coverage.py** — Code and branch coverage measurement
- **Git and GitHub** — Version control and submission

## 4. Project Structure

```text
Lab 6/
├── ski_resort_pass.py
├── test_ski_resort.py
├── CodeCoverageTest_PES2UG24CS194_application.py
├── BranchCoverageTest_PES2UG24CS194_application.py
├── CodeCoverage_PES2UG24CS194.png
└── BranchCoverage_PES2UG24CS194.png
```

## 5. Application Functions Tested

### `process_resort_bookings()`

The test cases cover:

- Input validation and invalid facility fees
- Active and inactive booking groups
- Season, full-day, and half-day passes
- Age-based pricing and gear rental charges
- Blackout overrides
- Locker facility fees
- Rejected passes, zero sales, and audit review conditions

### `check_chairlift_anemometer()`

The test cases cover:

- Empty or missing wind data
- Safe wind conditions
- Consecutive high-wind gusts
- Chairlift suspension conditions

## 6. Code Coverage Testing

The code coverage tests are implemented in:

`CodeCoverageTest_PES2UG24CS194_application.py`

Run the following commands from the `Lab 6` directory:

```bash
python -m coverage erase
python -m coverage run --source=ski_resort_pass -m pytest -q CodeCoverageTest_PES2UG24CS194_application.py
python -m coverage report -m
```

**Result:**
- Tests passed: 12
- Code coverage achieved: **98%**

Screenshot: `CodeCoverage_PES2UG24CS194.png`

## 7. Branch Coverage Testing

The branch coverage tests are implemented in:

`BranchCoverageTest_PES2UG24CS194_application.py`

Run the following commands:

```bash
python -m coverage erase
python -m coverage run --branch --source=ski_resort_pass -m pytest -q BranchCoverageTest_PES2UG24CS194_application.py
python -m coverage report -m
```

**Result:**
- Tests passed: 8
- Statements covered: 59/59
- Branches covered: 42/42
- Branch coverage achieved: **100%**

Screenshot: `BranchCoverage_PES2UG24CS194.png`

## 8. Summary of Results

| Metric | Result |
|---|---:|
| Code coverage tests passed | 12/12 |
| Code coverage | 98% |
| Branch coverage tests passed | 8/8 |
| Branches covered | 42/42 |
| Branch coverage | 100% |

Both code coverage and branch coverage exceeded the required 90% target.

## 9. Version Control

The test files and coverage screenshots were committed and pushed to the GitHub repository.

Repository: [L6_L7_08_ski_resort_pass](https://github.com/Himani-PES2UG24CS194/L6_L7_08_ski_resort_pass)

## 10. Conclusion

The Ski Resort Pass application was tested using automated Python test cases. The testing process achieved 98% code coverage and 100% branch coverage. The results demonstrate that the test suite exercised nearly all application statements and all identified branches, meeting the lab's coverage objectives.
