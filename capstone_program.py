import random
import time

# Constants
NUM_BUSHES = 5
NUM_BUGS = 3
MAX_ATTEMPTS = 5

# This function prints the intro story of the game
def intro():
    print("🐞 Welcome to Learning to Code: The Bug Hunt!")
    print("In this game, you're a brave coder on a mission to catch coding bugs in the wild.")
    print("But be careful! Not everything is what it seems...")
    input("🎮 Press Enter to begin!")

# This function asks the player for their name
def get_player_name():
    name = input("\nWhat's your name, brave bug hunter? ")
    print(f"Nice to meet you, {name}! Let the hunt begin!\n")
    return name

# This function simulates a short search animation
def search_animation():
    print("🔎 Searching", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print()

# This function contains the main game logic
def play_game(name):
    bugs_caught = 0
    attempts = MAX_ATTEMPTS
    bug_positions = random.sample(range(1, NUM_BUSHES + 1), NUM_BUGS)
    bushes_searched = [] # List to store searched bushes
    print(f"There are {NUM_BUSHES} bushes. Some have bugs🐛, some are empty🍃, and some have traps🪤!")
    print(f"You have {MAX_ATTEMPTS} chances to pick a bush (1-{NUM_BUSHES}). Try to catch all {NUM_BUGS} bugs!")

    # Loop until player runs out of attempts or catches all bugs
    while attempts > 0 and bugs_caught < NUM_BUGS:
        try:
            choice = int(input(f"\n👉 Pick a bush to search (1-{NUM_BUSHES}): "))
        except ValueError:
            print("❌ That's not a valid number! Try again.")
            continue

        if choice < 1 or choice > NUM_BUSHES:
            print(f"⚠️ Please choose a number between 1 and {NUM_BUSHES}.")
            continue

        if choice in bushes_searched:
            print("🔄 You've already searched that bush! Try a different one.")
            continue # Skip the rest of the loop, ask for input again

        bushes_searched.append(choice)

        search_animation()

        if choice in bug_positions:
            print("🎉 You found a bug! +1 point!")
            bugs_caught += 1
            bug_positions.remove(choice)
            attempts -= 1 # You used one attempt to find the bug
        else:
            if random.random() < 0.3:
                print("😱 Oh no! You fell into a trap! You lose an extra attempt!")
                attempts -= 2  # Extra penalty
            else:
                print("😐 Just leaves... no bugs here.")
                attempts -= 1 # You used one attempt and found nothing
            if attempts < 0:
                attempts = 0

        print(f"🔁 Attempts remaining: {attempts}")
        print(f"✅ Bugs caught so far: {bugs_caught}\n")

    # Game Over — Results
    print("Hunt Complete!")
    if bugs_caught == NUM_BUGS:
        print(f"\n🏆 Amazing, {name}! You caught all the bugs and fixed our code!")
    elif bugs_caught > 0:
        print(f"\n👍 Not bad, {name}! You caught {bugs_caught} bug(s). Better luck next time!")
    else:
        print(f"\n😢 No bugs today, {name}... But every coder has their off days!")

# Main function that controls the game loop
def main():
    intro()
    name = get_player_name()
    while True:
        play_game(name)
        replay = input("\n🔁 Would you like to play again? (y/n): ").strip().lower()
        if replay not in ['y', 'yes']:
            print("\n👋 Thanks for playing Bug Hunt! Keep coding, and keep hunting those bugs!")
            break
        else:
            print("\n🔄 Restarting the game...\n")

# Start the program
if __name__ == "__main__":
    main()