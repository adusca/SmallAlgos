from linkedlist import LinkedList


class Animal:

    def __init__(self, species):
        self.species = species


class AnimalShelter:

    def __init__(self):
        self.dogs = LinkedList()
        self.cats = LinkedList()
        self.counter = 0

    def enqueue(self, animal):
        if animal.species == 'dog':
            self.dogs.add((animal, self.counter))
        elif animal.species == 'cat':
            self.cats.add((animal, self.counter))
        else:
            raise Exception("Unsupported animal type.")
        self.counter += 1

    def dequeue_dog(self):
        return self.dogs.pop()

    def dequeue_cat(self):
        return self.cat.pop()

    def dequeue_any(self):
        dog = self.dogs.head
        cat = self.cats.head
        if dog is None:
            return cat
        if cat is None:
            return dog

        if dog.value[1] > cat.value[1]:
            return cat
        else:
            return dog
