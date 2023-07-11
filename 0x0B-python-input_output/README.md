**General**

*Why Python programming is awesome*

*How to open a file*

*How to write text in a file*

*How to read the full content of a file*

*How to read a file line by line*

*How to move the cursor in a file*

*How to make sure a file is closed after using it*

*What is and how to use the with statement*

*What is JSON*

*What is serialization*

*What is deserialization*

*How to convert a Python data structure to a JSON string*

*How to convert a JSON string to a Python data structure*


***DIVE INTO PYTHON3***

*• In Files, you’ll learn the difference between reading files in “binary” and “text” mode. Reading (and writing!)

*files in text mode requires an encoding parameter. Some text file methods count characters, but other*

*methods count bytes. If your code assumes that one character == one byte, it will break on multi-byte*

*characters.*

*• In HTTP Web Services, the httplib2 module fetches headers and data over HTTP. HTTP headers are*

*returned as strings, but the HTTP body is returned as bytes.*

*• In Serializing Python Objects, you’ll learn why the pickle module in Python 3 defines a new data format that*

*is backwardly incompatible with Python 2. (Hint: it’s because of bytes and strings.) Also JSON, which doesn’t*

*support the bytes type at all. I’ll show you how to hack around that.*

*• In Case study: porting chardet to Python 3, it’s just a bloody mess of bytes and strings everywhere.*


***json**

*JSON (JavaScript Object Notation), specified by RFC 7159 (which obsoletes RFC 4627)*

*and by ECMA-404, is a lightweight data interchange format inspired by JavaScript object*

*literal syntax (although it is not a strict subset of JavaScript)*

**Warning** *Be cautious when parsing JSON data from untrusted sources. A malicious JSON*

*string may cause the decoder to consume considerable CPU and memory resources. Limiting the size of data to be parsed is recommended.*

*json exposes an API familiar to users of the standard library marshal and pickle modules.*

**Note** *JSON is a subset of YAML 1.2. The JSON produced by this module’s default settings*

*(in particular, the default separators value) is also a subset of YAML 1.0 and 1.1. This module can thus also be used as a YAML serializer.*


**py-file I/O**

*When we talked about storing our data somewhere, we meant storing our data into files.*

*A file is a container that stores information, right? In computer systems, a file is a contiguous set of bytes.

*Data in a computer system is always stored into files.*

*Files can take different forms depending on the user requirements like data files, text files, program executable files etc.*

*A computer processes these files by translating them into 0s and 1s.*

*So all the text, images, videos that you store on your computer are nothing but a series of 0s and 1s.*

*Every file contains three main parts:*

*1. Header: This contains information about the file i.e. file name, file type, file size etc.*

*2. Data: This is the actual information/content stored in the file.*

*3. End of file: This is a special character that marks the end of the file.*

*Also, in a file, a new line character (‘\n’) marks the end of a line or start of a new line.*


***Automate the Boring Stuff with Python**

*The best part of programming is the triumph of seeing the machine do something useful.*

*Automate the Boring Stuff with Python frames all of programming as these small triumphs; it makes the boring fun.*

*In Automate the Boring Stuff with Python, you'll learn how to use Python to write programs that do in minutes*

*what would take you hours to do by hand - no prior programming experience required. Once you've mastered the basics of*

*programming, you'll create Python programs that effortlessly perform useful and impressive feats of automation to:*

*Search for text in a file or across multiple files*

*Create, update, move, and rename files and folders*

*Search the Web and download online content*

*Update and format data in Excel spreadsheets of any size*

*Split, merge, watermark, and encrypt PDFs*

*Send reminder emails and text notifications*

*Fill out online forms*
