The general purpose of my program is to make it easier for students to keep track of their test scores and grade-point averages.
2 possible users of the program could be a teacher and a student. A student could use it to keep track of scores and even simulate how future grades could impact their average, while a teacher could use it to keep track of each of the classes they teach. A test score could the be the average test score on a test they give, and they could use this to see how their grading compares across classes and tests.
A non-negotiable is the get_average feature, because without it, it's impossible to calculate GPA or someone's best and worse classes. A nice to have feature is the option to show the user each individual grade. Once it goes into the general list, each individual score doesn't really matter too much.
I mentioned simulation of grades, but I would actually build that out in future iterations--the ability to keep some scores (the official ones) final and others (simulated ones) to be deleted could be powerful.
I'd also add the ability to weight each test, because most classes don't have every single assignment weighted the same. I'd create a class that tracked 
-grade and 
-points out of,
and use the properties of that class to weight the averages. This would make the program much more accurate.