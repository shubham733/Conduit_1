from faker import Faker


def generate_random_credentials():
    faker = Faker()
    username = faker.user_name()
    email = faker.email()
    return username, email


username, email = generate_random_credentials()
