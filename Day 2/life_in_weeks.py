target_age = int(input("What's your target age? "))

age = int(input("Insert your age now: "))

ageExpectation = target_age - age

months_remaining = ageExpectation * 12
weeks_remaining = ageExpectation * 52
days_remaining = ageExpectation * 365

print(f'You have {age} years now, so you have {months_remaining} months_remaining, {weeks_remaining} weeks_remaining or {days_remaining} days_remaining left.')
