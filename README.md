# FLashcards-for-German-Words-and-their-Translations
This is a Basic Flashcard Application to learn different languages made with Python GUI, Tkinter.  This project is catered towards German Language but you can easily change it to any other language of your choice just by changing the language name and the csv file.

TRICK: To create the csv file of any language of your choice, click on this link: https://github.com/hermitdave/FrequencyWords/tree/master/content/2018 to visit @hermitdave word compilation repository. 
Select the language you like and copy the words, paste it in google sheets 
In the column next to the word write '=GOOGLETRANSLATE(A1,L1,L2)', A1 = click on the word you want to translate, L1=language code for the language you want to translate, in this case 'de' (german), L2= language code for the language you want to translate to, in this case 'en' (English). 
Drag it to all the rows and download the file in .csv format

The User Interface is really simple, it has the flash card (two faces) and two buttons put in place using the Canvas and the Button class respectively.

A timer is employed with the 'after' method.
