# P12-Design
CS301-12
Program Skills
Creating a design document
Designing a program from an idea
Summary
This week, we'll be taking a step back and focusing exclusively on the problem-solving portion of programming.

You are creating software to run a vending machine. (What kind? Up to you! You will get to make a lot of creative design decisions this week.) It's relatively complicated, and several people will be helping to implement the program, so you want to have a common, detailed design spec to work from so that everyone's code will work the same way.

Program Requirements
The program you design must:

Maintain an inventory of its products (how many of each product does it have).
Maintain a running total of how much money it has made.
Allow the user to select from a display of items.
Accept coins from the user to purchase an item (1, 5, 10, 25 cents).
Give the user their product, and change in coins if they overpay.
Allow the user to cancel the transaction and give a refund.
The specifics of how these will work is up to you, but you should make and write down those decisions. If you'd like to add additional functionality, you are welcome to do so! Be creative :)

Document Requirements
Here are some guidelines for creating your document:

Be organized. Divide your document up into sections, one for each of the points above, and add other sections as needed.
Be detailed. There is a difference between "read the file in" (not specific enough!), "read the whole file in as a string", and "loop through the file" - be as detailed as possible when describing your design.
Be complete. Are you using any external modules? Which ones? What functions/methods will you write? How will they work? What are their parameters and return values?
And of course, check your spelling. This isn't an English class, but using proper grammar and spelling facilitate the clear communication of ideas.
You are welcome to include flow charts and other graphical representations of your design in your document!
There is no length requirement for this document, but if your design takes less than a page to describe, consider that you might not be going into enough detail.

For example, I might describe my design for normalizing the file in P11: What Should I Read? as:

Open the file for reading, if it exists, and get the contents as one string. Close the file. Create an empty string for building the normalized file, and loop through the original file one character at a time. If the character is a letter, concatenate the lowercase version onto the normalized string; if the character is whitespace, concatenate it onto the normalized string directly. Ignore all other characters. Return the normalized string once the loop is complete.

But if I just said something like

Read the file in, make it lower case, remove punctuation, return it.

that wouldn't be getting specific enough. You don't have to be extremely wordy, but in this case, it's not clear how I should read the file in (there are three different ways), whether there should be error checking, how I'm removing punctuation, or even what type of value that function would be returning.

Handing In Your Design
Students completing this program in pairs should join a P12 Group. If you are having trouble joining (not creating!) a P12 Group, please contact Hobbes with your partner's name.

You may upload your design document in any format.
