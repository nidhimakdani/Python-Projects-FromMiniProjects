print("This is going to be my First project of python... In this project you will get information about languages like C, Cpp, Java, Python just write ex. Java")

languagedict = {
"C":"C is a general-purpose high level language that was originally developed by Dennis Ritchie for the Unix operating system. It was first implemented on the Digital Eqquipment Corporation PDP-11 computer in 1972. The Unix operating system and virtually all Unix applications are written in the C language.",
"Java":"A small history of Java. Java is a programming language created by James Gosling from Sun Microsystems (Sun) in 1991. The target of Java is to write a program once and then run this program on multiple operating systems. The first publicly available version of Java (Java 1.0) was released in 1995.",
"Cpp":"C++ is a cross-platform language that can be used to create high-performance applications. C++ was developed by Bjarne Stroustrup, as an extension to the C language. C++ gives programmers a high level of control over system resources and memory.",
"Python":"Python has a simple syntax similar to the English language. Python has syntax that allows developers to write programs with fewer lines than some other programming languages. Python runs on an interpreter system, meaning that code can be executed as soon as it is written."
}

selectedlang = input()

print("Thank You For Selecting Language:\n",languagedict[selectedlang])
