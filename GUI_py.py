#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

# <rtc-template block="description">
"""
 @file GUI_py.py
 @brief ModuleDescription
 @date $Date$


"""
# </rtc-template>

import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist

from PyQt5.QtCore import Qt, QThread, pyqtSignal,QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton,QGridLayout,QLabel
import tkinter as tk
from tkinter import StringVar

# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
gui_py_spec = ["implementation_id", "GUI_py", 
         "type_name",         "GUI_py", 
         "description",       "ModuleDescription", 
         "version",           "1.0.0", 
         "vendor",            "VenderName", 
         "category",          "Controller", 
         "activity_type",     "STATIC", 
         "max_instance",      "1", 
         "language",          "Python", 
         "lang_type",         "SCRIPT",
         ""]
# </rtc-template>

# <rtc-template block="component_description">
##
# @class GUI_py
# @brief ModuleDescription
# 
# 
# </rtc-template>
class GUI_py(OpenRTM_aist.DataFlowComponentBase):
	
    ##
    # @brief constructor
    # @param manager Maneger Object
    # 
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

        self._d_gui_in = OpenRTM_aist.instantiateDataType(RTC.TimedShort)
        """
        """
        self._gui_inIn = OpenRTM_aist.InPort("gui_in", self._d_gui_in)
        self._d_gui_out = OpenRTM_aist.instantiateDataType(RTC.TimedShort)
        """
        """
        self._gui_outOut = OpenRTM_aist.OutPort("gui_out", self._d_gui_out)


		


        # initialize of configuration-data.
        # <rtc-template block="init_conf_param">
		
        # </rtc-template>


		 
    ##
    #
    # The initialize action (on CREATED->ALIVE transition)
    # 
    # @return RTC::ReturnCode_t
    # 
    #
    def onInitialize(self):
        # Bind variables and configuration variable
		
        # Set InPort buffers
        self.addInPort("gui_in",self._gui_inIn)
		
        # Set OutPort buffers
        self.addOutPort("gui_out",self._gui_outOut)

		
        return RTC.RTC_OK
 
    #
    def onActivated(self, ec_id):
    
        return RTC.RTC_OK
	

    def onDeactivated(self, ec_id):
    
        return RTC.RTC_OK


    def onExecute(self, ec_id):

        root=tk.Tk()

        root.title("Hospital guidance")

        root.geometry("500x450")

        def button_click0():
            self._d_gui_out.data = 0
            self._gui_outOut.write()
        
        def button_click1():
            self._d_gui_out.data = 1
            self._gui_outOut.write()

        def button_click2():
            self._d_gui_out.data = 2
            self._gui_outOut.write()      

        def button_click3():
            self._d_gui_out.data = 3
            self._gui_outOut.write()

        def button_click4():
            self._d_gui_out.data = 4
            self._gui_outOut.write()
            
        button0 = tk.Button(
            text="Home",
            width=50,
            height=3,
            command = button_click0
        )
        button0.place(x=40, y=20) #ボタンを配置する位置の設定

        button1 = tk.Button(
            text="Reception desk",
            width=50,
            height=3,
            command=button_click1,
        )
        button1.place(x=40, y=100) #ボタンを配置する位置の設定

        button2 = tk.Button(
            text="Examination room1",
            width=50,
            height=3,
            command=button_click2,
        )
        button2.place(x=40, y=180) #ボタンを配置する位置の設定

        button3 = tk.Button(
            text="Examination room2",
            width=50,
            height=3,
            command=button_click3,
        )
        button3.place(x=40, y=260) #ボタンを配置する位置の設定

        button4 = tk.Button(
            text="Operation room",
            width=50,
            height=3,
            command=button_click4,
        )
        button4.place(x=40, y=340) #ボタンを配置する位置の設定

        # button5 = tk.Button(
        #     text="Hospital room",
        #     width=168,
        #     height=5,
        # )
        # button5.place(x=80, y=700) #ボタンを配置する位置の設定


    
        root.mainloop()

        return RTC.RTC_OK



def GUI_pyInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=gui_py_spec)
    manager.registerFactory(profile,
                            GUI_py,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    GUI_pyInit(manager)

    # create instance_name option for createComponent()
    instance_name = [i for i in sys.argv if "--instance_name=" in i]
    if instance_name:
        args = instance_name[0].replace("--", "?")
    else:
        args = ""
  
    # Create a component
    comp = manager.createComponent("GUI_py" + args)

def main():
    # remove --instance_name= option
    argv = [i for i in sys.argv if not "--instance_name=" in i]
    # Initialize manager
    mgr = OpenRTM_aist.Manager.init(sys.argv)
    mgr.setModuleInitProc(MyModuleInit)
    mgr.activateManager()
    mgr.runManager()

    

if __name__ == "__main__":
    main()



