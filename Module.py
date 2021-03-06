from Generic import *
from ordereddict import OrderedDict
import Cell
import Net
import Port


class Module(Generic):
    "Defines a Verilog Module"
    def __init__(self, attrs):
        attrs["module"] = self
        Generic.__init__(self, attrs)

        # to be linked
        self.__cells = OrderedDict()
        self.__nets  = OrderedDict()
        self.__ports = OrderedDict()

        self.__topmod = None
        self.__submod = None
	self.__uniq = None

    cells = property(lambda self: self.__cells)
    nets  = property(lambda self: self.__nets)
    ports = property(lambda self: self.__ports)
    topmod = property(lambda self: self.__topmod)
    submod = property(lambda self: self.__submod)
    uniq = property(lambda self: self.__uniq)

    def link_topmod(self, topmod):
    	self.__topmod = topmod

    def link_submod(self, submod):
    	self.__submod = submod

    def set_uniq(self, uniq):
    	self.__uniq = uniq

    #link!
    def new_cell(self, cellAttr):
        cellAttr["module"] = self
        # create new cell here
        cell = Cell.Cell(cellAttr)
        self.__cells[cell.name] = cell
        return cell

    def new_net(self, netAttr):
        netAttr["module"] = self
        net = Net.Net(netAttr)
        self.__nets[net.name] = net
        return net

    def new_port(self, portAttr):
        portAttr["module"] = self
        port = Port.Port(portAttr)
        self.__ports[port.name] = port
        return port

    def add_port(self, port):
        self.__ports[port.name] = port
        return port
