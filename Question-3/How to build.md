***********************************************************
Requirements --->>
1. python 3.5.
2. epydoc.
3. pylint (for pyreverse).
4. dot (dot to pdf convert).
5. pdfunite to merge pdf (class diagram).
6. Okular (For opening documentation)
***********************************************************

************************************************************
To build code.
************************************************************
>> python3.5 source/main.py

************************************************************
To generate documentation
************************************************************
>> cd source
>> epydoc --pdf -o DOC --name "Assignment PPL Question-3" *


************************************************************
To view documentaion
************************************************************
>> cd source/DOC
>> okular api.pdf

************************************************************
To generate class diagram
************************************************************
>> cd source
>> pyreverse *
>> dot -Tpdf classes_No_Name.dot -o 1.pdf
>> dot -Tpdf packages_No_Name.dot -o 2.pdf
>> pdfunite 1.pdf 2.pdf class_diagram.pdf

************************************************************
clear extra files
************************************************************
>> rm 1.pdf
>> rm 2.pdf
>> rm classes_No_Name.dot
>> rm packages_No_Name.dot
