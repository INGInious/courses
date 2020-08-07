# A script to easily modify a course
import json
import sys
import codecs

# ISO-639 languages
iso639 = ['ab', 'aa', 'af', 'ak', 'sq', 'am', 'ar', 'an', 'hy', 'as', 'av', 'ae', 'ay', 'az', 'bm', 'ba', 'eu', 'be', 'bn', 'bh', 'bi', 'bs', 'br', 'bg', 'my', 'ca', 'ch', 'ce', 'ny', 'zh', 'cv', 'kw', 'co', 'cr', 'hr', 'cs', 'da', 'dv', 'nl', 'dz', 'en', 'eo', 'et', 'ee', 'fo', 'fj', 'fi', 'fr', 'ff', 'gl', 'ka', 'de', 'el', 'gn', 'gu', 'ht', 'ha', 'he', 'hz', 'hi', 'ho', 'hu', 'ia', 'id', 'ie', 'ga', 'ig', 'ik', 'io', 'is', 'it', 'iu', 'ja', 'jv', 'kl', 'kn', 'kr', 'ks', 'kk', 'km', 'ki', 'rw', 'ky', 'kv', 'kg', 'ko', 'ku', 'kj', 'la', 'lb', 'lg', 'li', 'ln', 'lo', 'lt', 'lu', 'lv', 'gv', 'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mh', 'mn', 'na', 'nv', 'nb', 'nd', 'ne', 'ng', 'nn', 'no', 'ii', 'nr', 'oc', 'oj', 'cu', 'om', 'or', 'os', 'pa', 'pi', 'fa', 'pl', 'ps', 'pt', 'qu', 'rm', 'rn', 'ro', 'ru', 'sa', 'sc', 'sd', 'se', 'sm', 'sg', 'sr', 'gd', 'sn', 'si', 'sk', 'sl', 'so', 'st', 'es', 'su', 'sw', 'ss', 'sv', 'ta', 'te', 'tg', 'th', 'ti', 'bo', 'tk', 'tl', 'tn', 'to', 'tr', 'ts', 'tt', 'tw', 'ty', 'ug', 'uk', 'ur', 'uz', 've', 'vi', 'vo', 'wa', 'cy', 'wo', 'fy', 'xh', 'yi', 'yo', 'za', 'zu']

# Read the market place file
with open("docs/marketplace.json", "r") as f:
    marketplace = json.load(f)

""" Create new course """

# Get course
courseid = input("Type the id of the course you want to modify: ")
all_id = [course["id"] for course in marketplace]
course = {}
while courseid not in all_id:
    courseid = input("Please type a valid id: ")
for mcourse in marketplace:
    if mcourse["id"] == courseid:
        course = mcourse

# Remove course
if input("Do you want to remove this course ? Yes[Y] or No[N]: ") in ["Yes", "yes", "Y", "y"]:
    with codecs.open("docs/marketplace.json", "w", "utf-8") as f:
        content = json.dumps([course for course in marketplace if not (course['id'] == courseid)], sort_keys=False, indent=4, separators=(',', ': '))
        f.write(content)
    sys.exit()


# Edit courseid
if input("Do you want to edit the id ? Yes[Y] or No[N]: ") in ["Yes", "yes", "Y", "y"]:
    course = {"id": input("Type the course id: ")}
    all_id = [course["id"] for course in marketplace]
    while not course["id"] or course["id"] in all_id:
        if not course["id"]:
            course["id"] = input("Please type an id: ")
        else:
            course["id"] = input("This id already exist. Type a new course id: ")

# Edit courseid
if input("Do you want to edit the link ? Yes[Y] or No[N]: ") in ["Yes", "yes", "Y", "y"]:
    course["link"] = input("Type the link to the repo: ")
    while not course["link"]:
        course["link"] = input("Please type a link: ")

# Edit language
if input("Do you want to edit the language ? Yes[Y] or No[N]: ") in ["Yes", "yes", "Y", "y"]:
    course["languages"] = input("Type the language(s) of this course: ")

# Edit license
if input("Do you want to edit the license ? Yes[Y] or No[N]: ") in ["Yes", "yes", "Y", "y"]:
    course["license"] = input("Type the license for this course: ")

# Edit maintainer
if input("Do you want to edit the maintainer(s) ? Yes[Y] or No[N]: ") in ["Yes", "yes", "Y", "y"]:
    course["maintainers"] = input("Type the maintainer(s) for this course: ")

# Edit author
if input("Do you want to edit the author(s) ? Yes[Y] or No[N]: ") in ["Yes", "yes", "Y", "y"]:
    course["authors"] = input("Type the author(s) for this course: ")

# Edit default language
if input("Do you want to edit the default language ? Yes[Y] or No[N]: ") in ["Yes", "yes", "Y", "y"]:
    default_language = input("Type the default language (in ISO639-1 format): ")
    while default_language not in iso639:
        default_language = input("Not a valid ISO639-1 language: ")
    course["default_language"] = default_language
else:
    default_language = course["default_language"]

# Edit course name
if default_language not in course["name"]:
    name = input("Type the name in " + default_language + ": ")
    while not name:
        name = input("Please type a name: ")
    course["name"][default_language] = name

while input("Do you want to edit one of the name ? Yes[Y] or No[N]: ") in ["Yes", "yes", "Y", "y"]:
    language = input("What language do you want to edit (" + str(list(course["name"].keys())) + ")")
    if language in course["name"].keys():
        name = input("Type the name in " + language + ": ")
        while not name:
            name = input("Please type a name: ")
        course["name"][language] = name
    else:
        print("Invalid language")

while input("Do you want to add translation ? Yes[Y] or No[N]: ") in ["Yes", "yes", "Y", "y"]:
    language = input("Type the language of the translation (in ISO639-1 format): ")
    while language not in iso639:
        language = input("Not a valid ISO639-1 language: ")
    name = input("Type the name in " + language + ": ")
    while not name:
        name = input("Please type a name: ")
    course["name"][language] = name

# Edit course short desc
if default_language not in course["short_desc"]:
    short_desc = input("Type the short description in " + default_language + ": ")
    while not short_desc:
        short_desc = input("Please type a description: ")
    course["short_desc"][default_language] = short_desc

while input("Do you want to edit one of the short description ? Yes[Y] or No[N]: ") in ["Yes", "yes", "Y", "y"]:
    language = input("What language do you want to edit (" + str(list(course["short_desc"].keys())) + ")")
    if language in course["short_desc"].keys():
        short_desc = input("Type the short description in " + language + ": ")
        while not short_desc:
            short_desc = input("Please type a short description: ")
        course["short_desc"][language] = short_desc
    else:
        print("Invalid language")

while input("Do you want to add translation ? Yes[Y] or No[N]: ")  in ["Yes", "yes", "Y", "y"]:
    language = input("Type the language of the translation (in ISO639-1 format): ")
    while language not in iso639:
        language = input("Not a valid ISO639-1 language: ")
    short_desc = input("Type the short description in " + language + ": ")
    while not short_desc:
        short_desc = input("Please type a description: ")
    course["short_desc"][language] = short_desc

# Edit course description
if default_language not in course["description"]:
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
    course["description"][default_language] = description

while input("Do you want to edit one of the description ? Yes[Y] or No[N]: ") in ["Yes", "yes", "Y", "y"]:
    language = input("What language do you want to edit (" + str(list(course["description"].keys())) + ")")
    if language in course["description"].keys():
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
    else:
        print("Invalid language")

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

if input("Do you want to validate your change ? Yes[Y] or No[N]: ") in ["Yes", "yes", "Y", "y"]:
    with codecs.open("docs/marketplace.json", "w", "utf-8") as f:
        content = json.dumps(marketplace, sort_keys=False, indent=4, separators=(',', ': '))
        f.write(content)
else:
    if input("This will lose what you typed! Are you sure ? Yes[Y] or No[N]: ") not in ["Yes", "yes", "Y", "y"]:
        with codecs.open("docs/marketplace.json", "w", "utf-8") as f:
            content = json.dumps(marketplace, sort_keys=False, indent=4, separators=(',', ': '))
            f.write(content)
