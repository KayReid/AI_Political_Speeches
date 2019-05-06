import os
outclinton = open("text/clinton.txt", "w+")
outtrump = open("text/trump.txt", "w+")
delete_list = ["hillary", "clinton", "donald", "trump", "mike",
               "pence", "bill", "chelsea", "barack", "obama", "joe",
               "biden", "michelle", "bernie", "sanders", "ted", "cruz",
               "gary", "johnson", "jill", "stein", "lincoln", "chafee",
               "lawrence", "lessig", "martin", "o'malley", "webb", "jeb",
               "bush", "ben", "carson", "chris", "christie", "carly",
               "fiorina", "jim" , "gilmore", "lindsey", "graham", "mike",
               "huckabee", "bobby", "jindal", "john", "kasich", "george",
               "pataki", " rand ", "paul", "rick", "perry", "santorum",
               "marco", "rubio", "scott", "walker", "andrew", "cuomo",
               " al ", "gore", "dennis", "kucinich", "brian", "schweitzer",
               "elizabeth", "warren", "kelly", "ayotte", "nikki", "haley",
               "peter", "king", "susana", "martinez", "mitt", "romney",
               "anthony", "weiner", "huma", "abedin", "ryan", "brian",
               "sandoval", "corey", "lewandowski", "manafort", "ivanka",
               "tiffany", "barron", "melania", "eric", "steve", "bannon",
               "kellyanne", "conway", "jeff", "sessions", "david", "bossie",
               "michael", "glassner", "jason", "miller", "katrina", "pierson",
               "jason", "miller", "katrina", "pierson", "hope", "hicks",
               "daniel", "scavino", "jr.", "jr", "flynn", "omarosa", "manigault",
               "rudy", "giuliani", "palatucci", "cohen", "arthur", "culvahouse",
               "brad", "parscale", "sam", "nunberg", "gates", "caputo",
               "vladimir", "putin", "democratic", "republican", "democrat",
               "<audience", "<crowd", "<title", "<title=", "<question:", "<unknown:",
               "<date:", "republican", "tim", "kaine", "hillary!", "(applause)",
               "<applause>", "(inaudible)", "<booing>", "<ph>", "<:>", "<:", ">",
               "(laughter)", "(ph)", ":", "<unidentified female", "<unidentified male",
               ",", ".","!","\"", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
line_list = ["<audience", "<crowd", "<title", "<date", "<question"]

for f in os.listdir("text/clinton"):
    infile = open("text/clinton/"+f)
    for line in infile:
        a = line.lower()
        for word in delete_list:
            a = a.replace(word, "")
        #for word in line_list:
         #   if (line.find(word)):
          #      a = ""
        outclinton.write(a)
    infile.close()
outclinton.close()

for f in os.listdir("text/trump"):
    infile = open("text/trump/"+f)
    for line in infile:
        a = line.lower()
        for word in delete_list:
            a = a.replace(word, "")
        # for word in line_list:
           # if (line.find(word)):
                #a = ""
        outtrump.write(a)
    infile.close()
outtrump.close()
