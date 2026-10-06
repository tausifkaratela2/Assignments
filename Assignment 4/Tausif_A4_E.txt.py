- Why do we make an attribute private with two underscores instead of leaving it public?
-> because the following attribute cannot be accessed by any other block of code. The value declared at first with two underscores cannot be overridden or changed by any other code logic. This also helps enforce encapsulation and prevent accidental modifications.


 - Why is a CSV file often more useful than a plain text file for this kind of data?
-> umm.. Because we can perform many actions on an excel file? Like formatting, formulas, etc. The txt file is just a normal text file, like a notebook. 



 - What does JSON give you that CSV does not?
-> 


 - Why put anything in a finally block at all, when the code after the try would run anyway?
-> code after try/except only runs if an exception is either not raised or explicitly caught. A finally block is guaranteed to run.
