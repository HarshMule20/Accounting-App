# -*- coding: utf-8 -*-
# Copyright (c) 2021, Harsh Mule and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class PaymentEntryForSupplier(Document):
	def before_submit(self):
		supplier_exists = frappe.db.exists(
			"Payment Entry for Supplier",
			{
				"supplier_name": self.supplier_name
			}

		)
		if supplier_exists:
			pass
