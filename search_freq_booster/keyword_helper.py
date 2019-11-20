def list_keywords(keywords):
    if len(keywords) > 0:
        print("List of search keywords: ")
        for keyword in keywords:
            keyword_display = str("- {}").format(keyword)
            print(keyword_display)


def get_keywords_from_txt():
    


def get_keywords():
    keywords = []
    while True:
        keyword = input("Input keyword (input -1 to stop): ")
        if keyword is None:
            continue
        elif keyword == "-1":
            break
        else:
            keywords.append(keyword)

    list_keywords(keywords)
    
    return keywords