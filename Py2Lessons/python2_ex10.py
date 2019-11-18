#Benpy lmao

#anyway some notes:
#\ is a way to put difficult-to-type characters or format functions into a string.
#example, \n generates a line break
#the book refers to these as "escape sequences"

#there is a single vs. double quote example in the book as well:
#"I am 6'2\" tall." -- basically this tells Py that the inches quote is not a real end quote.
#'I am 6\'2" tall.' -- same thing but with the foot quote.

#note that using these sorts of statements with %r will not hide the \.
#because %r is the raw data, so it's literal.

tabby_cat = "\tI'm tabbed in." #\t tabs the text
persian_cat = "I'm split\non a line." #new line, as previously stated
backslash_cat = "I'm \\ a \\ cat." #\\ just adds a \ so it's not read as divide

#lol it's Nero
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''
#\t* Catnip\n\t* Grass started a new line and kept the tab before the *

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

#the book included a list of escape sequences:
# \\    Backslash (\)
# \'    Single- quote (')
# \"    Double- quote (")
# \a    ASCII bell (BEL)
# \b    ASCII backspace (BS)
# \f    ASCII formfeed (FF)
# \n    ASCII linefeed (LF)
# \N{name}      Character named name in the Unicode database (Unicode only)
# \r    ASCII carriage return (CR)
# \t    ASCII horizontal tab (TAB)
# \uxxxx    Character with 16- bit hex value xxxx (Unicode only)
# \Uxxxxxxxx     Character with 32- bit hex value xxxxxxxx (Unicode only)
# \v    ASCII vertical tab (VT)
# \ooo      Character with octal value oo
# \xhh      Character with hex value hh