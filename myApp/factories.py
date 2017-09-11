import factory

from .models import Person, Group

class GroupFactory(factory.Factory):
	FACTORY_FOR = Group
	name = 'Developers'


class PersonFactory(factory.Factory):
	FACTORY_FOR = Person

	first_name = 'Christiam'
	last_name = 'Ndoradoumngue'
	group = factory.SubFactory(GroupFactory)
