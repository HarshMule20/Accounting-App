# -*- coding: utf-8 -*-
# Copyright (c) 2021, Harsh Mule and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import uuid
from datetime import datetime

class Customer(Document):
	def before_submit(self):
		"""
			to check whether the account of type customer already exists.
		"""
		customer = frappe.db.exists(
			'Customer',
			{
				"email_address": self.email_address,
				"doc_status": 1
			}
		)
		if customer:
			frappe.throw("Customer with the same email exists")

		"""
			to create a unique Id for customer	
		"""
		self.customer_id = str(uuid.uuid4())
		
		self.full_name = f'{self.first_name} {self.last_name}'
		self.created_at = datetime.now()