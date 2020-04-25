#how to load setting module directly
from django_seed import Seed
from expenses.models import Expense, Category
from django.contrib.auth.models import User

# from django.conf import settings
# settings.configure()

seeder = Seed.seeder(locale='en_US')


seedUser = User.objects.get(pk=3)
seedCategory = Category.objects.get(pk=1)

seeder.add_entity(Expense, 10, {
    'user':  lambda x: seedUser,
    'category': lambda x: seedCategory,
    'currency': lambda x: "AED",
    'payment_method': lambda x: "Cash",
})

inserted_pks = seeder.execute()
print(inserted_pks)