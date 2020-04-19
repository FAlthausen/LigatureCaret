# encoding: utf-8
from __future__ import division, print_function, unicode_literals

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

import objc
from GlyphsApp import *
from GlyphsApp.plugins import *
from math import tan, radians

class LigatureCaret(ReporterPlugin):

	@objc.python_method
	def settings(self):
		self.menuName = Glyphs.localize({
			'en': 'Ligature Caret',
			'de': 'Einfügemarken in Ligaturen',
			'fr': 'les curseurs dans les ligatures',
			'es': 'cursores en ligaturas',
		})

	@objc.python_method
	def drawCaret( self, layer, selectionCounts=False ):
		try:
			master = layer.master
			strokeWidth = 1.5/self.getScale()
			for line in layer.anchors:
				if "caret" in line.name and (line.selected or not selectionCounts):
					# draw upright caret:
					x1 = line.position.x
					y1 = master.descender
					x2 = x1
					y2 = master.ascender
					uprightCaret = NSBezierPath.bezierPath()
					uprightCaret.moveToPoint_((x1, y1))
					uprightCaret.lineToPoint_((x2, y2))
					uprightCaret.setLineWidth_(strokeWidth)
					angle = master.italicAngle
					
					if angle != 0:
						# also draw italic slant caret:
						bottomLeftShift = tan(radians(angle)) * master.descender
						topRightShift = tan(radians(angle)) * master.ascender
						x1Ital = x1 + round(bottomLeftShift)
						x2Ital = x2 + round(topRightShift)
						italicCaret = NSBezierPath.bezierPath()
						italicCaret.moveToPoint_((x1Ital, y1))
						italicCaret.lineToPoint_((x2Ital, y2))
						italicCaret.setLineWidth_(strokeWidth)
						italicCaret.stroke()
						
						# dash upright caret if italic:
						dashPatternValues = (1.0,3.0)
						dashPattern = tuple(3*v/self.getScale() for v in dashPatternValues)
						uprightCaret.setLineDash_count_phase_(dashPattern, len(dashPattern), 0)
						
					uprightCaret.stroke()
					
		except Exception as e:
			import traceback
			print(traceback.format_exc())
			self.logToConsole( "drawCaret: %s" % str(e) )
			
	@objc.python_method
	def background(self, layer):
		NSColor.colorWithCalibratedRed_green_blue_alpha_( 0.79, 0.71, 0.27, 0.8 ).set()
		self.drawCaret(layer)

	@objc.python_method
	def preview(self, layer):
		NSColor.colorWithCalibratedRed_green_blue_alpha_( 0.89, 0.81, 0.37, 0.8 ).set()
		self.drawCaret(layer, selectionCounts=True)

	@objc.python_method
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__
