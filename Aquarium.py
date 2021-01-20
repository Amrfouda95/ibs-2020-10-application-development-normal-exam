from Fish import Fish


class Aquarium:
    fishes = []

    def __init__(self):
        self.fishes = []

    def addFish(self, Fish):
        self.fishes.append(Fish)

    def feed(self):
        for fish in self.fishes:
            fish.weight = fish.weight + Fish.feed(fish)

    def removeFish(self):
        for fish in self.fishes:
            if (fish.weight > 11):
                self.fishes.remove(fish)

    def getStatus(self):
        for fish in self.fishes:
            Fish.status(fish)


if __name__ == "__main__":
    AQ = Aquarium()

    # adding new fish
    print("\nAdd new fishs\n")
    AQ.addFish(Fish("Tang", 10, "blue"))
    AQ.addFish(Fish("Clownfish", 4, "red"))
    AQ.addFish(Fish("Kong", 10, "green"))

    # get fish status
    AQ.getStatus()

    # adding the feed
    AQ.feed()

    # get fish status after feeding
    print("\nAfter feeds the fish\n")
    AQ.getStatus()

    # remove the big fish atleast 11 wtg
    AQ.removeFish()
    print("\nAfter remove Big Fish\n")
    AQ.getStatus()