# Copyright (c) 2004-2005 Nanorex, Inc.  All rights reserved.
"""
whatsthis.py

$Id$
"""

from qt import *

###@@@ bruce 051227 experimental code for putting hyperlinks into selected WhatsThis texts

enable_whatsthis_links = False # DO NOT COMMIT with True (since incomplete), but keep the code (might be used for A7)

class MyWhatsThis(QWhatsThis):
    def __init__(self, widget, text = None):
        QWhatsThis.__init__(self, widget)
        self.__text = text # note: using QString(text) here is ok but not required
    def text(self, pos):
        # this runs when Qt puts up a WhatsThis help window for widget
        print "text at pos %r in %r was queried by Qt" % (pos, self) # note: pos repr is not useful, doesn't show x,y
        text = self.__text
        if not text:
            print " no text" # never happens in current calling code [051227]
        return text
    def clicked(self, link):
        # this runs when user clicks on a hyperlink in the help text, with 'link' being the link text (href attribute)
        link = str(link) # QString to string (don't know if this is needed, guess yes)
        if link:
            print "clicked hyperlink in %r, href text is %r" % (self,link)
            ##e revise this to change link text to URL if it's not already, and open browser to help page (see wiki_help.py)
        else:
            print "clicked non-link in %r" % self # happens for clicking any empty part or other text in that popup dialog
        return True ## return True to make help text widget go away, or False to keep it around (with no change in contents)
    pass

    ## note: doesn't work on QActions (at least for an earlier version of the class with no __init__ method):
    ## MyWhatsThis(self.editCopyAction) ## TypeError: argument 1 of QWhatsThis() has an invalid type

###@@@ end bruce 051227 experimental code [but there's more, far below]


def createWhatsThis(self):
        
        ##############################################
        # File Toolbar
        ##############################################
        
        #### Open File ####
        
        fileOpenText = "<u><b>Open File</b></u>    (Ctrl + O)</b></p><br> "\
                        "<p><img source=\"fileopen\"><br> "\
                       "Opens a new file."\
                       "</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "fileopen",
                                                       self.fileOpenAction.iconSet().pixmap() )

        self.fileOpenAction.setWhatsThis( fileOpenText )
        
        #### Save File ####
        
        fileSaveText = "<u><b>Save File</b></u>     (Ctrl + S)</b></p><br> "\
                       "<p><img source=\"filesave\"><br> "\
                       "Saves the current file."\
                       "</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "filesave",
                                                       self.fileSaveAction.iconSet().pixmap() )

        self.fileSaveAction.setWhatsThis( fileSaveText )
        
        ##############################################
        # Edit Toolbar
        ##############################################
        
        #### Undo ####
        
        editUndoText =  "<u><b>Undo</b></u>     (Ctrl + Z)</b></p><br> "\
                       "<p><img source=\"editUndo\"><br> "\
                       "Reverses the last edit or command to the active part. "\
                       "<b>Currently not implemented</b>."\
                       "</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "editUndo",
                                                       self.editUndoAction.iconSet().pixmap() )

        self.editUndoAction.setWhatsThis( editUndoText )
        
        #### Redo ####
        
        editRedoText =  "<u><b>Redo</b></u>     (Ctrl + Y)</b></p><br> "\
                       "<p><img source=\"editRedo\"> <br>"\
                       "Re-applies the actions or commands on which you have used "\
                       "the Undo command. <b>Currently not implemented</b>."\
                       "</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "editRedo",
                                                       self.editRedoAction.iconSet().pixmap() )

        self.editRedoAction.setWhatsThis( editRedoText )
        
        #### Cut ####
        
        editCutText =  "<u><b>Cut</b></u>     (Ctrl + X)</b></p><br> "\
                       "<p><img source=\"editCut\"><br> "\
                       "Removes the selected object(s) and stores the cut data on the"\
                       "clipboard."\
                       "</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "editCut",
                                                       self.editCutAction.iconSet().pixmap() )

        self.editCutAction.setWhatsThis( editCutText )
        
        #### Copy ####
        
        editCopyText =  "<u><b>Copy</b></u>     (Ctrl + C)</b></p><br> "\
                       "<p><img source=\"editCopy\"><br> "\
                      "Places a copy of the selected chunk(s) on the clipboard "\
                      "while leaving the original chunk(s) unaffected."\
                      "</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "editCopy",
                                                       self.editCopyAction.iconSet().pixmap() )

        self.editCopyAction.setWhatsThis( editCopyText )
        
        #### Paste ####
        
        editPasteText = "<u><b>Paste</b></u>     (Ctrl + V)</b></p><br> "\
                       "<p><img source=\"editPaste\"><br> "\
                       "When selecting this feature, you are placed in "\
                       "<b>Build Atom</b> mode where you may paste copies "\
                       "of clipboard objects into the model where ever you click."\
                       "</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "editPaste",
                                                       self.editPasteAction.iconSet().pixmap() )

        self.editPasteAction.setWhatsThis( editPasteText )
   
        #### Delete ####
                                 
        editDeleteText =  "<u><b>Delete</b></u>     (DEL)</b></p><br> "\
                       "<p><img source=\"editDelete\"><br> "\
                       "Deletes the selected object(s).  "\
                       "For this Alpha release, deleted objects are permanantly lost.</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "editDelete",
                                                       self.editDeleteAction.iconSet().pixmap() )

        self.editDeleteAction.setWhatsThis( editDeleteText )
        
        ##############################################
        # View Toolbar
        ##############################################
        
        #### Home View ####
        
        setViewHomeActionText = "<u><b>Home</b></u>     (Home)<br>"\
                       "<p><img source=\"setViewHome\"><br> "\
                       "When you create a new model, it appears in a default view orientation (FRONT view). When you open an existing model, it appears in the orientation it was last saved.  You can change the default orientation by selecting <b>Set Home View to Current View</b> from the <b>View</b> menu.</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "setViewHome",
                                                       self.setViewHomeAction.iconSet().pixmap() )

        self.setViewHomeAction.setWhatsThis( setViewHomeActionText )

        #### Fit to Window ####
        
        setViewFitToWindowActionText = "<u><b>Fit To Window</b></u><br>"\
                       "<p><img source=\"setViewFitToWindow\"><br> "\
                       "Refits the model to the screen so you can view the entire model."\
                       "</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "setViewFitToWindow",
                                                       self.setViewFitToWindowAction.iconSet().pixmap() )

        self.setViewFitToWindowAction.setWhatsThis( setViewFitToWindowActionText )   

        #### Recenter ####
        
        setViewRecenterActionText = "<u><b>Recenter</b></u><br>"\
                       "<p><img source=\"setViewRecenter\"><br> "\
                       "Changes the view center and zoom factor so that the origin is in the "\
                       "center of the view and you can view the entire model."\
                       "</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "setViewRecenter",
                                                       self.setViewRecenterAction.iconSet().pixmap() )

        self.setViewRecenterAction.setWhatsThis( setViewRecenterActionText )       
        
        #### Zoom Tool ####
        
        setzoomToolActionText = "<u><b>Zoom Tool</b></u><br>"\
                       "<p><img source=\"setzoomTool\"><br> "\
                       "Allows the user to zoom into a specific area of the model by specifying a rectangular area. "\
                       "This is done by holding down the left button and dragging the mouse.</p>"\
                       "<p>A mouse with a mouse wheel can also be used to zoom in and out "\
                       "at any time, without using the Zoom Tool.</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "setzoomTool",
                                                       self.zoomToolAction.iconSet().pixmap() )

        self.zoomToolAction.setWhatsThis( setzoomToolActionText )      

        
        #### Pan Tool ####
        
        setpanToolActionText = "<u><b>Pan Tool</b></u><br>"\
                       "<p><img source=\"setpanTool\"><br> "\
                       "Allows X-Y panning using the left mouse button.</p>"\
                       "<p>Users with a 3-button mouse can pan the model at any time by pressing "\
                       "the middle mouse button while holding down the Shift key.</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "setpanTool",
                                                       self.panToolAction.iconSet().pixmap() )

        self.panToolAction.setWhatsThis( setpanToolActionText )

        
        #### Rotate Tool ####
        
        setrotateToolActionText = "<u><b>Rotate Tool</b></u><br>"\
                       "<p><img source=\"setrotateTool\"><br> "\
                       "Allows free rotation using the left mouse button.</p>"\
                       "<p>Users with a 3-button mouse can rotate the model at any time by pressing "\
                       "the middle mouse button and dragging the mouse.</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "setrotateTool",
                                                       self.rotateToolAction.iconSet().pixmap() )

        self.rotateToolAction.setWhatsThis( setrotateToolActionText )
        
        #### Orthographic Projection ####
        
        setViewOrthoActionText = "<u><b>Orthographic Projection</b></u><br>"\
                       "<p><img source=\"setViewOrtho\"><br> "\
                       "Sets nonperspective (or parallel) projection, with no foreshortening."\
                       "</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "setViewOrtho",
                                                       self.setViewOrthoAction.iconSet().pixmap() )

        self.setViewOrthoAction.setWhatsThis( setViewOrthoActionText )

        #### Perspective Projection ####
        
        setViewPerspecActionText = "<u><b>Perspective Projection</b></u><br>"\
                       "<p><img source=\"setViewPerspec\"><br> "\
                       "Set perspective projection, drawing objects slightly larger "\
                       "that are closer to the viewer."\
                       "</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "setViewPerspec",
                                                       self.setViewPerspecAction.iconSet().pixmap() )

        self.setViewPerspecAction.setWhatsThis( setViewPerspecActionText )        

        #### Front View ####
        
        setViewFrontActionText = "<u><b>Front View</b></u><br>"\
                       "<p><img source=\"setViewFront\"><br> "\
                       "Reorients the model so that it is viewed from the front."\
                       "</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "setViewFront",
                                                       self.setViewFrontAction.iconSet().pixmap() )

        self.setViewFrontAction.setWhatsThis( setViewFrontActionText )  

        #### Back View ####
        
        setViewBackActionText = "<u><b>Back View</b></u><br>"\
                       "<p><img source=\"setViewBack\"><br> "\
                       "Reorients the model so that it is viewed from the back."\
                       "</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "setViewBack",
                                                       self.setViewBackAction.iconSet().pixmap() )

        self.setViewBackAction.setWhatsThis( setViewBackActionText )     
        
        #### Top View ####
        
        setViewTopActionText = "<u><b>Top View</b></u><br>"\
                       "<p><img source=\"setViewTop\"><br> "\
                       "Reorients the model so that it is viewed from the top."\
                       "</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "setViewTop",
                                                       self.setViewTopAction.iconSet().pixmap() )

        self.setViewTopAction.setWhatsThis( setViewTopActionText )      
        
        #### Bottom View ####
        
        setViewBottomActionText = "<u><b>Bottom View</b></u><br>"\
                       "<p><img source=\"setViewBottom\"><br> "\
                       "Reorients the model so that it is viewed from the bottom."\
                       "</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "setViewBottom",
                                                       self.setViewBottomAction.iconSet().pixmap() )

        self.setViewBottomAction.setWhatsThis( setViewBottomActionText )  
        
        #### Left View ####
        
        setViewLeftActionText = "<u><b>Left View</b></u><br>"\
                       "<p><img source=\"setViewLeft\"><br> "\
                       "Reorients the model so that it is viewed from the left side."\
                       "</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "setViewLeft",
                                                       self.setViewLeftAction.iconSet().pixmap() )

        self.setViewLeftAction.setWhatsThis( setViewLeftActionText )
        
        #### Right View ####
        
        setViewRightActionText = "<u><b>Right View</b></u><br>"\
                       "<p><img source=\"setViewRight\"><br> "\
                       "Reorients the model so that it is viewed from the right side."\
                       "</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "setViewRight",
                                                       self.setViewRightAction.iconSet().pixmap() )

        self.setViewRightAction.setWhatsThis( setViewRightActionText )
        
        #### Opposite View ####
        
        setViewOppositeActionText = "<u><b>Opposite View</b></u><br>"\
                       "<p><img source=\"setViewOpposite\"><br> "\
                       "Reorients the model so that it is viewed from the opposite side of the current view."\
                       "</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "setViewOpposite",
                                                       self.setViewOppositeAction.iconSet().pixmap() )

        self.setViewOppositeAction.setWhatsThis( setViewOppositeActionText )
        
        ##############################################
        # Grids Toolbar
        ##############################################
        
        #### Surface 100 ####
        
        orient100ActionText = "<u><b>Surface 100</b></u><br>"\
                       "<p><img source=\"orient100Action\"><br> "\
                       "Reorients the view to the nearest angle that would "\
                       "look straight into a (1,0,0) surface of a diamond lattice."\
                       "</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "orient100Action",
                                                       self.orient100Action.iconSet().pixmap() )

        self.orient100Action.setWhatsThis(orient100ActionText )
        
        #### Surface 110 ####
        
        orient110ActionText = "<u><b>Surface 110</b></u><br>"\
                       "<p><img source=\"orient110Action\"><br> "\
                       "Reorients the view to the nearest angle that would "\
                       "look straight into a (1,1,0) surface of a diamond lattice."\
                       "</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "orient110Action",
                                                       self.orient110Action.iconSet().pixmap() )

        self.orient110Action.setWhatsThis(orient110ActionText )
        
        #### Surface 111 ####

        orient111ActionText = "<u><b>Surface 111</b></u><br>"\
                       "<p><img source=\"orient111Action\"><br> "\
                       "Reorients the view to the nearest angle that would "\
                       "look straight into a (1,1,1) surface of a diamond lattice."\
                       "</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "orient111Action",
                                                       self.orient111Action.iconSet().pixmap() )

        self.orient111Action.setWhatsThis(orient111ActionText )
        
        ##############################################
        # Molecular Display toolbar
        ##############################################
        
        #### Display Default  ####

        dispDefaultActionText = "<u><b>Display Default</b></u><br>"\
                       "<p><img source=\"dispDefaultAction\"><br> "\
                       "Changes the <i>display setting</i> of selected atoms or chunks to "\
                       "<b>Default</b> , rendering them in the <b>Current Display Mode</b>."\
                       "</p>"\
                       "<p>If no atoms or chunks are selected, then this action will change the "\
                       "<b>Current Display Mode</b> of the 3D workspace to the <b>Default Display Mode</b>. " \
                       "All chunks with their display setting set to <b>Default</b> will be rendered in the "\
                       "<b>Default Display Mode</b>."\
                       "</p>"\
                       "<p>The <b>Default Display Mode</b> can be changed via the "\
                       "<b>Edit > Preferences</b> menu and selecting the <b>General</b> tab."\
                       "</p>"\
                       "<p>The <b>Current or Default Display Mode</b> is displayed in the status bar in the "\
                       "lower right corner of the main window."\
                       "</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "dispDefaultAction",
                                                       self.dispDefaultAction.iconSet().pixmap() )

        self.dispDefaultAction.setWhatsThis(dispDefaultActionText )
 
        #### Display Invisible ####

        dispInvisActionText = "<u><b>Display Invisible</b></u><br>"\
                       "<p><img source=\"dispInvisAction\"><br> "\
                       "Changes the <i>display setting</i> of selected atoms or chunks to "\
                       "<b>Invisible</b>, making them invisible."\
                       "</p>"\
                       "<p>If no atoms or chunks are selected, then this action will change the "\
                       "<b>Current Display Mode</b> of the 3D workspace to <b>Invisible</b>. " \
                       "All chunks with their display setting set to <b>Default</b> will inherit "\
                       "this display property."\
                       "</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "dispInvisAction",
                                                       self.dispInvisAction.iconSet().pixmap() )

        self.dispInvisAction.setWhatsThis(dispInvisActionText )       

        #### Display Lines ####

        dispLinesActionText = "<u><b>Display Lines</b></u><br>"\
                       "<p><img source=\"dispLinesAction\"><br> "\
                       "Changes the <i>display setting</i> of selected atoms or chunks to "\
                       " <b>Lines</b>.  Only bonds are rendered as colored lines."\
                       "</p>"\
                       "<p>If no atoms or chunks are selected, then this action will change the "\
                       "<b>Current Display Mode</b> of the 3D workspace to <b>Lines</b>. " \
                       "All chunks with their display setting set to <b>Default</b> will inherit "\
                       "this display property."\
                       "</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "dispLinesAction",
                                                       self.dispLinesAction.iconSet().pixmap() )

        self.dispLinesAction.setWhatsThis(dispLinesActionText )  
        
        #### Display Tubes ####

        dispTubesActionText = "<u><b>Display Tubes</b></u><br>"\
                       "<p><img source=\"dispTubesAction\"><br> "\
                       "Changes the <i>display setting</i> of selected atoms or chunks to "\
                       "<b>Tubes</b>.  Atoms and bonds are rendered as colored tubes."\
                       "</p>"\
                       "<p>If no atoms or chunks are selected, then this action will change the "\
                       "<b>Current Display Mode</b> of the 3D workspace to <b>Tubes</b>. " \
                       "All chunks with their display setting set to <b>Default</b> will inherit "\
                       "this display property."\
                       "</p>"


        QMimeSourceFactory.defaultFactory().setPixmap( "dispTubesAction",
                                                       self.dispTubesAction.iconSet().pixmap() )

        self.dispTubesAction.setWhatsThis(dispTubesActionText )  
        
        #### Display CPK ####

        dispCPKActionText = "<u><b>Display CPK</b></u><br>"\
                       "<p><img source=\"dispCPKAction\"><br> "\
                       "Changes the <i>display setting</i> of selected atoms or chunks to "\
                       "<b>CPK</b> mode, also known as <b>\"Ball and Sticks\"</b> mode.  Atoms are rendered "\
                       "as spheres and bonds are rendered as narrow cylinders."\
                       "</p>"\
                       "<p>If no atoms or chunks are selected, then this action will change the "\
                       "<b>Current Display Mode</b> of the 3D workspace to <b>CPK</b>. " \
                       "All chunks with their display setting set to <b>Default</b> will inherit "\
                       "this display property."\
                       "</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "dispCPKAction",
                                                       self.dispCPKAction.iconSet().pixmap() )

        self.dispCPKAction.setWhatsThis(dispCPKActionText ) 
        
        #### Display VdW ####

        dispVdWActionText = "<u><b>Display VdW</b></u><br>"\
                       "<p><img source=\"dispVdWAction\"><br> "\
                       "Changes the <i>display setting</i> of selected atoms or chunks to "\
                       "<b>Van der Waals</b> mode.  Atoms are rendered as spheres with "\
                       "a size equal to the VdW radius.  Bonds are not rendered."\
                       "</p>"\
                       "<p>If no atoms or chunks are selected, then this action will change the "\
                       "<b>Current Display Mode</b> of the 3D workspace to <b>VdW</b>. " \
                       "All chunks with their display setting set to <b>Default</b> will inherit "\
                       "this display property."\
                       "</p>"
                      
        QMimeSourceFactory.defaultFactory().setPixmap( "dispVdWAction",
                                                       self.dispVdWAction.iconSet().pixmap() )

        self.dispVdWAction.setWhatsThis(dispVdWActionText )         
        
        ##############################################
        # Select toolbar
        ##############################################
        
        #### Select All ####

        selectAllActionText = "<u><b>Select All</b></u>     (Ctrl + A)</b></p><br>"\
                       "<p><img source=\"selectAllAction\"><br> "\
                       "During <b>Select Atoms</b> mode, this will select all the atoms in "\
                       "the model.  Otherwise, this will select all the chunks in the model."\
                       "</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "selectAllAction",
                                                       self.selectAllAction.iconSet().pixmap() )

        self.selectAllAction.setWhatsThis(selectAllActionText )
        
        #### Select None ####

        selectNoneActionText = "<u><b>Select None</b></u></p><br>"\
                       "<p><img source=\"selectNoneAction\"><br> "\
                       "Unselects everything currently selected.</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "selectNoneAction",
                                                       self.selectNoneAction.iconSet().pixmap() )

        self.selectNoneAction.setWhatsThis(selectNoneActionText )
 
        #### Invert Selection ####

        selectInvertActionText = "<u><b>Invert Selection</b></u> <br>    (Ctrl + Shift + I)</b></p><br>"\
                       "<p><img source=\"selectInvertAction\"><br> "\
                       "Inverts the current selection.</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "selectInvertAction",
                                                       self.selectInvertAction.iconSet().pixmap() )

        self.selectInvertAction.setWhatsThis(selectInvertActionText )
        
        #### Select Connected ####

        selectConnectedActionText = "<u><b>Select Connected</b></u>     (Ctrl + Shift + C)</b></p><br>"\
            "<p><img source=\"selectConnectedAction\"><br> "\
            "Selects all the atoms that can be reached by the currently selected atom "\
            "via an unbroken chain of bonds. </p>"\
            "<p>To use this feature, you must first be in "\
            "<b>Select Atoms</b> mode and select at least one atom.</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "selectConnectedAction",
                                                       self.selectConnectedAction.iconSet().pixmap() )

        self.selectConnectedAction.setWhatsThis(selectConnectedActionText )
        
        #### Select Doubly ####

        selectDoublyActionText = "<u><b>Select Doubly</b></u>    (Ctrl + Shift + D)</b></p><br>"\
                       "<p><img source=\"selectDoublyAction\"><br> "\
                       "Selects all the atoms that can be reached from a currently selected "\
                       "atom through two disjoint unbroken chains of bonds.  Atoms singly "\
                       "connected to this group and unconnected to anything else are also "\
                       "included in the selection.</p>"\
                       "<p>To use this feature, you must first be in "\
                       "<b>Select Atoms</b> mode and select at least one atom.</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "selectDoublyAction",
                                                       self.selectDoublyAction.iconSet().pixmap() )

        self.selectDoublyAction.setWhatsThis(selectDoublyActionText )
        
        ##############################################
        # Modify Toolbar
        ##############################################
        
        #### Minimize Selection ####

        modifyMinimizeSelActionText = "<u><b>Minimize Selection</b></u>    (Ctrl + M)</b></p><br>"\
                       "<p><img source=\"modifyMinimizeSelAction\"><br> "\
                       "Arranges the atoms (<i>of the current selection</i>) to their chemically stable point of "\
                       "equilibrium in reference to the other atoms in the structure."\
                       "</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "modifyMinimizeSelAction",
                                                       self.modifyMinimizeSelAction.iconSet().pixmap() )

        self.modifyMinimizeSelAction.setWhatsThis(modifyMinimizeSelActionText )
        
        #### Minimize All ####

        modifyMinimizeAllActionText = "<u><b>Minimize All</b></u></p><br>"\
                       "<p><img source=\"modifyMinimizeAllAction\"><br> "\
                       "Arranges the atoms (<i>of the entire part</i>) to their chemically stable point of "\
                       "equilibrium in reference to the other atoms in the structure."\
                       "</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "modifyMinimizeAllAction",
                                                       self.modifyMinimizeAllAction.iconSet().pixmap() )

        self.modifyMinimizeAllAction.setWhatsThis(modifyMinimizeAllActionText )
        
        #### Hydrogenate ####

        modifyHydrogenateActionText = "<u><b>Hydrogenate</b></u> </b></p><br>"\
                       "<p><img source=\"modifyHydrogenateAction\"><br> "\
                       "Adds hydrogen atoms to all the open bonds in the selection.</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "modifyHydrogenateAction",
                                                       self.modifyHydrogenateAction.iconSet().pixmap() )

        self.modifyHydrogenateAction.setWhatsThis(modifyHydrogenateActionText )

        #### Dehydrogenate ####

        modifyDehydrogenateActionText = "<u><b>Dehydrogenate</b></u><br>"\
                       "<p><img source=\"modifyDehydrogenateAction\"><br> "\
                       "Removes all hydrogen atoms from the selection.</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "modifyDehydrogenateAction",
                                                       self.modifyDehydrogenateAction.iconSet().pixmap() )

        self.modifyDehydrogenateAction.setWhatsThis(modifyDehydrogenateActionText )     
        
        #### Passivate ####

        modifyPassivateActionText = "<u><b>Passivate</b></u>    (Ctrl + P)</b></p><br>"\
                       "<p><img source=\"modifyPassivateAction\"><br> "\
                       "Changes the types of incompletely bonded atoms to atoms with the "\
                       "right number of bonds, using atoms with the best atomic radius."\
                       "</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "modifyPassivateAction",
                                                       self.modifyPassivateAction.iconSet().pixmap() )

        self.modifyPassivateAction.setWhatsThis(modifyPassivateActionText )
        
        #### Stretch ####

        modifyStretchActionText = "<u><b>Stretch</b></u><br>"\
                       "<p><img source=\"modifyStretchAction\"><br> "\
                       "Stretches the bonds of the selected chunk(s).</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "modifyStretchAction",
                                                       self.modifyStretchAction.iconSet().pixmap() )

        self.modifyStretchAction.setWhatsThis(modifyStretchActionText )

        #### Delete Bonds ####

        modifyDeleteBondsActionText = "<u><b>Delete Bonds</b></u><br>"\
                       "<p><img source=\"modifyDeleteBondsAction\"><br> "\
                       "Delete all bonds between selected and unselected atoms or chunks.</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "modifyDeleteBondsAction",
                                                       self.modifyDeleteBondsAction.iconSet().pixmap() )

        self.modifyDeleteBondsAction.setWhatsThis(modifyDeleteBondsActionText )  
        
        #### Separate ####

        modifySeparateActionText = "<u><b>Separate</b></u><br>"\
                       "<p><img source=\"modifySeparateAction\"><br> "\
                       "Creates a new chunk from the currently selected atoms.</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "modifySeparateAction",
                                                       self.modifySeparateAction.iconSet().pixmap() )

        self.modifySeparateAction.setWhatsThis(modifySeparateActionText )  
        
        #### Merge Chunks ####

        modifyMergeActionText = "<u><b>Merge Chunks</b></u><br>"\
                       "<p><img source=\"modifyMergeAction\"><br> "\
                       "Merges two or more chunks into a single chunk.</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "modifyMergeAction",
                                                       self.modifyMergeAction.iconSet().pixmap() )
       
        self.modifyMergeAction.setWhatsThis(modifyMergeActionText )  
                
        #### Invert Chunks ####

        modifyInvertActionText = "<u><b>Invert</b></u><br>"\
                       "<p><img source=\"modifyInvertAction\"><br> "\
                       "Inverts the atoms of the selected chunks.</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "modifyInvertAction",
                                                       self.modifyInvertAction.iconSet().pixmap() )
       
        self.modifyInvertAction.setWhatsThis(modifyInvertActionText )  

        #### Align to Common Axis ####

        modifyAlignCommonAxisActionText = "<u><b>Align To Common Axis</b></u><br>"\
                       "<p><img source=\"modifyAlignCommonAxis\"><br> "\
                       "Aligns one or more chunks to the axis of the first selected chunk."\
                       "You must select two or more chunks before using this feature."\
                       "</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "modifyAlignCommonAxis",
                                                       self. modifyAlignCommonAxisAction.iconSet().pixmap() )
       
        self. modifyAlignCommonAxisAction.setWhatsThis( modifyAlignCommonAxisActionText )
                
        ##############################################
        # Tools Toolbar
        ##############################################
        
        #### Select Chunks ####

        toolsSelectMoleculesActionText = "<u><b>Select Chunks</b></u><br>"\
                       "<p><img source=\" toolsSelectMoleculesAction\"><br> "\
                       "<b>Select Chunks</b> allows you to select/unselect chunks with the mouse.</p>"\
                       "<p><b><u>Mouse/Key Combinations</u></b></p>"\
                       "<p><b>Left Click/Drag</b> - selects a chunk(s).</p>"\
                       "<p><b>Ctrl+Left Click/Drag</b> - removes chunk(s) from selection.</p>"\
                       "<p><b>Shift+Left Click/Drag</b> - adds chunk(s) to selection."\
                       "</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( " toolsSelectMoleculesAction",
                                                       self. toolsSelectMoleculesAction.iconSet().pixmap() )
       
        self. toolsSelectMoleculesAction.setWhatsThis( toolsSelectMoleculesActionText )  

        #### Select Atoms ####

        toolsSelectAtomsActionText = "<u><b>Select Atoms</b></u><br>"\
                       "<p><img source=\" toolsSelectAtomsAction\"><br> "\
                       "<b>Select Atoms</b> allows you to select/unselect atoms with the mouse.</p>"\
                       "<p><b><u>Mouse/Key Combinations</u></b></p>"\
                       "<p><b>Left Click/Drag</b> - selects an atom(s).</p>"\
                       "<p><b>Ctrl+Left Click/Drag</b> - removes atom(s) from selection.</p>"\
                       "<p><b>Shift+Left Click/Drag</b> - adds atom(s) to selection."\
                       "</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( " toolsSelectAtomsAction",
                                                       self. toolsSelectAtomsAction.iconSet().pixmap() )
       
        self. toolsSelectAtomsAction.setWhatsThis( toolsSelectAtomsActionText ) 
        
        #### Move Chunks ####

        toolsMoveMoleculeActionText = "<u><b>Move Chunks</b></u><br>"\
                       "<p><img source=\" toolsMoveMoleculeAction\"><br> "\
                       "Activates <b>Move Chunks</b> mode, allowing you to select, "\
                       "move and rotate one of more chunks with the mouse.</p>"\
                       "<p><b><u>Mouse/Key Combinations</u></b></p>"\
                       "<p><b>Left Drag</b> - moves the selected chunk(s).</p>"\
                       "<p><b>Ctrl+Left Drag</b> - freely rotates selected chunk(s).</p>"\
                       "<p><b>Shift+Left Drag</b> - constrained movement and rotation of a chunk about its own axis."\
                       "</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( " toolsMoveMoleculeAction",
                                                       self. toolsMoveMoleculeAction.iconSet().pixmap() )
       
        self. toolsMoveMoleculeAction.setWhatsThis( toolsMoveMoleculeActionText ) 
        
        #### Build Atoms Tool ####

        toolsDepositAtomActionText = "<u><b>Build Tool</b></u><br>"\
                       "<p><img source=\" toolsDepositAtomAction\"><br> "\
                       "<b>Build Tool</b> allows you to deposit individual atoms or add/move/delete "\
                       "atoms from an existing chunk.  Build Tool can also be used to paste "\
                       "copies of chunks from the clipboard into the part.</p>"\
                       "<p><b><u>Mouse/Key Combinations</u></b></p>"\
                       "<p><b>Left Click</b> - adds an atom or pastes a chunk from the clipboard. "\
                       "New atoms can be connected to an existing chunk if an open bond is highlighted "\
                       "during a left click.</p>"\
                       "<p><b>Ctrl+Left Click</b> - deletes a highlighted atom or bond.</p>"\
                       "<p><b>Shift+Left Drag</b> - moves an atom or open bond. An open bond will be "\
                       "connected to another open bond if the mouse button is released over a different "\
                       "open bond."\
                       "</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( " toolsDepositAtomAction",
                                                       self. toolsDepositAtomAction.iconSet().pixmap() )
       
        self. toolsDepositAtomAction.setWhatsThis( toolsDepositAtomActionText ) 
        
        #### Cookie Cutter ####
                                        
        toolsCookieCutActionText = "<u><b>Cookie Cutter Tool</b></u><br>"\
                       "<p><><img source=\" toolsCookieCutAction\"><br> "\
                       "Activates <b>Cookie Cutter</b> mode, allowing you to cut out 3-D shapes from a "\
                       "slab of diamond or lonsdaleite lattice.</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( " toolsCookieCutAction",
                                                       self. toolsCookieCutAction.iconSet().pixmap() )
       
        self. toolsCookieCutAction.setWhatsThis( toolsCookieCutActionText )
       
        #### Extrude Tool ####

        toolsExtrudeActionText = "<u><b>Extrude Tool</b></u><br>"\
                       "<p><img source=\" toolsExtrudeAction\"><br> "\
                       "Activates <b>Extrude</b> mode, allowing you to create a rod or ring using a chunk as "\
                       "a repeating unit.</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( " toolsExtrudeAction",
                                                       self. toolsExtrudeAction.iconSet().pixmap() )
       
        self. toolsExtrudeAction.setWhatsThis( toolsExtrudeActionText )  
        
        #### Fuse Chunks Tool ####

        toolsFuseChunksActionText = "<u><b>Fuse Chunks Tool</b></u><br>"\
                       "<p><img source=\" toolsFuseChunksAction\"><br> "\
                       "<b>Fuse Chunks</b> creates bonds between two or more chunks.</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( " toolsFuseChunksAction",
                                                       self. toolsFuseChunksAction.iconSet().pixmap() )
       
        self.toolsFuseChunksAction.setWhatsThis( toolsFuseChunksActionText )
        
        #### Fuse Atoms Tool ####

        toolsFuseAtomsActionText = "<u><b>Fuse Atoms Tool</b></u><br>"\
                       "<p><img source=\" toolsFuseAtomsAction\"><br> "\
                       "<b>Fuse Atoms</b> fuses the overlapping atoms between two or more chunks.</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( " toolsFuseAtomsAction",
                                                       self. toolsFuseAtomsAction.iconSet().pixmap() )
       
        self.toolsFuseAtomsAction.setWhatsThis( toolsFuseAtomsActionText )  

        #### Movie Player ####

        simMoviePlayerActionText = "<u><b>Movie Player</b></u><br>"\
                       "<p><img source=\" simMoviePlayerAction\"><br> "\
                       "Plays the most recent trajectory (movie) file created by the <b>Simulator</b>.</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( " simMoviePlayerAction",
                                                       self. simMoviePlayerAction.iconSet().pixmap() )
       
        self. simMoviePlayerAction.setWhatsThis( simMoviePlayerActionText )  
        
        #### Simulator ####

        simSetupActionText = "<u><b>Simulator</b></u><br>"\
                       "<p><img source=\" simSetupAction\"><br> "\
                       "Creates a trajectory (movie) file by calculating the inter-atomic potentials and bonding "\
                       "of the entire model.  The user determines the number of frames in the movie, the time step, "\
                       "and the temperature for the simulation.</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( " simSetupAction",
                                                       self. simSetupAction.iconSet().pixmap() )
       
        self. simSetupAction.setWhatsThis( simSetupActionText )

        #### Plot Tool ####

        simPlotToolActionText = "<u><b>Plot Tool</b></u><br>"\
                       "<p><img source=\" simPlotToolAction\"><br> "\
                       "Plots a simulator trace file using GNUplot.  A simulation must be run to create "\
                       "the trace file, and the part must have a jig that writes output to the trace file. <br><br>"\
                       "The following list of jigs write data to the trace file:<br>"\
                       "<b>Rotary Motors:</b> speed (GHz) and torque (nn-nm)<br>"\
                       "<b>Linear Motors:</b> displacement (pm)<br>"\
                       "<b>Anchors:</b> torque (nn-nm)<br>"\
                       "<b>Thermostats:</b> energy added (zJ)<br>"\
                       "<b>Thermometer:</b> temperature (K)<br>"\
                       "</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( " simPlotToolAction",
                                                       self. simPlotToolAction.iconSet().pixmap() )
       
        self. simPlotToolAction.setWhatsThis( simPlotToolActionText )
                
        ##############################################
        # Dashboard Buttons
        ##############################################
        
        #### Done ####

        toolsDoneActionText = "<u><b>Done</b></u><br>"\
                       "<p><img source=\" toolsDoneAction\"><br> "\
                       "Completes the current operation and enters Select Chunks mode."\
                       "</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( " toolsDoneAction",
                                                       self. toolsDoneAction.iconSet().pixmap() )
       
        self. toolsDoneAction.setWhatsThis( toolsDoneActionText )  

        #### Cancel ####

        toolsCancelActionText = "<u><b>Cancel</b></u><br>"\
                       "<p><img source=\" toolsCancelAction\"><br> "\
                       "Cancels the current operation and enters Select Chunks mode."\
                       "</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( " toolsCancelAction",
                                                       self.toolsCancelAction.iconSet().pixmap() )
       
        self. toolsCancelAction.setWhatsThis( toolsCancelActionText ) 
        
        #### Back up ####

        toolsBackUpActionText = "<u><b>Back Up</b></u><br>"\
                       "<p><img source=\" toolsBackUpAction\"><br> "\
                       "Undoes the previous operation."\
                       "</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( " toolsBackUpAction",
                                                       self.toolsBackUpAction.iconSet().pixmap() )
       
        self. toolsBackUpAction.setWhatsThis( toolsBackUpActionText ) 
   
        #### Start Over ####
                        
        toolsStartOverActionText = "<u><b>Start Over</b></u><br>"\
                       "<p><img source=\"toolsStartOverAction\"><br> "\
                       "Cancels the current operation, leaving the user in the current mode."\
                       "</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "toolsStartOverAction",
                                                       self.toolsStartOverAction.iconSet().pixmap() )
       
        self.toolsStartOverAction.setWhatsThis(toolsStartOverActionText ) 
        
        #### Add Layers ####
                        
        ccAddLayerActionText = "<u><b>Add Layer</b></u><br>"\
                       "<p><img source=\"ccAddLayerAction\"><br> "\
                       "Adds a new layer of diamond lattice to the existing layer.</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "ccAddLayerAction",
                                                       self.ccAddLayerAction.iconSet().pixmap() )
       
        self.ccAddLayerAction.setWhatsThis(ccAddLayerActionText ) 
        
        ##############################################
        # Jigs
        ##############################################
        
        #### Anchor ####

        jigsAnchorActionText = "<u><b>Anchor</b></u><br>"\
                       "<p><img source=\"jigsAnchorAction\"><br> "\
                       "Attaches a <b>Anchor</b> to the selected atom(s), which "\
                       "constrains its motion during a minimization or simulation.</p>"\
                       "<p>To create an Anchor, enter <b>Select Atoms</b> mode, "\
                       "select the atom(s) you want to anchor and then select this action. "\
                       "Anchors are drawn as a black wireframe box around each selected atom.</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "jigsAnchorAction",
                                                       self.jigsAnchorAction.iconSet().pixmap() )
       
        self.jigsAnchorAction.setWhatsThis(jigsAnchorActionText )  
        
        #### Rotary Motor ####

        jigsMotorActionText = "<u><b>Rotary Motor</b></u><br>"\
                       "<p><img source=\"jigsMotorAction\"><br> "\
                       "Attaches a <b>Rotary Motor</b> to the selected atoms.  The Rotary Motor is used by "\
                       "the simulator to apply rotary motion to a set of atoms during a simulation run.  You may "\
                       "specify the <b>torque (in nN*nm)</b> and <b>speed (in Ghz)</b> of the motor.</p>"\
                       "<p>To create a Rotary Motor, enter <b>Select Atoms</b> mode, "\
                       "select the atoms you want to attach the motor to and then select this action.</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "jigsMotorAction",
                                                       self.jigsMotorAction.iconSet().pixmap() )
       
        self.jigsMotorAction.setWhatsThis(jigsMotorActionText )  
        
        #### Linear Motor ####

        jigsLinearMotorActionText = "<u><b>Linear Motor</b></u><br>"\
                       "<p><img source=\"jigsLinearMotorAction\"><br> "\
                       "Attaches a <b>Linear Motor</b> to the selected atoms.  The Linear Motor is used by "\
                       "the simulator to apply linear motion to a set of atoms during a simulation run.  You may "\
                       "specify the <b>force (in nN*nm)</b> and <b>stiffness (in N/m)</b> of the motor.</p>"\
                       "<p>To create a Linear Motor, enter <b>Select Atoms</b> mode, "\
                       "select the atoms you want to attach the motor to and then select this action.</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "jigsLinearMotorAction",
                                                       self.jigsLinearMotorAction.iconSet().pixmap() )
       
        self.jigsLinearMotorAction.setWhatsThis(jigsLinearMotorActionText )  
        
        #### Thermostat ####

        jigsStatActionText = "<u><b>Thermostat</b></u><br>"\
                       "<p><img source=\"jigsStatAction\"><br> "\
                       "Attaches a <b>Langevin Thermostat</b> to a single selected atom, thereby associating "\
                       "the themostat to the entire molecule of which the selected atom is a member. The user "\
                       "specifies the temperature (in Kelvin).</p>"\
                       "<p>The Langevin Thermostat is used to set and hold the temperature "\
                       "of a molecule during a simulation run.</p>"\
                       "<p>To create a Langevin Thermostat, enter <b>Select Atoms</b> mode, "\
                       "select a single atom and then select this action. The thermostat is drawn as a "\
                       "blue wireframe box around the selected atom.</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "jigsStatAction",
                                                       self.jigsStatAction.iconSet().pixmap() )
       
        self.jigsStatAction.setWhatsThis(jigsStatActionText ) 

        #### Thermometer ####

        jigsThermoActionText = "<u><b>Thermometer</b></u><br>"\
                       "<p><img source=\"jigsThermoAction\"><br> "\
                        "Attaches a <b>Thermometer</b> to a single selected atom, thereby associating "\
                       "the themometer to the entire molecule of which the selected atom is a member. "\
                       "<p>The temperature of the molecule will be recorded and written to a trace file "\
                       "during a simulation run.</p>"\
                       "<p>To create a Thermometer, enter <b>Select Atoms</b> mode, "\
                       "select a single atom and then select this action. The thermometer is drawn as a "\
                       "dark red wireframe box around the selected atom.</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "jigsThermoAction",
                                                       self.jigsThermoAction.iconSet().pixmap() )
       
        self.jigsThermoAction.setWhatsThis(jigsThermoActionText ) 
        
        ##############################################
        # Display
        ##############################################
        
        #### Display Object Color ####

        dispObjectColorActionText = "<u><b>Object Color</b></u><br>"\
                       "<p><img source=\"dispObjectColorAction\"><br> "\
                       "Allows you to change the color of the selected object(s).</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "dispObjectColorAction",
                                                       self.dispObjectColorAction.iconSet().pixmap() )
       
        self.dispObjectColorAction.setWhatsThis(dispObjectColorActionText ) 
        
        #### Display Background Color ####

        dispBGColorActionText = "<u><b>Background Color</b></u><br>"\
                       "<p><img source=\"dispBGColorAction\"><br> "\
                       "Allows you to change the background color of the main window.</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "dispBGColorAction",
                                                       self.dispBGColorAction.iconSet().pixmap() )
       
        self.dispBGColorAction.setWhatsThis(dispBGColorActionText ) 
       
        ##############################################
        # Help Toolbar
        ##############################################
        
        #### NE-1 Assistant ####
        
        helpAssistantText = "<u><b>nanoENGINEER-1 Assistant</b></u><br>"\
                        "<p><img source=\"helpAssistant\"><br> "\
                       "Opens  <b>nanoENGINEER-1 Assistant</b>, "\
                       "the nanoENGINEER-1 Reference Documentation.</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "helpAssistant",
                                                       self.helpAssistantAction.iconSet().pixmap() )

        self.helpAssistantAction.setWhatsThis( helpAssistantText )
        
        #### What's This ####
        
        helpWhatsThisText = "<u><b>What's This</b></u><br>"\
                        "<p><img source=\"helpWhatsThis\"><br> "\
                       "Click this option to invoke a small question mark that is attached to the mouse pointer. "\
                       "Click on a feature which you would like more information about. "\
                       "A popup box appears with information about the feature.</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "helpWhatsThis",
                                                       self.helpWhatsThisAction.iconSet().pixmap() )

        self.helpWhatsThisAction.setWhatsThis( helpWhatsThisText )
        

        ##############################################
        # Datum Display Toolbar
        ##############################################
        
        #### Display Trihedron ####

        dispTrihedronText = "<u><b>Display Trihedron</b></u><br>"\
                       "<p><img source=\"dispTrihedron\"><br> "\
                       "Toggles the trihedron on and off.</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "dispTrihedron",
                                                       self.dispTrihedronAction.iconSet().pixmap() )
       
        self.dispTrihedronAction.setWhatsThis(dispTrihedronText ) 

        #### Display Csys ####

        dispCsysText = "<u><b>Display Csys Axis</b></u><br>"\
                       "<p><img source=\"dispCsys\"><br> "\
                       "Toggles the coordinate system axis on and off."\
                       "</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "dispCsys",
                                                       self.dispCsysAction.iconSet().pixmap() )
       
        self.dispCsysAction.setWhatsThis(dispCsysText ) 
        
        #### Display Datum Lines ####

        dispDatumLinesText = "<u><b>Display Datum Lines</b></u><br>"\
                       "<p><img source=\"dispDatumLines\"><br> "\
                       "Toggles Datum Lines on and off.</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "dispDatumLines",
                                                       self.dispDatumLinesAction.iconSet().pixmap() )
       
        self.dispDatumLinesAction.setWhatsThis(dispDatumLinesText )    

        #### Display Datum Planes ####

        dispDatumPlanesText = "<u><b>Display Datum Planes</b></u><br>"\
                       "<p><img source=\"dispDatumPlanes\"><br> "\
                       "Toggles Datum Planes on and off.</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "dispDatumPlanes",
                                                       self.dispDatumPlanesAction.iconSet().pixmap() )
       
        self.dispDatumPlanesAction.setWhatsThis(dispDatumPlanesText )    
        
        #### Display Grid ####

        dispGridText = "<u><b>Display 3-D Grid</b></u><br>"\
                       "<p><img source=\"dispGrid\"><br> "\
                       "Toggles the 3-D grid on and off."\
                       "</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "dispGrid",
                                                       self.dispGridAction.iconSet().pixmap() )
       
        self.dispGridAction.setWhatsThis(dispGridText )           

        #### Display Open Bonds ####

        dispOpenBondsText = "<u><b>Display Singlets</b></u><br>"\
                       "<p><img source=\"dispOpenBonds\"><br> "\
                       "Toggles Singlets on and off."\
                       "</p>"

        QMimeSourceFactory.defaultFactory().setPixmap( "dispOpenBonds",
                                                       self.dispOpenBondsAction.iconSet().pixmap() )
       
        self.dispOpenBondsAction.setWhatsThis(dispOpenBondsText )
        

def create_whats_this_descriptions_for_selectAtomsMode(w):
    "Create What's This descriptions for the Select Atoms mode dashboard widgets."
    
    #### Element Selector ####

    eSelectorText = "<u><b>Element Selector</b></u><br>"\
                       "<p><img source=\"eselectoricon\"><br> "\
                       "Opens the <b>Element Selector</b>, which aids in atom selection when the "\
                       "<b>Selection Filter</b> is activated."\
                       "</p>"\
                       "<p>It also contains a <b>Transmute</b> button, which allows the user to change the "\
                       "selected atoms to the current atom type (in the Element Selector)."\
                       "</p>"

    QMimeSourceFactory.defaultFactory().setPixmap( "eselectoricon",
                                                       w.modifySetElementAction.iconSet().pixmap() )
       
    w.modifySetElementAction.setWhatsThis(eSelectorText )
    
    # Filter Checkbox #
    
    filterText = "<u><b>Selection Filter</b></u><br> "\
                        "When turned on, only atoms of the current atom type are selected."\
                        "</p>"

    #QWhatsThis.add ( w.filterCheckBox, filterText )
    
    # Atom Type Combobox #
    
    elemFilterText = "<u><b>Atom Type</b></u><br> "\
                        "Decides the type of atoms that will be selected while performing select atoms operation in the 3D workspace. \
Example: if this combobox is showing 'Carbon' as the element type, only carbon atoms will be selected when 'select atoms' operation is performed the next time \
in the 3 D workspace."\
"</p>"
                        
    QWhatsThis.add ( w.elemFilterComboBox, elemFilterText)
    
def create_whats_this_descriptions_for_depositMode(w):
    "Create What's This descriptions for the deposit (Build) mode dashboard widgets."
    
    #### Modeling Kit ####

    mmkitText = "<u><b>Modeling Kit</b></u><br>"\
                       "<p><img source=\"mmkiticon\"><br> "\
                       "Opens the Modeling Kit, which aids in atom and clipboard selection."\
                       "</p>"

    QMimeSourceFactory.defaultFactory().setPixmap( "mmkiticon",
                                                       w.modifyMMKitAction.iconSet().pixmap() )
       
    w.modifyMMKitAction.setWhatsThis(mmkitText )
        
    # Deposit (Atom) button
    
    depositText = "<u><b>Deposit Atom</b></u><br> "\
                        "<p><img source=\"eyedroppericon\"><br> "\
                        "Sets <i>Deposit Atom</i> mode."\
                        "</p>"

    QMimeSourceFactory.defaultFactory().setPixmap( "eyedroppericon",
                        w.depositAtomDashboard.depositBtn.iconSet().pixmap() )

    QWhatsThis.add ( w.depositAtomDashboard.depositBtn, depositText )
    
    # Paste button
    
    pasteText = "<u><b>Paste from Clipboard</b></u><br> "\
                        "<p><img source=\"clipboardicon\"><br> "\
                        "Sets <i>Paste</i> mode."\
                        "</p>"

    QMimeSourceFactory.defaultFactory().setPixmap( "clipboardicon",
                        w.depositAtomDashboard.pasteBtn.iconSet().pixmap() )

    QWhatsThis.add ( w.depositAtomDashboard.pasteBtn, pasteText )
    
    # Single Bond button
    
    singleBondText = "<u><b>Single Bond Mode</b></u><br> "\
                        "<p><img source=\"singlebondicon\"><br> "\
                        "Sets <i>Single Bond</i> mode.  Clicking on a highlighted bond "\
                        "will change the bond to a single bond, if permitted."\
                        "</p>"

    QMimeSourceFactory.defaultFactory().setPixmap( "singlebondicon",
                        w.depositAtomDashboard.bond1Btn.iconSet().pixmap() )

    QWhatsThis.add ( w.depositAtomDashboard.bond1Btn, singleBondText )
    
    # Double Bond button
    
    doubleBondText = "<u><b>Double Bond Mode</b></u><br> "\
                        "<p><img source=\"doublebondicon\"><br> "\
                        "Sets <i>Double Bond</i> mode.  Clicking on a highlighted bond "\
                        "will change the bond to a double bond, if permitted."\
                        "</p>"

    QMimeSourceFactory.defaultFactory().setPixmap( "doublebondicon",
                        w.depositAtomDashboard.bond2Btn.iconSet().pixmap() )

    QWhatsThis.add ( w.depositAtomDashboard.bond2Btn, doubleBondText )
    
    # Triple Bond button
    
    tripleBondText = "<u><b>Triple Bond Mode</b></u><br> "\
                        "<p><img source=\"triplebondicon\"><br> "\
                        "Sets <i>Triple Bond</i> mode.  Clicking on a highlighted bond "\
                        "will change the bond to a triple bond, if permitted."\
                        "</p>"

    QMimeSourceFactory.defaultFactory().setPixmap( "triplebondicon",
                        w.depositAtomDashboard.bond3Btn.iconSet().pixmap() )

    QWhatsThis.add ( w.depositAtomDashboard.bond3Btn, tripleBondText )
    
    # Aromatic Bond button
    
    aromaticBondText = "<u><b>Aromatic Bond Mode</b></u><br> "\
                        "<p><img source=\"aromaticbondicon\"><br> "\
                        "Sets <i>Aromatic Bond</i> mode.  Clicking on a highlighted bond "\
                        "will change the bond to an aromatic bond, if permitted."\
                        "</p>"

    QMimeSourceFactory.defaultFactory().setPixmap( "aromaticbondicon",
                        w.depositAtomDashboard.bondaBtn.iconSet().pixmap() )

    QWhatsThis.add ( w.depositAtomDashboard.bondaBtn, aromaticBondText )
    
    # Graphitic Bond button
    
    graphiticBondText = "<u><b>Graphitic Bond Mode</b></u><br> "\
                        "<p><img source=\"graphiticbondicon\"><br> "\
                        "Sets <i>Graphitic Bond</i> mode.  Clicking on a highlighted bond "\
                        "will change the bond to a graphitic bond, if permitted."\
                        "</p>"

    QMimeSourceFactory.defaultFactory().setPixmap( "graphiticbondicon",
                        w.depositAtomDashboard.bondgBtn.iconSet().pixmap() )

    QWhatsThis.add ( w.depositAtomDashboard.bondgBtn, graphiticBondText )
    
    # Autobond checkbox
    
    autoBondText = "<u><b>Autobond</b></u><br> "\
                        "Enables/disables <b>Autobonding</b><br> "\
                        "<br> When <b>enabled</b>, additional bonds are formed "\
                        "<b>automatically</b> with the deposited atom  if any "\
                        "open bonds of neighboring atoms fall within the VdW radius, "\
                        "and the deposited atom has extra bonds available.<br>"\
                        "<br>When <b>disabled</b>, the deposited atom will form only one "\
                        "bond <b>manually</b> with the open bond selected by the user."\
                        "</p>"

    QWhatsThis.add ( w.depositAtomDashboard.autobondCB, autoBondText )
    
    autoBondTipText = "Enables/disables Autobonding"

    QToolTip.add(w.depositAtomDashboard.autobondCB, autoBondTipText)
    

def create_whats_this_descriptions_for_UserPrefs_dialog(w):
    "Create What's This descriptions for the User Prefs dialog widgets."

    #### Bond Line Thickness ####

    bondThicknessText = "<u><b>Bond Thickness</b></u><br>"\
                       "Sets the <i>Bond Thickness</i> (in pixels) for Lines Display Mode."\
                       "This will also affect the thickness of bonds where atoms or chunks "\
                       "have been set to <b>Lines</b> display."\
                       "</p>"
       
    QWhatsThis.add ( w.bond_line_thickness_spinbox, bondThicknessText )

def create_whats_this_descriptions_for_NanoHive_dialog(w):
    "Create What's This descriptions for the Nano-Hive dialog widgets."
    
    #### MPQC Electrostatics Potential Plane ####

    MPQCESPText = "<u><b>MPQC Electrostatics Potential Plane</b></u><br>"\
                       "Enables the <i>MPQC Electrostatics Potential Plane</i> plugin. "\
                       "</p>"
       
    QWhatsThis.add ( w.MPQC_ESP_checkbox, MPQCESPText )
    
    MPQCESPTipText = "Enables/disables MPQC Electrostatics Potential Plane Plugin"

    QToolTip.add(w.MPQC_ESP_checkbox, MPQCESPTipText)
    
def fix_whatsthis_text_for_mac(parent):
    '''If the system is a Mac, this replaces all occurances of 'Ctrl' with 'Cmd' in all the 
    whatsthis text for all QAction widgets that are children of parent.  This should be 
    called after all widgets (and their whatsthis text) in the UI have been created.
    '''
    from platform import is_macintosh #bruce 051227 zapped only use of misguided is_not_macintosh variant of this
    
    if is_macintosh():  
        objList = parent.queryList("QAction")
        for obj in objList:
            original_txt = obj.whatsThis()
            new_txt = replace_ctrl_with_cmd_text(original_txt)
            obj.setWhatsThis(new_txt)
###@@@ bruce 051227 hack
    if enable_whatsthis_links:
        hack_whatsthis_object_for_widgets(parent)
###@@@ end bruce hack
    return

###@@@ bruce 051227 hack

_KEEPERS = []

def hack_whatsthis_object_for_widgets(parent):
    objList = parent.queryList("QWidget")
    for widget in objList:
        try:
            ## this never works: original_txt = widget.whatsThis()
            original_txt = QWhatsThis.textFor( widget)
        except:
            pass ## print "no textFor attr, or it fails:",widget
            ## this happens for a lot of QObjects (don't know what they are), e.g. for <constants.qt.QObject object at 0xb96b750>
        else:
            # it's often a null string
            if original_txt:
                original_txt = str(original_txt) # in case of QString, tho during debug it seemed this was already a Python string
                newtext = modified_whatsthis_text(original_txt, widget)
                if newtext:
                    pass
                else:
                    print "didn't find desired content in:", original_text ###@@@
                    FAKELINK = "<a href=\"xxx\">linktoxxx</a>"
                    newtext = FAKELINK + str(original_txt) + FAKELINK ###@@@
                set_hyperlinked_whatsthis_text(widget, newtext)
    return

def set_hyperlinked_whatsthis_text(widget, text):
    obj1 = MyWhatsThis( widget, text)
    ## widget._KEEP_WHATSTHIS = obj1 # this was not sufficient to prevent a bus error
    _KEEPERS.append(obj1) # this is needed to prevent a bus error
    return

def modified_whatsthis_text(text, widget):
    "Given some nonempty whatsthis text from a widget, return None or modified text (e.g. containing a web help URL)."
    if text.startswith("<u><b>"):
        text = text[len("<u><b>"):] # strip that prefix
        ff = text.split("</b></u>", 1)
        if len(ff) == 2: # should never be more than 2
            text = ff[0] # the words between <u><b> and </b></u>
            rest = ff[1] # use this part later, unchanged
            #e should verify text is one or more capitalized words sep by ' '; could use split, isalpha (or so) ###@@@
            print "proposed web help name: %r" % (text,) ###@@@
            return "<a href=\"%s\">%s</a>" % ("fakeurl", text) + rest #WRONG link URL (or featurename to be made into URL later) ###@@@
    return None

###@@@ end bruce hack
    
def replace_ctrl_with_cmd_text(str):
    '''Returns a string, replacing all occurances of Ctrl with Cmd in 'str'.
    '''
    str = str.replace('Ctrl', 'Cmd')
    str = str.replace('ctrl', 'cmd')
    return str
