"""Classes for elements, atoms, bonds, molecules

"""
__author__ = "Josh"

from VQT import *
from LinearAlgebra import *
import string
import re
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from drawer import *
from shape import *

from constants import *

CPKvdW = 0.25

assyList = []

Elno = 0

Gno = 0
def gensym(string):
    """return string appended with a unique number"""
    global Gno
    Gno += 1
    return string + str(Gno)

def genKey():
    """ produces generators that count indefinitely """
    i=0
    while 1:
        i += 1
        yield i

atKey=genKey()


def povpoint(p):
    # note z reversal -- povray is left-handed
    return "<" + str(p[0]) + "," + str(p[1]) + "," + str(-p[2]) + ">"


class elem:
    """one of these for each element type"""
    def __init__(self, sym, n, m, rv, col, bn):
        """called from a table in the source
        
        sym = (e.g.) "H"
        n = (e.g.) "Hydrogen"
        m = atomic mass in e-27 kg
        rv = van der Waals radius
        col = color (RGB, 0-1)
        bn = bonding info: list of triples:
             # of bonds in this form
             covalent radius
             angle between bonds in degrees
        """
        global Elno
        self.atnum = Elno
        Elno += 1
        self.symbol = sym
        self.name = n
        self.color = col
        self.mass = m
        self.rvdw = rv
        self.rcovalent = bn and bn[0][1]/100.0
        self.bonds = bn
        self.numbonds = bn and bn[0][0]
        self.base = None
        self.quats = []
        if bn and bn[0][2]:
            s = bn[0][2][0]
            self.base = s
            for v in bn[0][2][1:]:
                self.quats += [Q(s,v)]

    def __repr__(self):
        return "<Element: " + self.symbol + "(" + self.name + ")>"

# the formations of bonds -- standard offsets
uvec = norm(V(1,1,1))
tetra4 = uvec * A([[1,1,1], [-1,1,-1], [-1,-1,1], [1,-1,-1]])
tetra3 = uvec * A([[-1,1,-1], [-1,-1,1], [1,-1,-1]])
oxy2 = A([[-1,0,0], [0.2588, -0.9659, 0]])
tetra2 = A([[-1,0,0], [0.342, -0.9396, 0]])
straight = A([[-1,0,0], [1,0,0]])
flat = A([[-0.5,0.866,0], [-0.5,-0.866,0], [1,0,0]])


#      sym   name          mass    rVdW  color
#      [[Nbonds, radius, angle] ...]
Mendeleev=[ \
 elem("X", "Singlet",      0.001,  1.1,  [0.8, 0.0, 0.0],
      [[1, 0, None]]),
 elem("H",  "Hydrogen",    1.6737, 1.2,  [0.0, 0.6, 0.6],
      [[1, 30, None]]),
 elem("He", "Helium",      6.646,  1.4,  [1.0, 0.27, 0.67],
      None),
 elem("Li", "Lithium",    11.525,  4.0,  [0.0, 0.5, 0.5],
      [[1, 152, None]]),
 elem("Be", "Beryllium",  14.964,  3.0,  [0.98, 0.67, 1.0],
      [[2, 114, None]]),
 elem("B",  "Boron",      17.949,  2.0,  [0.3, 0.3, 1.0],
      [[3, 90, flat]]),
 elem("C",  "Carbon",     19.925,  1.84, [0.04, 0.2, 0.0],
      [[4, 77, tetra4], [3, 71, flat], [2, 66, straight], [1, 59, None]]),
 elem("N",  "Nitrogen",   23.257,  1.55, [0.84, 0.37, 1.0],
      [[3, 70, tetra3], [2, 62, tetra2], [1, 54.5, None] ]),
 elem("O",  "Oxygen",     26.565,  1.74, [0.6, 0.2, 0.2],
      [[2, 66, oxy2], [1, 55, None]]),
 elem("F",  "Fluorine",   31.545,  1.65, [0.0, 0.8, 0.34],
      [[1, 64, None]]),
 elem("Ne", "Neon",       33.49,   1.82, [0.92, 0.25, 0.62],
      None),
 elem("Na", "Sodium",     38.1726, 4.0,  [0.0, 0.4, 0.4],
      [[1, 186, None]]),
 elem("Mg", "Magnesium",  40.356,  3.0,  [0.88, 0.6, 0.9],
      [[2, 160, None]]),
 elem("Al", "Aluminum",   44.7997, 2.5,  [0.5, 0.5, 0.9],
      [[3, 143, flat]]),
 elem("Si", "Silicon",    46.6245, 2.25, [0.2, 0.2, 0.2],
      [[4, 117, tetra4]]),
 elem("P",  "Phosphorus", 51.429,  2.11, [0.73, 0.32, 0.87],
      [[3, 110, tetra3]]),
 elem("S",  "Sulfur",     53.233,  2.11, [1.0, 0.65, 0.0],
      [[2, 104, tetra2]]),
 elem("Cl", "Chlorine",   58.867,  2.03, [0.34, 0.68, 0.0],
      [[1, 99, None]]),
 elem("Ar", "Argon",      66.33,   1.88, [0.85, 0.24, 0.57],
      None),
 # not used after this
 elem("K",  "Potassium",  64.9256, 5.0,  [0.0, 0.3, 0.3],
      [[1, 231, None]]),
 elem("Ca", "Calcium",    66.5495, 4.0,  [0.79, 0.55, 0.8],
      [[2, 197, tetra2]]),
 elem("Sc", "Scandium",   74.646,  3.7,  [0.417, 0.417, 0.511],
      [[3, 160, tetra3]]),
 elem("Ti", "Titanium",   79.534,  3.5,  [0.417, 0.417, 0.511],
      [[4, 147, tetra4]]),
 elem("V",  "Vanadium",   84.584,  3.3,  [0.417, 0.417, 0.511],
      [[5, 132, None]]),
 elem("Cr", "Chromium",   86.335,  3.1,  [0.417, 0.417, 0.511],
      [[6, 125, None]]),
 elem("Mn", "Manganese",  91.22,   3.0,  [0.417, 0.417, 0.511],
      [[7, 112, None]]),
 elem("Fe", "Iron",       92.729,  3.0,  [0.417, 0.417, 0.511],
      [[3, 124, None]]),
 elem("Co", "Cobalt",     97.854,  3.0,  [0.417, 0.417, 0.511],
      [[3, 125, None]]),
 elem("Ni", "Nickel",     97.483,  3.0,  [0.417, 0.417, 0.511],
      [[3, 125, None]]),
 elem("Cu", "Copper",    105.513,  3.0,  [0.417, 0.417, 0.511],
      [[2, 128, None]]),
 elem("Zn", "Zinc",      108.541,  2.9,  [0.417, 0.417, 0.511],
      [[2, 133, None]]),
 elem("Ga", "Gallium",   115.764,  2.7,  [0.6, 0.6, 0.8],
      [[3, 135, None]]),
 elem("Ge", "Germanium", 120.53,   2.5,  [0.447, 0.49, 0.416],
      [[4, 122, tetra4]]),
 elem("As", "Arsenic",   124.401,  2.2,  [0.6, 0.26, 0.7],
      [[5, 119, tetra3]]),
 elem("Se", "Selenium",  131.106,  2.1,  [0.9, 0.35, 0.0],
      [[6, 120, tetra2]]),
 elem("Br", "Bromine",   132.674,  2.0,  [0.0, 0.5, 0.0],
      [[1, 119, None]]),
 elem("Kr", "Krypton",   134.429,  1.9,  [0.78, 0.21, 0.53],
      None)]

# note mass is in e-27 kg, not amu

# the elements, indexed by symbol (H, C, O ...)
PeriodicTable={}
for el in Mendeleev:
    PeriodicTable[el.symbol] = el

Hydrogen = PeriodicTable["H"]
Carbon = PeriodicTable["C"]
Nitrogen = PeriodicTable["N"]
Oxygen = PeriodicTable["O"]

Singlet = PeriodicTable["X"]


# the elements, indexed by name (Hydrogen, Carbon ...)
fullnamePeriodicTable={}

for el in Mendeleev:
    fullnamePeriodicTable[el.name] = el

class atom:
    def __init__(self, sym, where, mol):
        """create an atom of element sym (e.g. 'C')
        at location where (e.g. V(36, 24, 36))
        belonging to molecule mol, which is part of assembly assy
        """
        # unique key for hashing
        self.key = atKey.next()
        # element-type object
        self.element=PeriodicTable[sym]
        # location, which will be set relative to its molecule's center
        self.xyz=where
        # list of bond objects
        self.bonds=[]
        # whether the atom is selected, see also assembly.selatoms
        self.picked = 0
        # can be set to override molecule or global value
        self.display = diDEFAULT
        # pointer to molecule containing this atom
        self.molecule=mol
        self.molecule.atoms[self.key] = self

        # note that the assembly is not explicitly stored

    def posn(self):
        """return the absolute position of the atom in space,
        by calculating rotation and translation offset from molecule
        """
        if self.xyz != 'no':
            return self.xyz
        else:
            return self.molecule.curpos[self.index]

    def __repr__(self):
        return self.element.symbol + str(self.key)

    def __str__(self):
        return self.element.symbol + str(self.key)

    def prin(self):
        """for debugging
        """
        lis = map((lambda b: b.other(self).element.symbol), self.bonds)
        print self.element.name, lis

    def draw(self, win, dispdef, col, level):
        """draw the atom depending on whether it is picked
        and its (possibly inherited) display mode
        An atom's display mode overrides the inherited one from
        the molecule, but a molecule's color overrides the atom's
        element-dependent one
        """
        color = col or self.element.color
        disp, rad = self.howdraw(dispdef)
        # note use of basepos since it's being drawn under
        # rotation/translation of molecule
        pos = self.molecule.basepos[self.index]
        if disp in [diVDW, diCPK]:
            drawsphere(color, pos, rad, level)
        rad *= 1.1
        if disp == diTUBES:
            if len(self.bonds)<4:
                if self == win.singlet:
                    drawsphere(LEDon, pos, rad, level)
                else:
                    drawsphere(color, pos, rad, level)
            rad *= 1.8
        if self.picked:
            drawwiresphere(PickedColor, pos, rad)

    def setDisplay(self, disp):
        self.display = disp
        self.molecule.changeapp()
        

    def howdraw(self, dispdef):
        """ tell how to draw the atom depending
        its (possibly inherited) display mode
        An atom's display mode overrides the inherited one from
        the molecule, but a molecule's color overrides the atom's
        element-dependent one
        return that and radius to use in a tuple
        """
        if self.display == diDEFAULT: disp=dispdef
        else: disp=self.display
        rad = self.element.rvdw
        if disp != diVDW: rad=rad*CPKvdW
        if disp == diTUBES: rad = TubeRadius
        
        return (disp, rad)

    def povwrite(self, file, dispdef, col):
        color = col or self.element.color
        color = color * V(1,1,-1)
        disp, rad = self.howdraw(dispdef)
        if disp in [diVDW, diCPK]:
            file.write("atom(" + povpoint(self.posn()) +
                       "," + str(rad) + "," +
                       povpoint(color) + ")\n")


    def checkpick(self, p1, v1, r=None, iPic=None):
        """check if the line through point p1 in direction v1
        goes through the atom (defined as a sphere 70% its vdW radius)
        This is a royal kludge, needs to be replaced by something
        that uses the screen representation
        """
        if self.element == Singlet: return None
        if not r: r=self.element.rvdw*0.7
        if self.picked and not iPic: return None
        dist, wid = orthodist(p1, v1, self.posn())
        if wid > r: return None
        if dist<0: return None
        return dist

    def pick(self):
        """make the atom selected
        """
        if self.element == Singlet: return
        if not self.picked:
            self.picked = 1
            self.molecule.assy.selatoms[self.key] = self
            self.molecule.changeapp()

    def unpick(self):
        """make the atom unselected
        """
        if self.element == Singlet: return
        if self.picked:
            self.picked = 0
            del self.molecule.assy.selatoms[self.key]
            self.molecule.changeapp()

    def copy(self, numol):
        """create a copy of the atom
        (to go in numol, a copy of its molecule)
        """
        nuat = atom(self.element.symbol, 'no', numol)
        nuat.index = self.index
        return nuat

    def unbond(self, b):
        """remove bond b from the atom.
        called from atom.kill of the other atom.
        """
        # the caller needs to do a shakedown
        self.bonds.remove(b)
        if self.element == Singlet: return
        x = atom('X', b.ubp(self), self.molecule)
        self.molecule.bond(self, x)

    def hopmol(self, numol):
        """move this atom to molecule numol
        """
        if self.molecule == numol: return
        nxyz = self.posn()
        del self.molecule.atoms[self.key]
        self.xyz = nxyz
        self.molecule = numol
        numol.atoms[self.key] = self
        for a in self.neighbors():
            if a.element == Singlet:
                a.hopmol(numol)
        # both molecules change!
        self.molecule.changeapp()
        numol.changeapp()

    def neighbors(self):
        """return a list of the atoms bonded to this one
        """
        return map((lambda b: b.other(self)), self.bonds)

    def mvElement(self, elt):
        """Change the element type of this atom to element elname
        (e.g. 'Oxygen')
        """
        self.element = elt
        for b in self.bonds: b.setup()            
        self.molecule.changeapp()

    def kill(self):
        """kill an atom: remove it from molecule.atoms,
        and remove bonds to it from its neighbors
        """
        try: del self.molecule.atoms[self.key]
        except KeyError: pass
        for b in self.bonds:
            n = b.other(self)
            n.unbond(b)
            if n.element == Singlet: n.kill()
            
        # may have changed appearance of the molecule ;-)
        self.molecule.shakedown()

    def Hydrogenate(self):
        """ if this is a singlet, change it to a hydrogen
        """
        if not self.element == Singlet: return
        o = self.bonds[0].other(self)
        self.mvElement(Hydrogen)
        self.molecule.basepos[self.index] += Hydrogen.rcovalent * norm(self.molecule.basepos[self.index] - o.molecule.basepos[o.index])

class bondtype:
    """not implemented
    """
    pass
    # int at1, at2;    /* types of the elements */
    # num r0,ks;           /* bond length and stiffness */
    # num ediss;           /* dissociation (breaking) energy */
    # int order;            /* 1 single, 2 double, 3 triple */
    # num length;          // bond length from nucleus to nucleus
    # num angrad1, aks1;        // angular radius and stiffness for at1
    # num angrad2, aks2;        // angular radius and stiffness for at2

class bond:
    """essentially a record pointing to two atoms
    """
    
    def __init__(self, at1, at2):
        """create a bond from atom at1 to atom at2.
        the key created will be the same whichever order the atoms are
        given, and is used to compare bonds.
        """
        self.atom1 = at1
        self.atom2 = at2
        self.picked = 0
        self.key = 65536*min(at1.key,at2.key)+max(at1.key,at2.key)

    def setup(self):
        self.a1pos = self.atom1.molecule.basepos[self.atom1.index]
        self.a2pos = self.atom2.molecule.basepos[self.atom2.index]
        if self.atom1.molecule != self.atom2.molecule:
            self.a1pos = self.atom1.posn()
            self.a2pos = self.atom2.posn()

        vec = self.a2pos - self.a1pos
        len = 0.98 * vlen(vec)
        vec = norm(vec)
        self.c1 = self.a1pos + vec*self.atom1.element.rcovalent
        self.c2 = self.a2pos - vec*self.atom2.element.rcovalent
        if len > self.atom1.element.rcovalent + self.atom2.element.rcovalent:
            self.center = None
        else:
            self.center = (self.c1 + self.c2) /2.0

    def other(self, at):
        """Given one atom the bond is connected to, return the other one
        """
        if self.atom1 == at: return self.atom2
        return self.atom1
    
    def ubp(self, atom):
        """ unbond point """
        if self.atom1.molecule != self.atom2.molecule:
            off = V(0,0,0)
        else: off = atom.molecule.center
        if atom==self.atom1: return self.c1 + off
        else: return self.c2 + off

    # "break" is a python keyword
    def bust(self):
        self.atom1.unbond(self)
        self.atom2.unbond(self)
        self.atom1.molecule.shakedown()
        if self.atom1.molecule != self.atom2.molecule:
            self.atom2.molecule.shakedown()

    def rebond(self, old, new):
        if self.atom1 == old: self.atom1 = new
        if self.atom2 == old: self.atom2 = new
        self.__init__(self.atom1, self.atom2)
        

    def __eq__(self, ob):
        return ob.key == self.key

    def draw(self, win, dispdef, col, level):
        """bonds are drawn in CPK or line display mode.
        display mode is inherited from the atoms or molecule.
        lines change color from atom to atom.
        CPK bonds are drawn in the molecule's color or bondColor
        (which is light gray)
        """
        color1 = col or self.atom1.element.color
        color2 = col or self.atom2.element.color

        disp=max(self.atom1.display, self.atom2.display)
        if disp == diDEFAULT: disp= dispdef
        if disp == diLINES:
            if self.center:
                drawline(color1, self.a1pos, self.center)
                drawline(color2, self.a2pos, self.center)
            else:
                drawline(color1, self.a1pos, self.c1)
                drawline(color2, self.a2pos, self.c2)
                drawline(red, self.c1, self.c2)
        if disp == diCPK:
            drawcylinder(col or bondColor, self.a1pos, self.a2pos,
                         0.1, self.picked)
        if disp == diTUBES:
            v1 = self.atom1.display != diINVISIBLE
            v2 = self.atom2.display != diINVISIBLE
            if self.center:
                if v1:
                    drawcylinder(color1, self.a1pos, self.center, TubeRadius)
                if v2:
                    drawcylinder(color2, self.a2pos, self.center, TubeRadius)
                if not (v1 and v2):
                    drawsphere(black, self.center, TubeRadius, level)
            else:
                drawcylinder(red, self.c1, self.c2, TubeRadius)
                if v1:
                    drawcylinder(color1, self.a1pos, self.c1, TubeRadius)
                else:
                    drawsphere(black, self.c1, TubeRadius, level)
                if v2:
                    drawcylinder(color2, self.a2pos, self.c2, TubeRadius)
                else:
                    drawsphere(black, self.c2, TubeRadius, level)

    def povwrite(self, file, dispdef, col):
        disp=max(self.atom1.display, self.atom2.display)
        
        if disp<0: disp= dispdef
        if disp == diLINES:
            file.write("line(" + povpoint(self.atom1.posn()) +
                       "," + povpoint(self.atom2.posn()) + ")\n")
        if disp == diCPK:
            file.write("bond(" + povpoint(self.atom1.posn()) +
                       "," + povpoint(self.atom2.posn()) + ")\n")


# I use "molecule" and "part" interchangeably throughout the program.
# this is the class intended to represent rigid collections of
# atoms bonded together, but it's quite possible to make a molecule
# object with unbonded atoms, and with bonds to atoms in other
# molecules
class molecule:
    def __init__(self, assembly, nam=None):
        self.assy = assembly
        # name doesn't get used yet, except as a comment
        # in mmp file output, but could be used to name
        # separate molecule files
        if nam: self.name = nam
        else: self.name = gensym("Part")
        # atoms in a dictionary, indexed by atom.key
        self.atoms = {}
        # motors, grounds
        self.gadgets = []
        # center and bounding box of the molecule
        self.center=V(0,0,0)
        # this overrides global display (GLPane.display)
        # but is overriden by atom value if not default
        self.display = diDEFAULT
        # this set and the molecule in assembly.selmols
        # must remain consistent
        self.picked=0
        # this specifies the molecule's attitude in space
        self.quat = Q(1, 0, 0, 0)
        # this overrides atom colors if set
        self.color = None
        # for caching the display as a GL call list
        self.displist = glGenLists(1)
        self.havelist = 0

    def bond(self, at1, at2):
        """Cause atom at1 to be bonded to at2
        """
        b=bond(at1,at2)
        if not b in at2.bonds:
            at1.bonds += [b]
            at2.bonds += [b]
        # may have changed appearance of the molecule
        self.havelist = 0

    def shakedown(self):
        """Find center and bounding box for atoms, and set each one's
        xyz to be relative to the center and find principal axes
        """
        if not self.atoms:
            self.bbox = BBox()
            self.center = V(0,0,0)
            self.quat = Q(1,0,0,0)
            self.axis = V(1,0,0)
            self.basepos = self.curpos = []
            return
        atpos = []
        singlets = []
        singlpos = []
        for a,i in zip(self.atoms.values(),range(len(self.atoms))):
            pos = a.posn()
            atpos += [pos]
            a.index = i
            a.xyz = 'no'
            if a.element == Singlet:
                 singlets += [a]
                 singlpos += [pos]
        atpos = A(atpos)
        

        self.bbox = BBox(atpos)
        self.center = add.reduce(atpos)/len(self.atoms)
        self.quat = Q(1,0,0,0)  # since all atoms are in place 

        # make the positions relative to the center
        self.basepos = atpos-self.center
        self.curpos = atpos
        self.singlets = array(singlets, PyObject)
        self.singlpos = array(singlpos)
        self.singlbase = self.singlpos

##         # find extrema in many directions
##         xtab = dot(atpos, ddhhXmat)
##         mins = minimum.reduce(xtab) - 1.0
##         maxs = maximum.reduce(xtab) + 1.0
        
##         self.ddhh = cat(maxs,mins)

        # and compute inertia tensor
        tensor = zeros((3,3),Float)
        for p in self.basepos:
            rsq = dot(p, p)
            m= - multiply.outer(p, p)
            m[0,0] += rsq
            m[1,1] += rsq
            m[2,2] += rsq
            tensor += m
        self.eval, self.evec = eigenvectors(tensor)

        # find a tight bounding box, not necessarily square to space,
        # for drawing the pick box
        bv = transpose(self.evec)
        pts = dot(self.basepos, bv)
        
        bbhi = maximum.reduce(pts) + 1.0
        bblo = minimum.reduce(pts) - 1.0
        c = (bbhi+bblo)/2.0

        self.bbLines = dot(cubeLines*(bbhi-c) + c, self.evec)
      
        # Pick a principal axis: if square or circular, the axle;
        # otherwise the long axis (this is a heuristic)
        if len(atpos)<=1:
            self.axis = V(1,0,0)
        elif len(atpos) == 2:
            self.axis = norm(subtract.reduce(atpos))
        else:
            ug = argsort(self.eval)
            if self.eval[ug[0]]/self.eval[ug[1]] >0.95:
                self.axis = self.evec[ug[2]]
            else: self.axis = self.evec[ug[0]]
            
        # may have changed appearance of the molecule

        drawn = {}

        self.externs = []

        for atm in self.atoms.itervalues():
            for bon in atm.bonds:
                if bon.key not in drawn:
                    if bon.other(atm).molecule != self:
                        self.externs += [bon]
                    else:
                        drawn[bon.key] = bon
                    bon.setup()

        self.havelist = 0

    def freeze(self):
        """ set the molecule up for minimization or simulation"""
        self.center = V(0,0,0)
        self.quat = Q(1,0,0,0)  
        self.basepos = self.curpos # reference == same object
        self.singlbase = self.singlpos # ditto

    def unfreeze(self):
        """ to be done at the end of minimization or simulation"""
        self.shakedown()


    def draw(self, o, level):
        """draw all the atoms, using the atom's, molecule's,
        or GLPane's display mode in that order of preference
        Use the hash table drawn to draw each bond only once,
        as each one will be referenced from two atoms
        If the molecule itself is selected, draw its
        bounding box as a wireframe
        o is a GLPane
        """

        # put it in its place
        glPushMatrix()

        glTranslatef(self.center[0], self.center[1], self.center[2])
        
        q = self.quat
        glRotatef(q.angle*180.0/pi, q.x, q.y, q.z)

        if self.picked:
            drawlinelist(PickedColor, self.bbLines)
            #drawddhh(red,self.ddhh)

        if self.display != diDEFAULT: disp = self.display
        else: disp = o.display

        # cache molecule display as GL list
        if self.havelist:
            glCallList(self.displist)

        else:
            glNewList(self.displist, GL_COMPILE_AND_EXECUTE)

            drawn = {}

            self.externs = []

            for atm in self.atoms.itervalues():
                atm.draw(o, disp, self.color, level)
                for bon in atm.bonds:
                    if bon.key not in drawn:
                        if bon.other(atm).molecule != self:
                            self.externs += [bon]
                        else:
                            drawn[bon.key] = bon
                            bon.draw(o, disp, self.color, level)


            for g in self.gadgets:
                g.draw(o, disp)

            glEndList()
            self.havelist = 1
        glPopMatrix()

        for bon in self.externs:
            bon.draw(o, disp, self.color, level)

    # write a povray file: just draw everything inside
    def povwrite(self,file, win):

        if self.display != diDEFAULT: disp = self.display
        else: disp = win.display
        
        drawn = {}
        for atm in self.atoms.itervalues():
            atm.povwrite(file, disp, self.color)
            for bon in atm.bonds:
                if bon.key not in drawn:
                    drawn[bon.key] = bon
                    bon.povwrite(file, disp, self.color)

        for g in self.gadgets:
            g.povwrite(file, disp)

    def move(self, offs):
        self.center += offs
        self.curpos = self.center + self.quat.rot(self.basepos)
        if self.singlets:
            self.singlpos = self.center + self.quat.rot(self.singlbase)
        for bon in self.externs: bon.setup()

    def rot(self, q):
        self.quat += q
        self.curpos = self.center + self.quat.rot(self.basepos)
        if self.singlets:
            self.singlpos = self.center + self.quat.rot(self.singlbase)
        for bon in self.externs: bon.setup()

    def stretch(self, factor):
        self.basepos *= 1.1
        self.curpos = self.center + self.quat.rot(self.basepos)
        if self.singlets:
            self.singlpos = self.center + self.quat.rot(self.singlbase)
        for bon in self.externs: bon.setup()
        self.changeapp()


    def getaxis(self):
        return self.quat.rot(self.axis)

    def setcolor(self, color):
        """change the molecule's color
        """
        self.color = color
        self.havelist = 0

    def setDisplay(self, disp):
        self.display = disp
        self.havelist = 0
        
    def changeapp(self):
        """call when you've changed appearance of the molecule
        """ 
        self.havelist = 0
    
    def pick(self):
        """select the molecule.
        """
        if not self.picked:
            self.picked = 1
            self.assy.selmols.append(self)
            # may have changed appearance of the molecule
            self.havelist = 0

    def unpick(self):
        """unselect the molecule.
        """
        if self.picked:
            self.picked = 0
            self.assy.selmols.remove(self)
            # may have changed appearance of the molecule
            self.havelist = 0

    # point is some point on the line of sight
    # matrix is a rotation matrix with z along the line of sight,
    # positive z out of the plane
    # return positive points only, sorted by distance
    def findSinglets(self, point, matrix, radius, cutoff):
        if not self.singlets: return None
        v = dot(self.singlpos-point,matrix)
        r = sqrt(v[:,0]**2 + v[:,1]**2)
        i = argmax(v[:,2] - 100000.0*(r>radius))
        if r[i]>radius: return None
        if v[i,2]<cutoff: return None
        return self.singlets[i]

    # return the singlets in the given sphere
    # sorted by increasing distance from the center
    def nearSinglets(self, point, radius):
        if not self.singlets: return None
        v = self.singlpos-point
        r = sqrt(v[:,0]**2 + v[:,1]**2 + v[:,2]**2)
        p= r<=radius
        i=argsort(compress(p,r))
        return take(compress(p,self.singlets),i)

    def copy(self, offset):
        """Copy the molecule to a new molecule.
        offset tells where it will go relative to the original.
        There should be a rotation parameter but there isn't.
        note the assembly must be passed in.
        """
        pairlis = []
        ndix = {}
        numol = molecule(self.assy, gensym(self.name))
        for a in self.atoms.itervalues():
            na = a.copy(numol)
            pairlis += [(a, na)]
            ndix[a.key] = na
        for (a, na) in pairlis:
            for b in a.bonds:
                if b.other(a).key in ndix:
                    numol.bond(na,ndix[b.other(a).key])
        numol.curpos =self.curpos+offset
        numol.shakedown()
        numol.setDisplay(self.display)
        self.unpick()
        numol.pick()
        return numol

    def passivate(self):
        """kludgey hack: change carbons with 3 neighbors to nitrogen,
        with 2 neighbors to oxygen, with 1 to hydrogen, and
        delete unbonded ones.
        """
        for a in self.atoms.values():
            if a.element == Carbon:
                valence = len(a.bonds)
                if valence == 0: a.kill()
                elif valence == 1: a.element = Hydrogen
                elif valence == 2: a.element = Oxygen
                elif valence == 3: a.element = Nitrogen
        # will have changed appearance of the molecule
        self.havelist = 0

    def Hydrogenate(self):
        """Add hydrogen to all unfilled bond sites on carbon
        atoms assuming they are in a diamond lattice.
        For hilariously incorrect results, use on graphite.
        This ought to be an atom method.
        """
        # will change appearance of the molecule
        self.havelist = 0
        for a in self.atoms.values():
            a.Hydrogenate()


    def __str__(self):
        return "<Molecule of " + self.name + ">"

def oneUnbonded(elem, assy, pos):
    mol = molecule(assy, gensym('Clicked'))
    a = atom(elem.symbol, pos, mol)
    r = elem.rcovalent
    if elem.bonds and elem.bonds[0][2]:
        for dp in elem.bonds[0][2]:
            x = atom('X', pos+r*dp, mol)
            mol.bond(a,x)
    assy.addmol(mol)

    return mol
    
                     
# this code knows where to place missing bonds in carbon
# sure to be used later

        
##         # length of Carbon-Hydrogen bond
##         lCHb = (Carbon.bonds[0][1] + Hydrogen.bonds[0][1]) / 100.0
##         for a in self.atoms.values():
##             if a.element == Carbon:
##                 valence = len(a.bonds)
##                 # lone atom, pick 4 directions arbitrarily
##                 if valence == 0:
##                     b=atom("H", a.xyz+lCHb*norm(V(-1,-1,-1)), self)
##                     c=atom("H", a.xyz+lCHb*norm(V(1,-1,1)), self)
##                     d=atom("H", a.xyz+lCHb*norm(V(1,1,-1)), self)
##                     e=atom("H", a.xyz+lCHb*norm(V(-1,1,1)), self)
##                     self.bond(a,b)
##                     self.bond(a,c)
##                     self.bond(a,d)
##                     self.bond(a,e)

##                 # pick an arbitrary tripod, and rotate it to
##                 # center away from the one bond
##                 elif valence == 1:
##                     bpos = lCHb*norm(V(-1,-1,-1))
##                     cpos = lCHb*norm(V(1,-1,1))
##                     dpos = lCHb*norm(V(1,1,-1))
##                     epos = V(-1,1,1)
##                     q1 = Q(epos, a.bonds[0].other(a).xyz - a.xyz)
##                     b=atom("H", a.xyz+q1.rot(bpos), self)
##                     c=atom("H", a.xyz+q1.rot(cpos), self)
##                     d=atom("H", a.xyz+q1.rot(dpos), self)
##                     self.bond(a,b)
##                     self.bond(a,c)
##                     self.bond(a,d)

##                 # for two bonds, the new ones can be constructed
##                 # as linear combinations of their sum and cross product
##                 elif valence == 2:
##                     b=a.bonds[0].other(a).xyz - a.xyz
##                     c=a.bonds[1].other(a).xyz - a.xyz
##                     v1 = - norm(b+c)
##                     v2 = norm(cross(b,c))
##                     bpos = lCHb*(v1 + sqrt(2)*v2)/sqrt(3)
##                     cpos = lCHb*(v1 - sqrt(2)*v2)/sqrt(3)
##                     b=atom("H", a.xyz+bpos, self)
##                     c=atom("H", a.xyz+cpos, self)
##                     self.bond(a,b)
##                     self.bond(a,c)

##                 # given 3, the last one is opposite their average
##                 elif valence == 3:
##                     b=a.bonds[0].other(a).xyz - a.xyz
##                     c=a.bonds[1].other(a).xyz - a.xyz
##                     d=a.bonds[2].other(a).xyz - a.xyz
##                     v = - norm(b+c+d)
##                     b=atom("H", a.xyz+lCHb*v, self)
##                     self.bond(a,b)

