import re

def extract_markdown_images(text):
    #input is raw md string
    #output should be a tuple (title, link) [("rick roll", "https://imgur.com/blabla")]
    #for images, ![alt text](imglink)
    #regex for this is ((!\[\w+ \w+])\(\w+://\w+.\w+\)) for entire string
    #for !alt text part only: \!\[(.*)]
    alt_text = re.findall(r"\!\[(.*?)]", text) # gives a list of matches [match, match]
    link_text = re.findall(r"\((.*?\:.*?)\)", text) #gives a list of matches [match, match]
    tuples_list=[]
    for i in range(len(alt_text)):
        tuples_list.append((alt_text[i], link_text[i]))
    return tuples_list

# text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
# print(extract_markdown_images(text))

def extract_markdown_links(text):
    link_text = re.findall(r"\[(.*?)]", text)
    link = re.findall(r"\((.*?\:.*?)\)", text)
    tuples_list = []
    for i in range(len(link_text)):
        tuples_list.append((link_text[i], link[i]))
    return tuples_list
