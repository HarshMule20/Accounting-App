# -*- coding: utf-8 -*-
# Copyright (c) 2021, Harsh Mule and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from datetime import datetime

class Items(Document):
	def before_save(self):
		self.created_at = datetime.now()
		if self.price <= 0:
			frappe.throw("Amount/Price cannot set to 0 or less than 0")
