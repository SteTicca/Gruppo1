import re

# file = open("Salvini_Luglio.csv", "rb")
#
# tweets = []
#
# for i in file.readlines():
#     tweet =i.split(",")
#     tweets.append(tweet)
#
# print(tweets)


filein = open("Salvini_Luglio.csv", "rb")

fileout = open("Salvini_Luglio.txt", "w")

id = re.compile("^[0-9]{19}")


for i in filein.readlines():
    if id.match(i.split(',')[0]) == None:
        fileout.writelines(i.split(',')[0:])
    else: fileout.writelines(i.split(',')[2:])