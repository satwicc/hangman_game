import random


hangman_words = [
    "apple", "banana", "cherry", "date", "elder", "fig", "grape", "hazel", "ivy", "juniper",
    "kiwi", "lemon", "mango", "nectar", "olive", "peach", "quince", "raspberry", "straw", "tamarind",
    "umbrella", "vanilla", "watermelon", "xigua", "yam", "zucchini", "amber", "azure", "beige", "black",
    "blue", "bronze", "brown", "burgundy", "crimson", "cyan", "gold", "gray", "green", "indigo",
    "ivory", "lavender", "lime", "magenta", "maroon", "navy", "olive", "orange", "pink", "purple",
    "red", "rose", "salmon", "scarlet", "silver", "tan", "teal", "turquoise", "violet", "white",
    "yellow", "ant", "bat", "bear", "bee", "beetle", "buffalo", "camel", "cat", "cheetah",
    "chicken", "cow", "coyote", "crab", "crow", "deer", "dog", "dolphin", "donkey", "duck",
    "eagle", "elephant", "falcon", "ferret", "fish", "flamingo", "fox", "frog", "giraffe", "goat",
    "goose", "gorilla", "hamster", "hare", "hawk", "hippo", "horse", "hyena", "jackal", "jaguar",
    "kangaroo", "koala", "leopard", "lion", "lizard", "llama", "lobster", "lynx", "mole", "monkey",
    "moose", "mouse", "mule", "newt", "octopus", "ostrich", "otter", "owl", "ox", "panda",
    "parrot", "peacock", "pelican", "penguin", "pig", "pigeon", "porcupine", "quail", "rabbit", "raccoon",
    "rat", "raven", "reindeer", "rhino", "rooster", "salmon", "seal", "shark", "sheep", "shrimp",
    "skunk", "sloth", "snail", "snake", "sparrow", "spider", "squid", "squirrel", "swan", "tiger",
    "toad", "turkey", "turtle", "vulture", "walrus", "wasp", "weasel", "whale", "wolf", "wombat",
    "woodpecker", "yak", "zebra", "actor", "artist", "baker", "banker", "barber", "builder", "butcher",
    "carpenter", "chef", "clerk", "dentist", "doctor", "driver", "engineer", "farmer", "fireman", "fisherman",
    "gardener", "guide", "janitor", "judge", "lawyer", "librarian", "mechanic", "miner", "nurse", "painter",
    "pharmacist", "photographer", "pilot", "plumber", "police", "porter", "receptionist", "scientist", "soldier", "surgeon",
    "tailor", "teacher", "technician", "translator", "vet", "waiter", "waitress", "writer", "zoologist", "acorn",
    "balloon", "beacon", "beach", "blizzard", "boulder", "breeze", "cabin", "cactus", "canyon", "cave",
    "cavern", "cliff", "cloud", "coast", "coral", "crater", "creek", "desert", "dune", "earthquake",
    "fog", "forest", "frost", "geyser", "glacier", "grove", "hill", "horizon", "iceberg", "island",
    "jungle", "lagoon", "lake", "lava", "meadow", "meteor", "mine", "mist", "moon", "mountain",
    "oasis", "ocean", "peak", "plain", "plateau", "pond", "quarry", "rain", "rainbow", "reef",
    "river", "rock", "sand", "savanna", "sea", "snow", "storm", "sun", "swamp", "tide",
    "tsunami", "valley", "volcano", "waterfall", "wave", "wind", "wood", "aurora", "cloudburst", "delta",
    "dust", "eclipse", "foggy", "galaxy", "hail", "hurricane", "lightning", "mirage", "nimbus", "northern",
    "puddle", "smog", "solstice", "star", "sunlight", "tempest", "thunder", "twister", "typhoon", "vapor"
]


def lives_subtractor(life):
    global lives
    lives = life-1
    print (f"nawrrr... it isn't there :/\nyou've {lives} lives left\n\n")


def hangman_hanging_part():
    guess=input("\nwhat's the guess gonna be???\n").lower()
    if guess in guessed_list:
            print(f"you've already guessed {guess} bestie\ntry again ദ്ദി (• ᴗ -)✧\n")
            return

    else:
        guessed_list.append(guess)

        print(f"\nyou guessed {guess}\n")
        found = False
        for i in range(len(random_word)):
            if random_word[i] == guess:
                length_word[i] = guess
                print (f"and {guess} is correct!!! lessgooo\n")
                print (length_word)
                found = True
    
        if not found:
            lives_subtractor(lives)
            print(length_word)


random_word =random.choice(hangman_words)
length_word = ['_'] * len(random_word)
guessed_list = []
# print(random_word)
lives = 7


while '_' in length_word and lives > 0:
    hangman_hanging_part()

if '_' not in length_word:
    print("\n🎉 ayyyyy, you guessed the word! you win a cookie! (buy urself one, im broke)\n")
else:
    print(f"\n💀 out of lives, sucks to suck!\n\nThe word was: \n{random_word}\n")
