# A script to easily add new course
import json
import codecs

# ISO-639 languages
iso639 = ['ab', 'aa', 'af', 'ak', 'sq', 'am', 'ar', 'an', 'hy', 'as', 'av', 'ae', 'ay', 'az', 'bm', 'ba', 'eu', 'be', 'bn', 'bh', 'bi', 'bs', 'br', 'bg', 'my', 'ca', 'ch', 'ce', 'ny', 'zh', 'cv', 'kw', 'co', 'cr', 'hr', 'cs', 'da', 'dv', 'nl', 'dz', 'en', 'eo', 'et', 'ee', 'fo', 'fj', 'fi', 'fr', 'ff', 'gl', 'ka', 'de', 'el', 'gn', 'gu', 'ht', 'ha', 'he', 'hz', 'hi', 'ho', 'hu', 'ia', 'id', 'ie', 'ga', 'ig', 'ik', 'io', 'is', 'it', 'iu', 'ja', 'jv', 'kl', 'kn', 'kr', 'ks', 'kk', 'km', 'ki', 'rw', 'ky', 'kv', 'kg', 'ko', 'ku', 'kj', 'la', 'lb', 'lg', 'li', 'ln', 'lo', 'lt', 'lu', 'lv', 'gv', 'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mh', 'mn', 'na', 'nv', 'nb', 'nd', 'ne', 'ng', 'nn', 'no', 'ii', 'nr', 'oc', 'oj', 'cu', 'om', 'or', 'os', 'pa', 'pi', 'fa', 'pl', 'ps', 'pt', 'qu', 'rm', 'rn', 'ro', 'ru', 'sa', 'sc', 'sd', 'se', 'sm', 'sg', 'sr', 'gd', 'sn', 'si', 'sk', 'sl', 'so', 'st', 'es', 'su', 'sw', 'ss', 'sv', 'ta', 'te', 'tg', 'th', 'ti', 'bo', 'tk', 'tl', 'tn', 'to', 'tr', 'ts', 'tt', 'tw', 'ty', 'ug', 'uk', 'ur', 'uz', 've', 'vi', 'vo', 'wa', 'cy', 'wo', 'fy', 'xh', 'yi', 'yo', 'za', 'zu']

# Read the market place file
with open("Github-Pages/marketplace.json", "r") as f:
    marketplace = json.load(f)

""" Create new course """

# Get courseid
course = {"id": input("Type the course id: ")}
all_id = [course["id"] for course in marketplace]
while not course["id"] or course["id"] in all_id:
    if not course["id"]:
        course["id"] = input("Please type an id: ")
    else:
        course["id"] = input("This id already exist. Type a new course id: ")

# Get link
course["link"] = input("Type the link to the repo: ")
while not course["link"]:
    course["link"] = input("Please type a link: ")

# Get language
course["languages"] = input("Type the language(s) of this course: ")

# Get license
course["license"] = input("Type the license for this course: ")

# Get maintainer
course["maintainers"] = input("Type the maintainer(s) for this course: ")

# Get author
course["authors"] = input("Type the author(s) for this course: ")

# Get default language
default_language = input("Type the default language (in ISO639-1 format): ")
while default_language not in iso639:
    default_language = input("Not a valid ISO639-1 language: ")
course["default_language"] = default_language

# Get course name
name = input("Type the name in " + default_language + ": ")
while not name:
    name = input("Please type a name: ")
course["name"] = {default_language: name}

while input("Do you want to add translation ? Yes[Y] or No[N]: ") in ["Yes", "yes", "Y", "y"]:
    language = input("Type the language of the translation (in ISO639-1 format): ")
    while language not in iso639:
        language = input("Not a valid ISO639-1 language: ")
    name = input("Type the name in " + language + ": ")
    while not name:
        name = input("Please type a name: ")
    course["name"][language] = name

# Get course short desc
short_desc = input("Type the short description in " + default_language + ": ")
while not short_desc:
    short_desc = input("Please type a description: ")
course["short_desc"] = {default_language: short_desc}

while input("Do you want to add translation ? Yes[Y] or No[N]: ")  in ["Yes", "yes", "Y", "y"]:
    language = input("Type the language of the translation (in ISO639-1 format): ")
    while language not in iso639:
        language = input("Not a valid ISO639-1 language: ")
    short_desc = input("Type the short description in " + language + ": ")
    while not short_desc:
        short_desc = input("Please type a description: ")
    course["short_desc"][language] = short_desc

# Get course description
while input("Do you want to add description in " + default_language + " from file? Yes[Y] or No[N]: ") in ["Yes", "yes", "Y", "y"]:
    filepath = input("Please type filepath: ")
    try:
        with open(filepath, 'r') as file:
            description = file.read()
        break
    except EnvironmentError:
        print("Invalid file!")
else:
    description = input("Type the description in " + default_language + ": ")
    while not description:
        description = input("Please type a description: ")
course["description"] = {default_language: description}

while input("Do you want to add translation ? Yes[Y] or No[N]: ") in ["Yes", "yes", "Y", "y"]:
    language = input("Type the language of the translation (in ISO639-1 format): ")
    while language not in iso639:
        language = input("Not a valid ISO639-1 language: ")
    while input("Do you want to add description in " + language + " from file? Yes[Y] or No[N]: ") in ["Yes", "yes", "Y", "y"]:
        filepath = input("Please type filepath: ")
        try:
            with open(filepath, 'r') as file:
                description = file.read()
            break
        except EnvironmentError:
            print("Invalid file!")
    else:
        description = input("Type the description in " + default_language + ": ")
        while not description:
            description = input("Please type a description: ")
    course["description"][language] = description

if input("Do you want to validate your new course ? Yes[Y] or No[N]: ") in ["Yes", "yes", "Y", "y"]:
    marketplace.append(course)
    with codecs.open("Github-Pages/marketplace.json", "w", "utf-8") as f:
        content = json.dumps(marketplace, sort_keys=False, indent=4, separators=(',', ': '))
        f.write(content)
else:
    if input("This will lose what you typed! Are you sure ? Yes[Y] or No[N]: ") not in ["Yes", "yes", "Y", "y"]:
        marketplace.append(course)
        with codecs.open("Github-Pages/marketplace.json", "w", "utf-8") as f:
            content = json.dumps(marketplace, sort_keys=False, indent=4, separators=(',', ': '))
            f.write(content)


if input("Do you want to add the course to the README ? Yes[Y] or No[N]: ") in ["Yes", "yes", "Y", "y"]:
    table = "\n| Name | " + course["name"][default_language] + " |\n"
    table += "| :---- | ------------------------------------- |\n"
    table += "| Link | " + course["link"] + " |\n"
    while not course["languages"]:
        course["languages"] = input("Please type non empty language(s) for the course: ")
    table += "| Language | " + course["languages"] + " |\n"
    table += "| Description | " + course["short_desc"][default_language] + " |\n"
    while not course["license"]:
        course["license"] = input("Please type non empty license for the course: ")
    table += "| License | " + course["license"] + " |\n"
    while not course["maintainers"]:
        course["maintainers"] = input("Please type non empty maintainer(s) for the course: ")
    table += "| Maintainer | " + course["maintainers"] + " |\n"
    while not course["authors"]:
        course["authors"] = input("Please type non empty author(s) for the course: ")
    table += "| Authors | " + course["authors"] + " |\n"

    with open("README.md", "a") as myfile:
        myfile.write(table)
