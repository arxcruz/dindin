#!/usr/bin/env python


#
# Imports
#
from controller.controller import Controller
from interface.basicinterface import BasicInterface


#
# Constants
#


#
# Code
#
if __name__ == '__main__':

    # create user controller
    controller = Controller()

    # associate an interface to the controller
    app = BasicInterface(controller)

    # run interface
    app.run()
