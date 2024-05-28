import re
def get_month_and_year(url):
    # Define the regex pattern
    pattern = r"https:\/\/peerlist\.io\/projects\/(\d{4})\/month\/([A-Za-z]+)"

    # Use re.search to find the match
    match = re.search(pattern, url)

    if match:
        year = match.group(1)
        month = match.group(2)
        print(f"Year: {year}, Month: {month}")
    else:
        print("No match found")


    return year, month
