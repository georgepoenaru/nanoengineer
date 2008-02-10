# Copyright 2004-2007 Nanorex, Inc.  See LICENSE file for details. 
"""
$Id$

TODO: 
- Does the parentWidget for the DnaFlyout always needs to be a propertyManager
  The parentWidget is the propertyManager object of the currentCommand on the 
  commandSequencer. What if the currentCommand doesn't have a PM but it wants 
  its own commandToolbar?  Use the mainWindow as its parentWidget? 
- The implementation may change after Command Manager (Command toolbar) code 
  cleanup. The implementation as of 2007-12-20 is an attempt to define 
  flyouttoolbar object in the 'Command.
"""

import env
from PyQt4 import QtCore, QtGui
from PyQt4.Qt import Qt
from PyQt4.Qt import SIGNAL
from icon_utilities import geticon
from utilities.Log import greenmsg

_theDnaFlyout = None

#NOTE: global methods setupUi, activateDnaFlyout are not called as of 2007-12-19
#Use methods like DnaFlyout.activateFlyoutToolbar instead. 
#Command toolbar needs to be integrated with the commandSequencer. 
#See DnaDuplex_EditCommand.init_gui for an example. (still experimental)


def setupUi(mainWindow):
    """
    Construct the QWidgetActions for the Dna flyout on the 
    Command Manager toolbar.
    """
    global _theDnaFlyout

    _theDnaFlyout = DnaFlyout(mainWindow)
    
# probably needs a retranslateUi to add tooltips too...

def activateDnaFlyout(mainWindow):
    mainWindow.commandToolbar.updateCommandToolbar(mainWindow.buildDnaAction, 
                                                   _theDnaFlyout)

    
class DnaFlyout:    
    def __init__(self, mainWindow, parentWidget):
        """
        Create necessary flyout action list and update the flyout toolbar in
        the command toolbar with the actions provided by the object of this
        class.
        
        @param mainWindow: The mainWindow object
        @type  mainWindow: B{MWsemantics} 
        
        @param parentWidget: The parentWidget to which actions defined by this 
                             object belong to. This needs to be revised.
                             
        """
    
        
        self.parentWidget = parentWidget
        self.win = mainWindow
        self._isActive = False
        self._createActions(self.parentWidget)
        

    def getFlyoutActionList(self):
        """
        Returns a tuple that contains lists of actions used to create
        the flyout toolbar. 
        Called by CommandToolbar._createFlyoutToolBar().
        @return: params: A tuple that contains 3 lists: 
        (subControlAreaActionList, commandActionLists, allActionsList)
        """
        #'allActionsList' returns all actions in the flyout toolbar 
        #including the subcontrolArea actions. 
        allActionsList = []
        
        self.subControlActionGroup = QtGui.QActionGroup(self.parentWidget)
        self.subControlActionGroup.setExclusive(False)   
        self.subControlActionGroup.addAction(self.dnaDuplexAction)
        self.subControlActionGroup.addAction(self.breakStrandAction) 

        #Action List for  subcontrol Area buttons. 
        subControlAreaActionList = []
        subControlAreaActionList.append(self.exitDnaAction)
        separator = QtGui.QAction(self.parentWidget)
        separator.setSeparator(True)
        subControlAreaActionList.append(separator) 
        subControlAreaActionList.append(self.dnaDuplexAction)        
        subControlAreaActionList.append(self.breakStrandAction)
        subControlAreaActionList.append(self.orderDnaAction)

        allActionsList.extend(subControlAreaActionList)

        commandActionLists = [] 
        #Append empty 'lists' in 'commandActionLists equal to the 
        #number of actions in subControlArea 
        for i in range(len(subControlAreaActionList)):
            lst = []
            commandActionLists.append(lst)
                            
        params = (subControlAreaActionList, commandActionLists, allActionsList)
        
        return params

    def _createActions(self, parentWidget):
        self.exitDnaAction = QtGui.QWidgetAction(parentWidget)
        self.exitDnaAction.setText("Exit DNA")
        self.exitDnaAction.setIcon(
            geticon("ui/actions/Toolbars/Smart/Exit.png"))
        self.exitDnaAction.setCheckable(True)
        
        self.dnaDuplexAction = QtGui.QWidgetAction(parentWidget)
        self.dnaDuplexAction.setText("Duplex")
        self.dnaDuplexAction.setCheckable(True)        
        self.dnaDuplexAction.setIcon(
            geticon("ui/actions/Tools/Build Structures/Duplex.png"))
        
        self.breakStrandAction = QtGui.QWidgetAction(parentWidget)
        self.breakStrandAction.setText("Break Strand")
        self.breakStrandAction.setCheckable(True)        
        self.breakStrandAction.setIcon(
            geticon("ui/actions/Properties Manager/Break_Strand.png"))

        self.dnaOrigamiAction = QtGui.QWidgetAction(parentWidget)
        self.dnaOrigamiAction.setText("Origami")
        self.dnaOrigamiAction.setIcon(
            geticon("ui/actions/Tools/Build Structures/DNA_Origami.png"))
        
        self.orderDnaAction = QtGui.QWidgetAction(parentWidget)
        self.orderDnaAction.setText("Order DNA")
        self.orderDnaAction.setIcon(
            geticon("ui/actions/Command Toolbar/Order_DNA.png"))

        # Add tooltips
        self.dnaDuplexAction.setToolTip("Duplex")
        self.dnaOrigamiAction.setToolTip("Origami")
        self.orderDnaAction.setToolTip("Order DNA")
    
    def connect_or_disconnect_signals(self, isConnect):
        """
        Connect or disconnect widget signals sent to their slot methods.
        This can be overridden in subclasses. By default it does nothing.
        @param isConnect: If True the widget will send the signals to the slot 
                          method. 
        @type  isConnect: boolean
        
        @see: self.activateFlyoutToolbar, self.deActivateFlyoutToolbar
        """
        if isConnect:
            change_connect = self.win.connect
        else:
            change_connect = self.win.disconnect 
            
        change_connect(self.exitDnaAction, 
                       SIGNAL("triggered(bool)"),
                       self.activateExitDna)
        
        change_connect(self.dnaDuplexAction, 
                             SIGNAL("triggered(bool)"),
                             self.activateDnaDuplex_EditCommand)
        
        change_connect(self.breakStrandAction, 
                             SIGNAL("triggered(bool)"),
                             self.activateBreakStrand_Command)
        
        change_connect(self.dnaOrigamiAction, 
                             SIGNAL("triggered()"),
                             self.activateDnaOrigamiEditCommand)
        
        change_connect(self.orderDnaAction, 
                             SIGNAL("triggered()"),
                             self.orderDnaCommand)
    
    
    def activateFlyoutToolbar(self):
        """
        Updates the flyout toolbar with the actions this class provides. 
        """    
               
        if self._isActive:
            return
        
        self._isActive = True
        
        #Temporary workaround for bug 2600 
        #until the Command Toolbar code is revised
        #When DnaFlyout toolbar is activated, it should switch to (check) the 
        #'Build Button' in the control area. So that the DnaFlyout 
        #actions are visible in the flyout area of the command toolbar. 
        #-- Ninad 2008-01-21. 
        self.win.commandToolbar.cmdButtonGroup.button(0).setChecked(True)
        #Now update the command toolbar (flyout area)
        self.win.commandToolbar.updateCommandToolbar(self.win.buildDnaAction,
                                                     self)
        #self.win.commandToolbar._setControlButtonMenu_in_flyoutToolbar(
                    #self.cmdButtonGroup.checkedId())
        self.exitDnaAction.setChecked(True)
        self.connect_or_disconnect_signals(True)
    
    def deActivateFlyoutToolbar(self):
        """
        Updates the flyout toolbar with the actions this class provides.
        """
        if not self._isActive:
            return 
        
        self._isActive = False
        
        #Uncheck all the actions in the flyout toolbar (subcontrol area)
        for action in self.subControlActionGroup.actions():
            if action.isChecked():
                action.setChecked(False)
            
        self.connect_or_disconnect_signals(False)    
        self.win.commandToolbar.updateCommandToolbar(self.win.buildDnaAction,
                                                     self,
                                                     entering = False)

    def activateExitDna(self, isChecked):
        """
        Slot for B{Exit DNA} action.
        """     
        #@TODO: This needs to be revised. 
        
        if hasattr(self.parentWidget, 'ok_btn_clicked'):
            if not isChecked:
                self.parentWidget.ok_btn_clicked()
        
    def activateDnaDuplex_EditCommand(self, isChecked):
        """
        Slot for B{Duplex} action.
        """
            
        self.win.insertDna(isChecked)
        
        #IMPORTANT: 
        #For a QAction, the method 
        #setChecked does NOT emmit the 'triggered' SIGNAL. So 
        #we can call self.breakStrandAction.setChecked without invoking its 
        #slot method!
        #Otherwise we would have needed to block the signal when action is 
        #emitted ..example we would have called something like :
        #'if self._block_dnaDuplexAction_event: return' at the beginning of this
        #method. Why we didn't use QAction group -- We need these actions to be
        # a) exclusive as well as
        #(b) 'toggle-able' (e.g. if you click on a checked action , it should 
        #uncheck)
        #QActionGroup achieves (a) but can't do (b) 
        
        if self.breakStrandAction.isChecked():
            self.breakStrandAction.setChecked(False)
        
    
    def activateBreakStrand_Command(self, isChecked):
        """
        """
        self.win.enterBreakStrandCommand(isChecked)
        
        if self.dnaDuplexAction.isChecked():
            self.dnaDuplexAction.setChecked(False)

    def activateDnaOrigamiEditCommand(self):
        """
        Slot for B{Origami} action.
        """
        msg1 = greenmsg("DNA Origami: ")
        msg2 = "Not implemented yet."
        final_msg = msg1 + msg2
        env.history.message(final_msg)
        
    def orderDnaCommand(self):
        """
        Slot for B{Order DNA} action.
        @see: MWSemantics.orderDna
        """
        self.win.orderDna()
        
        
                
        
