"""
sim.pyx

$Id$

Note: this file is processed by Pyrex to produce sim.c in this directory
(not in the build subdirectory). [bruce 060101]

Example usage script:

make clean; make pyx && python -c "import sim; sim.test()"
"""
__author__ = "Will"

import threading
import Numeric

cdef extern from "simhelp.c": 
    # note: this produces '#include "simhelp.c"' in generated sim.c file,
    # but distutils fails to realize there's a dependency on simhelp.c,
    # so I added some Makefile dependencies to fix that,
    # but these mean that sim.c is produced in the makefile
    # rather than by setup.py. [bruce 060101]
    char *filename
    # stuff from globals.c
    int debug_flags
    int Iteration
    int ToMinimize
    int IterPerFrame
    int NumFrames
    int DumpAsText
    int DumpIntermediateText
    int PrintFrameNums
    int OutputFormat
    int KeyRecordInterval
    int DirectEvaluate
    int Interrupted
    char *IDKey
    char *baseFilename
    char *OutFileName
    char *TraceFileName
    double Dt
    double Dx
    double Dmass
    double Temperature
    # end of globals.c stuff

    getMostRecentFrame()
    void initsimhelp()
    void readPart()
    void dumpPart()
    void everythingElse()
    cdef char *structCompareHelp()

    void strcpy(char *, char *) #bruce 051230 guess


cdef class Minimize:
    """Pyrex permits access to doc strings"""

    def __init__(self, fname):
        global ToMinimize, DumpAsText, filename
        ToMinimize = 1
        DumpAsText = 1
        filename = fname
        initsimhelp()
        readPart()

    def __getattr__(self, key):
        if key == "debug_flags":
            return debug_flags
        elif key == "Iteration":
            return Iteration
        elif key == "ToMinimize":
            return ToMinimize
        elif key == "IterPerFrame":
            return IterPerFrame
        elif key == "NumFrames":
            return NumFrames
        elif key == "DumpAsText":
            return DumpAsText
        elif key == "DumpIntermediateText":
            return DumpIntermediateText
        elif key == "PrintFrameNums":
            return PrintFrameNums
        elif key == "OutputFormat":
            return OutputFormat
        elif key == "KeyRecordInterval":
            return KeyRecordInterval
        elif key == "DirectEvaluate":
            return DirectEvaluate
        elif key == "Interrupted":
            return Interrupted
        elif key == "IDKey":
            return IDKey
        elif key == "baseFilename":
            if baseFilename == NULL: #bruce 051230 prevent exception when this is NULL (its default value)
                return "" # (not sure if None would be permitted here; probably it would, but this is better anyway)
            return baseFilename
        elif key == "OutFileName":
            if OutFileName == NULL:
                return ""
            return OutFileName
        elif key == "TraceFileName":
            if TraceFileName == NULL:
                return ""
            return TraceFileName
        elif key == "Dt":
            return Dt
        elif key == "Dx":
            return Dx
        elif key == "Dmass":
            return Dmass
        elif key == "Temperature":
            return Temperature
        else:
            raise AttributeError, key

    def __setattr__(self, key, value):
        if key == "debug_flags":
            global debug_flags
            debug_flags = value
        elif key == "Iteration":
            global Iteration
            Iteration = value
        elif key == "ToMinimize":
            global ToMinimize
            ToMinimize = value
        elif key == "IterPerFrame":
            global IterPerFrame
            IterPerFrame = value
        elif key == "NumFrames":
            global NumFrames
            NumFrames = value
        elif key == "DumpAsText":
            global DumpAsText
            DumpAsText = value
        elif key == "DumpIntermediateText":
            global DumpIntermediateText
            DumpIntermediateText = value
        elif key == "PrintFrameNums":
            global PrintFrameNums
            PrintFrameNums = value
        elif key == "OutputFormat":
            global OutputFormat
            OutputFormat = value
        elif key == "KeyRecordInterval":
            global KeyRecordInterval
            KeyRecordInterval = value
        elif key == "DirectEvaluate":
            global DirectEvaluate
            DirectEvaluate = value
        elif key == "Interrupted":
            global Interrupted
            Interrupted = value
        elif key == "IDKey":
            global IDKey
            IDKey = value
        elif key == "baseFilename":
            global baseFilename
            baseFilename = value
        elif key == "OutFileName":
            global OutFileName
            assert len(value) < 1024
            strcpy( OutFileName, value)
        elif key == "TraceFileName":
            global TraceFileName
            assert len(value) < 1024
            strcpy( TraceFileName, value)
        elif key == "Dt":
            global Dt
            Dt = value
        elif key == "Dx":
            global Dx
            Dx = value
        elif key == "Dmass":
            global Dmass
            Dmass = value
        elif key == "Temperature":
            global Temperature
            Temperature = value
        else:
            raise AttributeError, key

    def go(self):
        everythingElse()

    def structCompare(self):
        r = structCompare()
        if r:
            raise Exception, r

# The idea of a global most-recent frame is very non-object-oriented.
# Maybe I'll get a better idea over the next few days.  wware 060101
def getFrame():
    frm = getMostRecentFrame()
    atoms = len(frm) / (3 * 8)
    array = Numeric.fromstring(frm, Numeric.Float64)
    return Numeric.resize(array, [atoms, 3])

class Dynamics(Minimize):
    def __init__(self, filename):
        global ToMinimize, DumpAsText
        ToMinimize = 0
        DumpAsText = 0
        self.__init(filename)

def test():
    # m = Minimize("tests/rigid_organics/test_C6H10.mmp")
    m = Minimize("tests/minimize/test_h2.mmp")
    m.go()
    print getFrame()

def test2():
    d = Dynamics("tests/rigid_organics/test_C6H10.mmp")
    d.go()
    print getFrame()
