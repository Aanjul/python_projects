# For refrence https://levelup.gitconnected.com/10-interesting-python-programs-with-code-b676181a2d1a

# Requirements
# using "pip install Faker" in the terminal. 



from faker import Faker
fake = Faker()
print(fake.name())
print(fake.email())
print(fake.country())

print(fake.profile())

#Note: Try checking all the methods in Faker using dir(Faker())syntax. There are numerous interesting methods like fake text, fake credit card numbers, and many more.