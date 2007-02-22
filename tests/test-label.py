#!/usr/bin/env python

# Copyright (C) 2007, One Laptop Per Child
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
import gtk
import hippo

from sugar.graphics.toolbar import Toolbar
from sugar.graphics.label import Label
from sugar.graphics.iconbutton import IconButton

import os
theme = gtk.icon_theme_get_default()
theme.prepend_search_path(os.path.join(os.path.dirname(__file__), 'data'))

BUTTON_DELETE = 1
    
window = gtk.Window()
window.connect("destroy", lambda w: gtk.main_quit())
window.show()

canvas = hippo.Canvas()
window.add(canvas)
canvas.show()

vbox = hippo.CanvasBox()
canvas.set_root(vbox)

toolbar = Toolbar()
vbox.append(toolbar)

button = IconButton('theme:stock-close')
toolbar.append(button)

label = Label('mec moc')
toolbar.append(label)

label = Label()
label.props.text = 'mac mic'
toolbar.append(label)

gtk.main()