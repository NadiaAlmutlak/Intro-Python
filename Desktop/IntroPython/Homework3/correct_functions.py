# Modified by Donald F. Ferguson, Columbia University, 2018


# Import some frameworks that help us implement a web application.
from flask import Flask, render_template_string, request
from wtforms import Form, validators, TextField
import string


##############################################################################################################
# These are the two functions you will write.
# You will implement in a separate Python file and access via an import statement.
# The code here is a just a placeholder.


# 1. Check a dictionary to determine if word is correctly spelled.
# 2. If not, call a set of functions that generate "near by, correctly spelled words."
# 3. Return the 5 "best suggested corrections."

#Reads data file, and create lists of each line.

def format_data(csv_file):
    important = []
    with open (csv_file) as f:
        temp = f.read()
        temp = temp.split('\n')
        # Create a loop which runs through all the strings and splits the "words" from dictionary
        for row in temp:
            v=row.split(",")
            #important.append(v[0])
            important.append(v)
        print(important)
        f.close()

    return important


format_data("dictionary.csv")

# 1- Function produces a list of words with the input word's letters transposed
def generate_transposes(word,d):
    transposed = []
    # This was NOT that that hard to write, but ...
    # is not easy to understand and I should have a comment or two,
    for i in range(0,len(word)-1):
        l = word[:i]
        c1 = word[i]
        c2 = word[i+1]
        r = word[i+2:]
        n = l + c2 + c1 + r
        if check_word_simple(n,d):
            transposed.append(n)

    return transposed



#2- Function produces a list of words that contain every possible insertion of every letter in a-z in all positions
def generate_alphabet(word,d):
    alphabet=[] #creates a list for us to store information in
    alpha = "abcdefghijklmnpqrstuvwxyz"
    n=len(word)
    for i in range(n+1): #for all the slot in the word and one slot after
        for j in alpha: #for each letter in our alphabet list
            alpha_add=word[0:i]+ j+ word[i:] #Slices the word and adds a letter in each slot
            if check_word_simple(alpha_add,d):
                alphabet.append(alpha_add)

    return alphabet

#3- Function Produces a list containing pairs of words with spaces

def generate_spaces(word,d):
    spaced = [] #creates a list for us to store information in
    n = len(word)
    for i in range(n - 1):
        #space_add = word[0:i+1] + " " + word[i+1:]
        l = word[0:i+1]
        r = word[i+1:]
        if check_word_simple(l,d) and check_word_simple(r,d):
            spaced.append(l + " " + r)
    return spaced


# 4- produce a list of words with each letter removed
def generate_deleted(word,d):
    deleted = [] #creates a list for us to store information in
    n = len(word)
    for i in range(n):
        deleted_add = word[0:i] + word[i+1:]
        if check_word_simple(deleted_add,d):
            deleted.append(deleted_add)
    return deleted

#5- is there any entry for which the user created a new correction for the misspelled word


def check_word_simple(w,d):
    for l in d:
        if w == l[0]:
            return True
    else:
        return False

def generate_old_corrections(w, d):
    result = []
    for l in d:
        try:
            if len(l)>=3:
                if l[2] == w:
                    result.append(l[0])
        except:
            print("l = ", l)

    return result

 # Checks if the input word is in the list we defined using our format_data function
 # with the use of our dictionary file
def check_word(word):
    # Your code and called functions go here.
    possible = []
    dict_words = format_data("dictionary.csv") #Calls our dictioanry so we can run words through it
    if check_word_simple(word,dict_words):
        return "Your spelling is correct!"
    else:
        #compiles a list of all possible edits and words
        d = dict_words
        possibilities= generate_transposes(word,d)+generate_alphabet(word,d)+generate_spaces(word,d)+generate_deleted(word,d)
        possibilities = possibilities + generate_old_corrections(word, dict_words)
        for element in possibilities:
            if not element in possible:
                possible.append(element)
 #       if len(possible) == 0:
 #           return possibilities
 #       else:
        return possible


def save_dict(d):
    f = open("dictionary.csv","w")
    for l in d:
        try:
            l = map(str,l)
            ll = ",".join(l)
            f.writelines(ll)
            f.write("\n")
        except:
            print("l = ", l)

    f.close()


def update_selected(w, d):
    for l in d:
        if l[0] == w:
            temp = int(l[3])
            l[3] = temp + 1
            break


# The user selected a correction, or entered a new correct spelling.
# We will record the correct spelling and score as a possible common correction for user.
def update_corrections(original_word, corrected_word):
    # Your code goes here.
    dict_words=format_data("dictionary.csv")
    if check_word_simple(corrected_word, dict_words):
        #calculate increments

        update_selected(corrected_word, dict_words)
        save_dict(dict_words)
        return "Word is already in dictionary"
    else:
        n = [corrected_word, 0, original_word, 0, 0]
        dict_words.append(n)
        save_dict(dict_words)

    print("Correction for " + original_word + " is " + corrected_word)

# End of where your code will go.
##############################################################################################################

# Include and initialize the Flask framework.
app = Flask(__name__)


# html page is the view. Putting templates directly in the application is a massive anti-pattern.
# Also, most programmers and applications do not use static HTML templates like this one.
# I will give you the HTML pages to "serve" in your application.
#
page = '''
<html>
   <head>
      <title>HW3 -- The Spelling Correction Suggester!</title>
      <script>
        function myFunction() {
            var x = document.getElementById("told_you_so");
            if (x.style.display === "none") {
                x.style.display = "block";
            }
            else {
                x.style.display = "none";
            }
        }
        </script>
   </head>

   <body>
      <h1>HW3 -- Nadia AlMutlak's Spelling Police</h1>
      <h2>Our Motto is, "To correct and serve!"</h2>

      <form method=post action="">
         So, you think you can spell?
      <br>
      Enter a word.
         {{ template_form.text_field }}
      <br>
        {% if result != None %}
        <br>
           Did you possibly mean? {{ result }}
        <br>
        {% endif %}
      <br>
        <input type=submit value=Check>
      </form>
       <button onclick="myFunction()">What does this button do?</button>
       <div id="told_you_so" style="display:none;">
        <p>
        <span style="color:red;font-size: 32px;">
        Told you web apps are in the textbook.
        </span>
        </div>
   </body>
</html>
'''


# InputForm and below is our controller
# form with a single TextField.
# This is part of the framework and you do not need to worry about it.
class InputForm(Form):
    text_field = TextField(validators=[validators.InputRequired()])


# This is the core of the web application server and implementing the page delivery and REST API.
@app.route('/', methods=['GET', 'POST'])
def index():
    spell_result = None
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        input_val = form.text_field.data
        # input val is the input value on the web page
        spell_result = check_word(input_val)
    return render_template_string(page, template_form=form, result = spell_result)


if __name__ == '__main__':
    app.run(debug=True)