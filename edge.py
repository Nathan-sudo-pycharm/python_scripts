# Here we will make a program to search some random things on bing, with one click.
# We are importing all the Modules we need to make this work
import webbrowser, time, pyautogui, random, requests, time


# Start of our Search Function
def searchAuto():
    '''This is a function to perform random search queries in Microsoft Bing in order to hi
    hi
    earn the Daily Search Points! It works!'''

    # Sending a HTTP request to get a big list of random words
    response = requests.get(
        'https://www.mit.edu/~ecprice/wordlist.10000',
        timeout=5
    )
    # Here we are decoding the response and storing it in a variable for further use
    randomWords = response.content.decode('utf-8')
    # Getting a list of all the words without spaces basically
    words = randomWords.splitlines()
    # Choosing a random word from the list every time
    random_word = random.choice(words)
    # Forming the URL to search in Bing with the random word
    url = ("https://www.bing.com/search?q=" + random_word)
    # Using the Web Browser Module, performing the searches
    webbrowser.open(url)
    # After the set amount of time, the next line will be executed, and browser window will be closed. You can the number as you like.
    # Making a change and adding a new feature suggested by a friend. Now it will perform searches at random intervals between set value.
    # It is not necessary but might be useful to avoid getting banned? Not sure, seemed like fun so here it is.
    randomVal = random.randint(3, 12)
    # It will return a random number every time, between 3 and 12, and it will be read as seconds to wait before doing next search
    time.sleep(randomVal)
    # Finally, once the search is done and Points have been credited, we will close the browser window with this next line
    pyautogui.hotkey("ctrl", "w")


# End of our Search Function

# Starting to capture the time
st = time.time()
# Finally calling the function to run x number of times to collect the daily points.
# We just change the value of range to perform that many searches! If you want to make 30 searches, just change the range to 30. Boom done!
# Note we use '_' character instead of 'i' when we dont care about the value for 'i'
# Adding an input prompt to set the number of searches before running the program
num = int(input("How many searches you want to perform? : "))
for i in range(num):
    searchAuto()
    # This will indicate how many searches done, in the Terminal for reference.
    print("Search number :", i, "done!")

# Stopping time capture to show how long it took to perform all the searches
ed = time.time()

# Showing the time after calculation on terminal
print(f"That took {round(ed - st)} seconds ")

# Just a line of command to see the DocString for the search() function we created.
# print(searchAuto.__doc__)



