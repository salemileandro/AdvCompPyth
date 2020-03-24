

def test1():
    import animals
    m = animals.Mammals()
    m.printMembers()

    b = animals.Birds()
    b.printMembers()


def test2():
    import animals
    harmless_birds = animals.harmless.Birds()
    harmless_birds.printMembers()

    dangerous_fish = animals.dangerous.Fish()
    dangerous_fish.printMembers()


if __name__ == "__main__":
    print("Running the first test with the import animals:")
    test1()

    print("Running the first test with the import animals.harmeless (etc):")
    test2()

