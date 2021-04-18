# -*- coding: utf-8 -*-
# Copyright (c) 2021, Harsh Mule and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from datetime import datetime

class FiscalYear(Document):
	def before_submit(self):
		self.start_date = datetime.now().date().replace(month=1, day=1)
		self.end_date = datetime.now().date().replace(month=12, day=31)
		self.created_at = datetime.now()