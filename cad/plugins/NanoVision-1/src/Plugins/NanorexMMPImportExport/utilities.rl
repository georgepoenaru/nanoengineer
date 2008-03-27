
%%{

# NOTES:
# Define the following variables in scope
#     int intVal, intVal2;
#     std::string stringVal, stringVal2;
#     int x, y, z;
#
# Define the following (inline) function
#     void stripTrailingWhiteSpaces(std::string& s) {
#         std::string::const_reverse_iterator endCharIter = s.rbegin();
#         int num_ws = 0;
#         while(isspace(*endCharIter) && endCharIter != s.rend()) {
#             ++num_ws;
#             ++endCharIter;
#         }
#         s.resize((int)s.size()-num_ws);
#     }
#
    machine utilities;

    NEWLINE = '\n';
    EOF = 0xff ;
    nonNEWLINE = any - ('\n' | 0xff);
    
    IGNORED_LINE = nonNEWLINE*   NEWLINE;
    
    # Possible ways a line can end - with or without an inline comment
    # - also serves to catch whole blank or comment lines
    EOL = space* ('#' nonNEWLINE**)?   NEWLINE;
    
    whole_number = digit digit**
		>to{intVal=fc-'0';}
        ${intVal = intVal*10 + (fc-'0');}
    ;
    
	whole_number2 = digit digit**
		>to{intVal2=fc-'0';}
		${intVal2 = intVal2*10 + (fc-'0');}
	;
	
    integer = ('+'? whole_number ) | ('-' whole_number %{intVal=-intVal;}) ;
    
    
    real_number = [+\-]? digit digit** ( '.' digit** ([eE] [+\-]? digit digit**)? )?
        >{stringVal.clear(); stringVal = stringVal + fc; doubleVal = HUGE_VAL;}
        ${stringVal = stringVal + fc;}
        %{doubleVal = atof(stringVal.c_str());}
    ;
    
    
    char_string = ('_' | alnum) (alnum | [_\-])**
		>to{/*stringVal.clear();*/ stringVal = fc; }
        ${stringVal = stringVal + fc; }
    ;
    
    
    # Character string with spaces in between
    # - must be at least 1 character long, and must end in a non-whitespace char
	# KNOWN ISSUE: the string identified includes trailing spaces
    char_string_with_space_pattern =
		('_' | alnum)  (((space-'\n') | [_\-] | alnum)** ('_' | alnum))?;
    
    
    # Default assignment of identified character-string-with-spaces pattern
	# KNOWN ISSUE: the string identified includes trailing spaces
	char_string_with_space = char_string_with_space_pattern
        >to{stringVal.clear();}
        ${stringVal = stringVal + fc; }
		% { /*stripTrailingWhiteSpaces(stringVal);*/ }
	;
    
    
    # Alternate assignment of identified character-string-with-spaces pattern
    # - useful in a binary expression
	# KNOWN ISSUE: the string identified includes trailing spaces
	char_string_with_space2 = char_string_with_space_pattern
        >to{stringVal2.clear();}
        ${stringVal2 = stringVal2 + fc; }
		% { /*stripTrailingWhiteSpaces(stringVal2);*/ } 
    ;
    
}%%

