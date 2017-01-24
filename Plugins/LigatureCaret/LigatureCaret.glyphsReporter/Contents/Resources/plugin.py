# encoding: utf-8

###########################################################################################################
#
#
#	Reporter Plugin
#
#	Read the docs:
#	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/Reporter
#
#
###########################################################################################################

import math
from GlyphsApp.plugins import *

class LigatureCaret(ReporterPlugin):

	def settings(self):
		self.menuName = Glyphs.localize({'en': u'Ligature Caret'})
#		self.generalContextMenus = [
#			{'name': Glyphs.localize({'en': u'Do something', 'de': u'Tu etwas'}), 'action': self.doSomething},
#		]
		
	def foreground(self, layer):
		NSColor.colorWithCalibratedRed_green_blue_alpha_( 0.89, 0.81, 0.37, 0.8 ).set()
		strokeWidth = 3/self.getScale()
		for line in layer.anchors:
			if "caret" in line.name and line.selected:
				x1 = line.position.x
				y1 = Glyphs.font.selectedFontMaster.descender
				x2 = x1
				y2 = Glyphs.font.selectedFontMaster.ascender
				myPath = NSBezierPath.bezierPath()
				myPath.moveToPoint_((x1, y1))
				myPath.lineToPoint_((x2, y2))
				myPath.setLineWidth_(strokeWidth)
				myPath.stroke()
				angle = Glyphs.font.selectedFontMaster.italicAngle
				if angle != 0:
					bottomLeftShift = math.tan(math.radians(angle)) * Glyphs.font.selectedFontMaster.descender
					x1Ital = x1 + round(bottomLeftShift)
					topRightShift = math.tan(math.radians(angle)) * Glyphs.font.selectedFontMaster.ascender
					x2Ital = x2 + round(topRightShift)
					myItalPath = NSBezierPath.bezierPath()
					myItalPath.moveToPoint_((x1Ital, y1))
					myItalPath.lineToPoint_((x2Ital, y2))
					myItalPath.setLineWidth_(strokeWidth)
					myItalPath.stroke()
				

#	def inactiveLayers(self, layer):
#		NSColor.redColor().set()
#		if layer.paths:
#			layer.bezierPath.fill()
#		if layer.components:
#			for component in layer.components:
#				component.bezierPath.fill()
#
	def preview(self, layer):
		NSColor.colorWithCalibratedRed_green_blue_alpha_( 0.89, 0.81, 0.37, 1.0 ).set()
		strokeWidth = 2/self.getScale()
		for line in layer.anchors:
			if "caret" in line.name and line.selected:
				x1 = line.position.x
				y1 = Glyphs.font.selectedFontMaster.descender
				x2 = x1
				y2 = Glyphs.font.selectedFontMaster.ascender
				myPath = NSBezierPath.bezierPath()
				myPath.moveToPoint_((x1, y1))
				myPath.lineToPoint_((x2, y2))
				myPath.setLineWidth_(strokeWidth)
				myPath.stroke()
				angle = Glyphs.font.selectedFontMaster.italicAngle
				if angle != 0:
					bottomLeftShift = math.tan(math.radians(angle)) * Glyphs.font.selectedFontMaster.descender
					x1Ital = x1 + round(bottomLeftShift)
					topRightShift = math.tan(math.radians(angle)) * Glyphs.font.selectedFontMaster.ascender
					x2Ital = x2 + round(topRightShift)
					myItalPath = NSBezierPath.bezierPath()
					myItalPath.moveToPoint_((x1Ital, y1))
					myItalPath.lineToPoint_((x2Ital, y2))
					myItalPath.setLineWidth_(strokeWidth)
					myItalPath.stroke()


#	def doSomething(self):
#		print 'Just did something'
#		
#	def conditionalContextMenus(self):
#
#		# Empty list of context menu items
#		contextMenus = []
#
#		# Execute only if layers are actually selected
#		if Glyphs.font.selectedLayers:
#			layer = Glyphs.font.selectedLayers[0]
#			
#			# Exactly one object is selected and it’s an anchor
#			if len(layer.selection) == 1 and type(layer.selection[0]) == GSAnchor:
#					
#				# Add context menu item
#				contextMenus.append({'name': Glyphs.localize({'en': u'Do something else', 'de': u'Tu etwas anderes'}), 'action': self.doSomethingElse})
#
#		# Return list of context menu items
#		return contextMenus

#	def doSomethingElse(self):
#		print 'Just did something else'
