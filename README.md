# WordsScrambler

* Write a Python program that reads a text file, scrambles the words in the file on following rules and writes the output to
  a new text file:
  - Words less than or equal to 3 characters need not be scrambled
  - Don't scramble first and last char, so Scrambling can become Srbmnacilg or Srbmnailcg or Snmbracilg , 
    i.e. letters except first and last can be scrambled in any order
  - Punctuation at the end of the word to be maintained as is i.e. "Surprising," could become "Spsirnirug," but not "Spsirn,irug"
  - Following punctuation marks are to be supported - Comma Question mark, Full stop, Semicolon, Exclamation
  - Do this for a file and maintain sequences of lines
    Hint: use random module of Python for scrambling
