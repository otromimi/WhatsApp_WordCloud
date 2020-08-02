#!/usr/bin/python3
import sys
import wordcloud
import re


words_to_omitte = ('i', 'you', 'so', 'and', 'can', 'a', 'didn', 'did', 'ha', 'don')
word_min_len = 4
txt_filename = sys.argv[1]
text = ""

# MM/DD/YY, HH:MM - <Name>:
pattern1 = r"\d{1,2}/\d{1,2}/\d{2}, \d{2}:\d{2} - .{1,}?: "

# <Media omitted>
pattern2 = r"<Media omitted>\n"

# http || https ULRs
pattern3 = r"[https://,http://].{,}?\n"



with open(txt_filename, 'r') as f:
	text = f.read()
	

# Deleting message stamps
text = re.sub(pattern1, " ", text)
# Deleting media comments
text = re.sub(pattern2, " ", text)
# Deleting links
text = re.sub(pattern3, " ", text)
# Deleting simbols and emojis
text = re.sub(r"\W", " ", text)
# Deleting new lines
text = re.sub(r"\n", " ", text)
# Deleting useless spaces
text = re.sub(r"\s{2,}", " ", text)


text = text.lower()
text = text.split()
frequencies_dic = {}

print('Words after text trim: {}'.format(len(text)))

for word in text:
	if word not in words_to_omitte:
		if len(word) >= word_min_len:
			if word in frequencies_dic:
				frequencies_dic[word] += 1
			else:
				frequencies_dic[word] = 1


cloud = wordcloud.WordCloud()
cloud.generate_from_frequencies(frequencies_dic)
cloud.to_file("word_cloud.jpg")

