import webbrowser
import requests
from bs4 import BeautifulSoup


def searchGoogle(searchTerm):
    r = requests.get(f"https://www.google.com/search?q={searchTerm}")
    return r


def parseHTML(request):
    return BeautifulSoup(request, "html.parser")


def openResult(results):
    valid = False
    resToOpen = 0
    while not valid:
        resToOpen = input("Result to open: ")
        if resToOpen.isdigit():
            valid = True
            resToOpen = int(resToOpen)

        if resToOpen > len(results) - 1:
            print("Must be in the range of search results")
            valid = False
        else:
            valid = True

    else:
        print("Not a valid number")

    webbrowser.open_new_tab(results[int(resToOpen)])


def main():
    searchTerm = str(input("What do you want to search: "))
    search = searchGoogle(searchTerm)
    parsed = parseHTML(search.content)

    results = []

    # looks for all <a> tags
    for link in parsed.find_all("a"):
        # this filters it down to search results
        if str(link.get("href")).startswith("/url?q="):
            # removes more un neccesary google search html things, leaves just the result url
            result, sep, tail = str(link.get('href').replace("/url?q=", '')).partition("&sa=")
            results.append(result)

    # #remove the default google results, such as the support page or the maps search ect...
    # results.pop(0)
    # results.pop(0)
    # results.pop(len(results) - 1)
    # results.pop(len(results) - 1)

    for res in range(len(results)):
        print(f"{res}: {results[res]}", end="\n\n")

    openResult(results)


if __name__ == "__main__":
    main()
