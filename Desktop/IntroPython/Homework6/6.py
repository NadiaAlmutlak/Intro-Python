# ## Question 1: Arabic Chat Transliteration
#
#
# __Overview__
#
# "The Arabic chat alphabet, also known as Arabish, Araby (Arabic: عربي‎, Arabī), Arabizi (عربيزي, Arabīzī), Mu'arrab (معرب), and Franco-Arabic, is an alphabet used to communicate in Arabic over the Internet or for sending messages via cellular phones. It is a character encoding of Arabic to the Latin script and the Arabic numerals. It differs from more formal and academic Arabic transliteration systems, as it avoids diacritics by freely using digits and multigraphs for letters that do not exist in the basic Latin script."<br>
# https://en.wikipedia.org/wiki/Arabic_chat_alphabet

# A code cell below  labelled __Character Sets__ creates two lists. ```arabic_letters``` is a subset of the Arabic letters. ```arabic_chat``` is the corresponding representation in Arabish. Note that some Arabic letters map to __two__ Latin letters/characters. This is called a diagraph("https://en.wikipedia.org/wiki/Digraph_(orthography)" -- "a combination of two letters representing one sound, as in ph and ey."
#
# For example,

# In[34]:


print(arabic_letters[16], "maps to", arabic_chat[16])
print("The mapping is to \"6'\" or 6 followed by a single quote.")

# In[35]:


print("and", arabic_chat[3], "maps to", arabic_letters[3], "while", arabic_chat[2], 'maps to', arabic_letters[2])

# You must implement a function ```my_transliterate(w, source, target, diagraph)```
# - Parameters
#     - ```w``` is a string of characters.
#     - ```source``` is the source character set for transliteration.
#     - ```target``` is the target character set for transliteration
#     - ```diagraph``` is an optional parameter, and is true if the source character set has entries with two characters, e.g. 'sh' or 'th'
# - The function returns the transliterated string.
#
# <u>Note:</u> Diagraph processing takes precedence. For example, this means that 'sh' always map ش and never to the individual character mappings for 's' and 'h' (س,ه).

# __Character Sets__

# * I edited the arabic letters to add the letters of my name :)

# In[33]:


arabic_letters = ['ا',
                  'ب',
                  'ت',
                  'ث',
                  'ج',
                  'ح',
                  'خ',
                  'د',
                  'ذ',
                  'ر',
                  'ز',
                  'س',
                  'ش',
                  'ص',
                  'ض',
                  'ط',
                  'ظ',
                  'ع',
                  'غ',
                  'ف',
                  'ق',
                  'ك',
                  'ل',
                  'م',
                  'ن',
                  'ه',
                  'ة',
                  'ي',
                  'و']

arabic_chat = ['a',
               'b',
               't',
               'th',
               'dj',
               '7',
               'kh',
               'd',
               'z',
               'r',
               'z',
               's',
               'sh',
               's',
               'dh',
               '6',
               "6'",
               '3',
               'gh',
               'f',
               'q',
               'k',
               'l',
               'm',
               'n',
               'h',
               'at',
               'i',
               'w']

print("Arabic Letters = ", arabic_letters)
print("Arabic Chat = ", arabic_chat)


# __Your Implementation__

# In[5]:


def my_transliterate(w, source, target, digraph=False):
    done = False
    result = []
    i = 0
    w = w.lower()

    while i < len(w):
        next_1 = None

        if digraph:
            c2 = w[i:i + 2]
            try:
                pos = source.index(c2)
                next_1 = target[pos]
                i += 2
            except ValueError as ie:
                next_1 = None

        if next_1 is None:
            c1 = w[i]
            try:
                pos = source.index(c1)
                next_1 = target[pos]
                i += 1
            except ValueError as ie:
                raise ValueError("Not a valid chat string", 1, "symbol=", w[i])

        result.append(next_1)
    result = "".join(result)
    return result


# __Mandatory Tests__

# In[6]:


try:
    z = 'shkra'
    x = my_transliterate(z, arabic_chat, arabic_letters, True)
    y = my_transliterate(x, arabic_letters, arabic_chat)
    print(z, 'transliterates to', x, 'which transliterates to', y)
except ValueError as e:
    print(e)

try:
    z = 'bnt'
    x = my_transliterate(z, arabic_chat, arabic_letters, True)
    y = my_transliterate(x, arabic_letters, arabic_chat)
    print(z, 'transliterates to', x, 'which transliterates to', y)
except ValueError as e:
    print(e)

try:
    z = 'bxt'
    x = my_transliterate(z, arabic_chat, arabic_letters, True)
    y = my_transliterate(x, arabic_letters, arabic_chat)
    print(z, 'transliterates to', x, 'which transliterates to', y)
except ValueError as e:
    print(e)

try:
    z = 'بنت'
    x = my_transliterate(z, arabic_letters, arabic_chat)
    y = my_transliterate(x, arabic_chat, arabic_letters, True)
    print(z, 'transliterates to', x, 'which transliterates to', y)
except ValueError as e:
    print(e)

try:
    z = 'بqنت'
    x = my_transliterate(z, arabic_letters, arabic_chat, True)
    y = my_transliterate(x, arabic_chat, arabic_letters)
    print(z, 'transliterates to', x, 'which transliterates to', y)
except ValueError as e:
    print(e)

# __Your Tests__

# In[7]:


try:
    h = "Nadia"
    z = "alm6lq"
    x = my_transliterate(z, arabic_chat, arabic_letters, True)
    w = my_transliterate(h, arabic_chat, arabic_letters, True)
    print("My name is Nadia AlMutlak which transliterates to", h, z, "which transliterates into", w, x)
except ValueError as e:
    print(e)

try:
    z = 'رمضان'
    x = my_transliterate(z, arabic_letters, arabic_chat)
    y = my_transliterate(x, arabic_chat, arabic_letters, True)
    print(z, 'transliterates to', x, 'which transliterates to', y)
except ValueError as e:
    print(e)

try:
    z = 'كريم'
    x = my_transliterate(z, arabic_letters, arabic_chat)
    y = my_transliterate(x, arabic_chat, arabic_letters, True)
    print(z, 'transliterates to', x, 'which transliterates to', y)
except ValueError as e:
    print(e)

try:
    a = 'رمضان'
    b = 'كريم'
    x = my_transliterate(a, arabic_letters, arabic_chat)
    y = my_transliterate(b, arabic_letters, arabic_chat)
    print("We would like to wish you a ", a, b, "which transliterates to", x, y)
except ValueError as e:
    print(e)


# __Comments__
#
# * I added some arabic letters just so I could write my name:)
# * I made it accept lower and upper cases

# ## Question 2: Parity Bit/Error Correcting
#
# __Overview__
#
# - "A parity bit, or check bit, is a bit added to a string of binary code to ensure that the total number of 1-bits in the string is even or odd. Parity bits are used as the simplest form of error detecting code." (https://en.wikipedia.org/wiki/Parity_bit)
#
#
# - A byte is 8-bits. Various forms of physical interference or errors can corrupt a bit in transmission, in memory, on a disk, etc. Assume that a bit can be in one of 3 states: 0, 1, U. U indicates that 0/1 state of the bit is uncertain.
#
#
# - Implement two Python classes
#     - ```CorrectingByte``` implements the core logic for a parity correcting byte.
#         - The constructor raises an exception if the data fails a parity check or has more than one 'U' value. If that data has a single 'U', the constructor corrects the data or parity bit.
#         - The method ```set_byte(b)``` sets the object's value. The method:
#             - Sets the value if the byte passes parity check or is has a single 'U'.
#             - If the data has a single 'U', the method corrects the byte or parity bit.
#             - Raise the exception is the byte has more than one 'U' or fails parity check.
#         - ```get_byte()``` returns the correct value of a byte or raises an exception if the byte has become corrupted while stored.
#         - ```flip_bit(i, v, p)``` allows a program to simulate a random change in a bit's value. ```p``` is an optional value. If ```p``` is not ```None``` the method sets the parity bit to ```v```. If ```p``` is ```None,``` the method sets the i-th bit in the byte to ```v.```
#     - ```AbstractBit``` has a constructor, and methods ```set_bit(v)``` and ```get_bit().``` The class ensures that a bit's value is one of 1, 0, U. The class may require additional methods.
#
#

# __Implementation__

# In[31]:


class AbstractBit(object):
    __allowed_values = ('0', '1', "U")

    def __init__(self, v):
        self.set_bit(v)

    def get_bit(self):
        return self.__value

    def set_bit(self, v):
        if v not in AbstractBit.__allowed_values:
            raise ValueError(str(v)) + " is not a valid value for a bit. You can't write bits with that!"
        else:
            self.__value = v

    def __eq__(self, other):
        return self.get_bit() == other.get_bit()

    def __str__(self):
        return str(self.get_bit())


class CorrectingByte(object):
    __no_of_bits = 8

    def __compute_parity(self):
        v = sum([int(x.get_bit()) for x in self.__b])
        v = v % 2
        return v

    def __correct_byte(self):
        # Case 1: too many uncertain bits
        u_count = len([x for x in self.__b if x.get_bit() == "U"])
        if (u_count > 1) or ((self.__p.get_bit() == "U" and (u_count > 0))):
            raise ValueError("Too many U bits")

        # Case 2 : p is U

        if self.__p.get_bit() == "U":
            p = self.__compute_parity()
            self.__p = AbstractBit(str(p))

        # Case 3 There is a single U in the Byte
        try:
            pos = self.__b.index(AbstractBit("U"))
            self.__b[pos] = self.__p
        except ValueError as ve:
            pass

        # Case 4: The byte is messed up
        p = self.__compute_parity()
        pp = self.__p.get_bit()
        if p != int(pp):
            raise ValueError("Byte and parity corrupted due to multiple errors")

        return (self.__b, self.__p)

    def __init__(self, b):
        if len(b[0]) != CorrectingByte.__no_of_bits:
            raise ValueError("Incorrect number of bits!")

        self.__b = [AbstractBit(p) for p in b[0]]
        self.__p = AbstractBit(b[1])
        self.__correct_byte()

    def set_byte(self, b):
        self.__b = [AbstractBit(p) for p in b[1]]
        self.__p = AbstractBit(b[1])
        self.__correct_byte()

    def get_byte(self):
        self.__correct_byte()
        return str(self)

    def flip_bit(self, i, v, p=None):
        if p is not None:
            self.__p = AbstractBit(v)
        else:
            self.__b[i] = AbstractBit(v)

    def __str__(self):
        s = "("
        l = len(self.__b)
        for x in self.__b:
            s += str(x)
        s += "," + str(self.__p) + ")"
        return s


# __Mandatory Test Cases__

# In[30]:


def test1():
    print("Test1:")
    b = CorrectingByte(('11111111', '0'))
    print(str(b))


def test2():
    print("Test2:")
    try:
        b = CorrectingByte(('11111111', '1'))
        print(str(b))
    except ValueError as ve:
        print("test2 - ve = ", ve)


def test3():
    print("Test3:")
    b = CorrectingByte(('10111111', '1'))
    print(str(b))


def test4():
    print("test4:")
    try:
        b = CorrectingByte(('11100111', '0'))
        print(str(b))
    except ValueError as ve:
        print("test4 - ve = ", ve)


def test5():
    print("Test5:")
    try:
        b = CorrectingByte(('111U0111', '0'))
        print(str(b))
    except ValueError as ve:
        print("test5 - ve = ", ve)


def test6():
    print("Test6:")
    try:
        b = CorrectingByte(('11100111', 'U'))
        print(str(b))
    except ValueError as ve:
        print("test6 - ve = ", ve)


def test7():
    print("Test7:")
    try:
        b = CorrectingByte(('1U100111', 'U'))
        print(str(b))
    except ValueError as ve:
        print("test7 - ve = ", ve)


def test8():
    print("Test8:")
    try:
        b = CorrectingByte(('10100111', '1'))
        b.flip_bit(2, 'U')
        v = b.get_byte()
        print(str(v))
    except ValueError as ve:
        print("test8 - ve = ", ve)


test1()
test2()
test3()
test4()
test5()
test6()
test7()
test8()


# __Your Test Cases__

# In[32]:


def test9():
    print("Test9:")
    try:
        b = CorrectingByte(('1100111', 'U'))
        print(str(b))
    except ValueError as ve:
        print("test9 - ve = ", ve)


test9()


def test10():
    print("Test10:")
    try:
        b = CorrectingByte(('1U1U01U1', "1"))
        print(str(b))
    except ValueError as ve:
        print("test10 - ve = ", ve)


test10()


def test11():
    print("Test11:")
    try:
        b = CorrectingByte(('01010101', "U"))
        print(str(b))
    except ValueError as ve:
        print("test11 - ve = ", ve)


test11()

# __Comments__

# ## Question 3: Computing Football Table

# __Overview__
#
# - "The Premier League is the top level of the English football league system. ... ... There are 20 clubs in the Premier League. During the course of a season (from August to May) each club plays the others twice (a double round-robin system), once at their home stadium and once at that of their opponents', for a total of 38 games. Teams receive three points for a win and one point for a draw. No points are awarded for a loss. Teams are ranked by total points, then goal difference, and then goals scored." (https://en.wikipedia.org/wiki/Premier_League)
#
#
# - The file epl2016.csv contains game-by-game results from the 2016-2017 season. The file contains many columns. Only the following contribute to the computation of final standings:
#     - HomeTeam
#     - AwayTeam
#     - FTHG: The number of goals the home team scored.
#     - FTAG: The number of goals the away team scored.
#     - FTR: Is 'H', if the home team won, 'A' if the away team won and 'D' if the match was a draw.

# <u>Tasks</u>
#
# You will implement several functions. Your functions will use Pandas and matplotlib.pyplot.
#
# - ```load_epl_games(file_name)``` loads the file and creates a Pandas data frame containing the contents.
#
#
# - ```get_points(team, table)``` takes a team name and a Pandas data frame. The method returns the number of points that the team earned.
#
#
# - ```get_finish(team, table)``` returns the finishing position of a team.
#
#
# - ```compute_table(df)``` uses the finishing position rules to return the final table.
#     - The table is sorted by the finishing position rules.
#     - The columns are ```Team,``` ```Points,``` ```Goals``` and ```GoalDifference.```
#
#
# - ```display_hbar(tables)``` displays a horizontal bar chart.
#     - The bar chart is sorted from final position from 1st place to last place.
#     - The bar is the number of points.
#

# In[103]:


import pandas as pd
import matplotlib.pyplot as plt


def load_epl_games(file_name):
    football_df = pd.read_csv(file_name)
    return football_df


def compute_table(df):
    df2 = df[["Date", "HomeTeam", "AwayTeam", "FTR", "FTHG", "FTAG"]].copy()
    result = pd.DataFrame()

    result['Team'] = get_team_names(df)
    result['Points'] = 0
    result['GoalDifference'] = 0
    result['Goals'] = 0
    result = result.set_index(['Team'])

    for r in df2.itertuples():

        if r.FTR == "H":
            result.loc[r.HomeTeam, "Points"] += 3
        elif r.FTR == "A":
            result.loc[r.AwayTeam, "Points"] += 3
        else:
            result.loc[r.HomeTeam, "Points"] += 1
            result.loc[r.AwayTeam, "Points"] += 1

        result.loc[r.HomeTeam, "Goals"] += r.FTHG
        result.loc[r.HomeTeam, "GoalDifference"] += r.FTHG - r.FTAG
        result.loc[r.AwayTeam, "Goals"] += r.FTAG
        result.loc[r.AwayTeam, "GoalDifference"] += r.FTAG - r.FTHG

    result = result.sort_values(by=["Points", "GoalDifference", "Goals"], ascending=False)
    finish = 1
    result["Finish"] = 0
    for r in result.index:
        result.loc[r, "Finish"] = finish
        finish = finish + 1
    return result


def get_team_names(table):
    result = table["HomeTeam"].unique()
    return result


def get_points(team, table):
    return table.loc[team, "Points"]


def get_finish(team, table):
    return table.loc[team, "Finish"]


def display_hbar(table):
    fig, ax = plt.subplots(figsize=(10, 10))
    t = table.index
    t = list(t)
    t.reverse()
    p = list(table["Points"])
    p.reverse()
    ax.barh(t, p, align="center", alpha=0.5)
    plt.ylabel('Team')
    plt.xlabel('Points')
    ax.tick_params(labeltop=True, bottom=True)
    ax.set_xticks(range(0, 100, 10))
    for d2 in range(0, 100, 5):
        plt.axvline(x=d2, color="k", linestyle='--')

    plt.show()


games = load_epl_games('epl2016.csv')
final_table = compute_table(games)

# __Mandatory Tests__
#
# Note: Your bar chart does not need to be as "pretty" as the test below.

# In[104]:


final_table

# In[105]:


print("Arsenal earned ", get_points("Arsenal", final_table), "points.")

# In[106]:


print("Arsenal finished in ", get_finish("Arsenal", final_table), "position.")

# In[107]:


display_hbar(final_table)

# __Your Tests__
#
# This would be a great place to show some tests for errors, and also computing some interest values from various operations on the table, e.g.
# - Total number of goals scored.
# - Average number of goals scored for a set of teams.
# - etc.

# In[109]:


print("We have a total of", final_table["Finish"].count(), "finishing teams in this year's statisical analysis!")
print("We found that the average goals for all teams was", final_table["Goals"].mean(), "goals,")
print("and the sum of all goals was", final_table["Goals"].sum(), ".")
print('')
print("The top three teams had an average score of", final_table.iloc[0:3, 2].mean(), ",")
print("whereas the bottom three teams had an average score of", final_table.iloc[17:20, 2].mean())
print("This seems accurate as the standard deviation of all the scores was", final_table["Goals"].std())
print('')
print("The team with the highest points in the league, Chelsea, had", final_table["Points"].max(), "points.")
print("However, they only scored", final_table.iloc[0, 2],
      "so they did not score the most goals in the leage which was", final_table["Goals"].max())
print("So how did they win?")
print("")

# __Comments__