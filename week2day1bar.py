from day4 import Waiter, Bar
import time

COCKTAIL_RECIPES = {
    'cubalibre': {
        'ingredients': ('rum', 'coke', 'lemon juice'),
        'steps': ('Drop ice cubes', 'Pour lemon juice', 'Pour rum', 'Fill the rest with coke')
    }
}


class CocktailRecipe:
    def __init__(self, name: str, ingredients: tuple, steps: tuple):
        self.__name = name
        self.__ingredients = ingredients
        self.__steps = steps

    @property
    def name(self):
        return self.__name

    @property
    def steps(self):
        formatted_steps = ''
        step_number = 1
        for step in self.__steps:
            formatted_steps += f'{step_number}: {step}\n'
            step_number += 1

        return formatted_steps

    def __str__(self):
        return f'Cocktail "{self.name}". Ingredients: {", ".join(self.__ingredients)}'


class CocktailWaiter(Waiter):
    def __init__(self, name: str, age: int, experience: float, recipes: tuple):
        super().__init__(name, age, experience)
        self.__recipes = recipes

    @property
    def known_cocktails(self):
        return [recipe for recipe in self.__recipes]

    def __knows_cocktail(self, cocktail_name: str):
        for known_cocktail in self.__recipes:
            if cocktail_name.lower() == known_cocktail.lower():
                cocktail = COCKTAIL_RECIPES[cocktail_name]
                return CocktailRecipe(cocktail_name,
                                      cocktail['ingredients'],
                                      cocktail['steps'])
        return False

    def prepare_cocktail(self, cocktail: str):
        known_cocktail = self.__knows_cocktail(cocktail)
        if isinstance(known_cocktail, CocktailRecipe):
            self.__busy = True
            print(f'{self.name} is preparing the {cocktail} cocktail...')
            print(known_cocktail.steps)
            time.sleep(5)
            print(known_cocktail)
            self.__busy = False
        else:
            print(f'{self.name} has no clue on how to prepare {cocktail} cocktail')

    def __str__(self):
        return f'Cocktail Waiter: {self.name} >>> Known cocktails: {", ".join(self.known_cocktails)}'


class WaiterAgency:
    def __init__(self):
        self.__waiters = []
        self.__load__waiters()

    def __add_waiter(self, waiter: Waiter):
        self.__waiters.append(waiter)

    def __load__waiters(self):
        try:
            file = open('c:\\git\\curso_python\\available_waiters.txt', 'rt')
            data = file.readlines()
            for line in data:
                name, age, xp, known_cocktails = line.strip('\n').split(':')
                if known_cocktails is None or len(known_cocktails) == 0:
                    self.__add_waiter(Waiter(name, age, xp))
                else:
                    self.__add_waiter(CocktailWaiter(name, age, xp, known_cocktails.split(',')))
                print(self.__waiters[-1])

            file.close()
        except:
            print('Problems loading the waiter list')

    def find_waiter(self, cocktail_list=None):
        if cocktail_list is None:
            return self.__waiters[0]

        for waiter in self.__waiters:
            known_cocktails = waiter.known_cocktails
            if known_cocktails is not None and set(cocktail_list).issubset(set(known_cocktails)):
                return waiter
        return None


class Tabern(Bar):
    def hire_waiter(self, cocktail_list=None):
        top_talent_agency = WaiterAgency()
        talent = top_talent_agency.find_waiter(cocktail_list)
        if talent is not None:
            print('New hire!', talent)
            super().hire_waiter(talent)
        else:
            print('No hire this time')

    def help_customer(self, waiter_name, cocktail_name=None):
        if cocktail_name is None:
            super().help_customer(waiter_name)
        else:
            available_waiters = list(filter(lambda waiter: waiter.name == waiter_name, self.staff))
            if available_waiters is not None:
                available_waiters[0].prepare_cocktail(cocktail_name)
            else:
                available_waiters = [waiter for waiter in self.staff
                                     if isinstance(waiter, CocktailWaiter)
                                     and cocktail_name in waiter.known_cocktails]
                if available_waiters is not None:
                    available_waiters[0].prepare_cocktail(cocktail_name)



def main():
    """
        # Week 2 Day 1
    """
    # CocktailRecipeBook.get_recipe('zoombie')

    # cm = CocktailWaiter('Steve Jobs', 58, 31, (
    #     CocktailRecipe('Cubalibre',
    #                    ('rum', 'coke', 'lemon juice'),
    #                    ('Drop ice cubes', 'Pour lemon juice', 'Pour rum', 'Fill the rest with coke')),
    # ))
    # cm.prepare_cocktail('cubalibre')
    bar_manolo = Tabern('Manolo\'s Irish Tabern')
    bar_manolo.hire_waiter()
    bar_manolo.help_customer('CocktailWaiter1', 'cubalibre')
