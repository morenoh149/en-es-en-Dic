import json
import xml.etree.ElementTree as ET

# read file
tree = ET.parse('./src/main/resources/dic/es-en.xml')
root = tree.getroot()

result = []
wordlist = root[0]
for word in wordlist:
  result.append({
    "prompt": word[0].text,
    "answer": word[1].text
  })
with open('spanish.json', 'w') as outfile:
  json.dump(result, outfile)
