# -*- coding: utf-8 -*-
# Copyright (c) 2021, Harsh Mule and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import uuid
from datetime import datetime

class Supplier(Document):
	def before_save(self):
		"""
			to check  whether the supplier account type already exists.
		"""
		supplier = frappe.db.exists(
			'Supplier',
			{
				"email_address": self.email_address,
				"status": self.status
			}
		)
		if supplier:
			frappe.throw("Supplier with the same email exists")
		
		"""
			to create a unique Id for supplier	
		"""
		self.supplier_id = str(uuid.uuid4())
		
		self.created_at = datetime.now()

