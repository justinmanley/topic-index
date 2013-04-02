A simple topic index generator implemented in python.  This program takes as its input a large piece of text and
outputs a list of the important topics in the text.

I use a simple heuristic for extracting the topics from a text: I extract the frequency of each word in the text,
normalize it with respect to the COCA (Corpus of Contemporary American English) word frequency list, and then
extract only those words which appear more frequently in the text than in the COCA word frequency list.

Tested on Aristotle's Politics, Mark Twain's Huck Finn, and The Decline and Fall of the Roman Empire:

The Decline and Fall of the Roman Empire

Valerian 
inroad
barbarians
skilful
dominions
appellation
emperors
consuls
effectually
Parthians
auxiliaries
Parthian
actuated
condescended
tribunes
buckler
provincials
appellations
devastations
polytheism
sacerdotal
pontiffs
rashness
liberality
insensibly
satraps
proconsul
.
.
.

Huck Finn

Sally
reckon
somewheres
reckoned
niggers
nigger
betwixt
ransomed
waked
knowed
genies
stile
git
fust
dat
looky
yaller
cussed
cussing
nabob
drawed
hove
roust
steamboat
ferryboat
.
.
.

Politics

lawgiver
dissensions
aristocracy
oligarchy
kingly
freeman
necessaries
employments
Solon
procures
desirous
therewith
skilful
artificer
magistrates
oftener
Cretans 
gymnastic
sedition
soldiery
Carthaginians
Doric
fitly
demagogues
oligarchies
tyrannies
flatterers
preceptors

While many important words are being extracted, there are two problems
  * important topic words are being left out (virtue and citizen is left out of the topic index for the Politics)
  * there's lots of detritus - words that are not important topic words

The heuristic needs to be modified to improve the topic index.  Some ideas:
  * Take frequency rank into account
  * Word stemming
  * Filter words by part-of-speech
  * Use a synonym dictionary to filter words
