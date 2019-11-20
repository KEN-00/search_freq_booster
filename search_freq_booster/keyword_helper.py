import os

def list_keywords(keywords):
    if len(keywords) > 0:
        print("List of search keywords: ")
        for keyword in keywords:
            keyword_display = str("- {}").format(keyword)
            print(keyword_display)


def get_keywords_from_txt():
    while True:
        file_path = input("Input file path for keyowrd txt file (input 'N' for manual input): ")
        if (file_path is not None) and (os.path.exists(file_path)):
            break

        elif not file_path:
            while True:
                user_prompt = input("Switch to manual input? (Y/N): ")
                if user_prompt == "Y": 
                    return get_keywords()
                elif user_prompt == "N":
                    break
        elif file_path == "N":
            return get_keywords()
            
        elif not os.path.exists(file_path):
            print("File not found. Check the file path and try again.")

    keywords = []
    with open(file_path, 'r') as keyword_file:
        keywords = keyword_file.readlines(0)

    keywords = [keyword.strip() for keyword in keywords]
    list_keywords(keywords)
    return keywords


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