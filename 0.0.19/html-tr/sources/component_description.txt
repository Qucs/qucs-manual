
Component Description
=====================


Typicaly the *Qucs* schematic is saved as a ``.sch`` file to store the components, wires, painigs and settings defined by the user.
Prior to simulation with *Qucsator* the schematic is translated into a ``.txt`` netlist file which is presente to the simulator.
The general format of schematic and netlist entries are listed below.


Schematic Component
-------------------

Schematic entry general form:

  ``<[model] [name][number] active x y xtext ytext mirrorX rotate ["value" visible]* >``

Examples:

  ``<R R1 1 170 90 -26 15 0 0 "50 Ohm" 1 "26.85" 0 "0.0" 0 "0.0" 0 "26.85" 0 "european" 0>``

  ``<Vdc V1 1 160 380 18 -26 0 1 "1 V" 1>``

  ``<GND * 1 160 470 0 0 0 0>``

  ``<Circulator X1 1 410 400 -26 -33 0 0 "50 Ohm" 0 "50 Ohm" 0 "50 Ohm" 0>``


Note that the ``GND`` ground componet will not be present on the netlist.
The ground node is unique and implicitly devined by the simulator.


Netlist Component
-----------------

Netlist entry general form:

  ``[model]:[name][number] _net[number]+ [propery="value"]*``

Examples:

  ``R:R1 _net0 _net1 R="50 Ohm" Temp="26.85" Tc1="0.0" Tc2="0.0" Tnom="26.85"``

  ``Vdc:V1 _net6 _net7 U="1 V"``

  ``Circulator:X1 _net16 _net17 _net18 Z1="50 Ohm" Z2="50 Ohm" Z3="50 Ohm"``



